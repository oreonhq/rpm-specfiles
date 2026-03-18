#!/usr/bin/bash

# Use a side tag to build libtree-sitter and everything that depends on
# it.  Where we have no permission to do the build ourselves, raise a
# pull request instead.
#
# Run in place of `fedpkg build`.  E.g.,
#   fedpkg switch-branch rawhide
#   ...
#   fedpkg commit
#   fedpkg push
#   ./chain-build.sh <rhbz-number>

# MIT License
#
# Copyright (c) 2025 Peter Oliver
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# TODO: Make this script idempotent, so that it can simply be re-run in
# the event of failures.

set -o errexit
set -o nounset
set -o pipefail

function usage {
    echo "usage: $BASH_ARGV0 [-P] [-d|-v] [bug-number]"
    exit 2
}

no_pull_requests=
quiet=-q
while getopts 'dPv' OPT; do
    case "$OPT" in
    d)
        set -o xtrace
        quiet=
        ;;
    P)
        no_pull_requests=1
        ;;
    v)
        quiet=
        ;;
    *)
        usage
        ;;
    esac
done
shift $((OPTIND - 1))

if (( $# == 1 )); then
    typeset -i bug=$1
    shift;
elif (( $# > 1 )); then
    usage
fi

function create_authorization_header_file {
    local type="$1"
    local filename="${tmp_dir}/${type}_authorization"

    local auth_type
    case "$type" in
    bugzilla)
        auth_type=Bearer
        ;;
    distgit)
        auth_type=token
        ;;
    esac

    if [[ ! -f "$filename" ]]; then
        (
            umask u=rwx,g=,o=
            printf 'Authorization: %s ' "$auth_type" > "$filename"
            if ! crudini --get ~/.config/rpkg/fedpkg.conf "fedpkg.$type" token \
                 >> "$filename"
            then
                case "$type" in
                bugzilla)
                    echo "You can get a token from https://bugzilla.redhat.com/userprefs.cgi?tab=apikey and store it with:
    ( umask u=rwx,g=,o= && crudini --set ~/.config/rpkg/fedpkg.conf fedpkg.bugzilla token ... )"
                ;;
                distgit)
                    echo "You can get a token from https://pagure.io/settings/token/new and store it with:
    fedpkg set-pagure-token"
                ;;
                esac
                return 2;
            fi
        )
    fi
}

# Fail ASAP if unauthenticated:
koji moshimoshi > /dev/null

# Install potential dependencies:
if [[ ! -x /usr/bin/crudini \
          || ! -x /usr/bin/jq ]]; then
    sudo dnf $quiet install -y /usr/bin/crudini /usr/bin/jq
fi

branch="$(git branch --show-current)"

# Get a list of packages that require libtree-sitter:
packages=($(
    dnf $quiet repoquery \
        --repo=fedora --repo=updates \
        --releasever="${branch#f}" \
        --whatrequires='libtree-sitter.so.*' \
        --qf='%{source_name}\n' \
        | grep -v '^tree-sitter$'
))

# Create a new side tag (or re-use the existing one, if this script
# failed last time it was run):
if [[ -f .side-tag ]]; then
    side_tag="$(cat .side-tag)"

    if fedpkg list-side-tags | grep --quiet --perl-regexp "^$side_tag\s"; then
        echo "Re-using side tag $side_tag"
    else
        echo "Side tag $side_tag no-longer exists.  Will create a new one"
        side_tag=''
    fi
fi
if [[ -z ${side_tag:-} ]]; then
    side_tag="$(
        fedpkg request-side-tag \
               | grep --perl-regexp --only-matching "(?<=^Side tag ').*(?=')"
    )"
    echo "$side_tag" > .side-tag
    koji $quiet wait-repo --no-request "$side_tag"
fi

# Build tree-sitter in the side tag:
verrel="$(fedpkg verrel)"
fedpkg $quiet build --target="$side_tag"
koji $quiet wait-repo --request --build="$verrel" "$side_tag"

# Try to bump and rebuild the requiring packages:
message="Rebuild against $verrel"
tmp_dir="$(mktemp -td tree-sitter-chain-build.XXXXXX)"
declare -i i=0
for package in "${packages[@]}"; do
    fedpkg $quiet clone --branch="$branch" --depth=1 "$package" \
           "$tmp_dir/$package"
    cd "$tmp_dir/$package"

    rpmdev-bumpspec --comment="$message" "$package.spec" >/dev/null
    git add "$package.spec"
    git commit --allow-empty --message="$message"

    if fedpkg $quiet push; then
        # Build the requiring package in the side tag:
        fedpkg $quiet build --target="$side_tag" --nowait
    elif [[ -n $no_pull_requests ]]; then
        echo "Skipping $package, which would require a pull request"
        skipped_packages+=("$package")
        unset packages[$i]
    else
        # We lack permission for the requiring package, so submit a pull
        # request instead.

        fedpkg $quiet fork
        git fetch $quiet --unshallow

        fas_login="$(
            git remote -v \
                | grep --perl-regexp --only-matching \
                       '^(\w+)(?=\s+ssh://(\1)@pkgs\.fedoraproject\.org/forks/\1/rpms/.+ \(push\)$)'
        )"

        git switch $quiet --create "$verrel"
        git push $quiet "$fas_login" "$verrel"

        create_authorization_header_file distgit

        response=$(
            curl \
                ${quiet:+--silent --show-error} \
                --fail-with-body \
                --header @"$tmp_dir/distgit_authorization" \
                --data title="$message" \
                --data branch_to="$branch" \
                --data branch_from="$verrel" \
                --data repo_from="$package" \
                --data repo_from_username="$fas_login" \
                --data repo_from_namespace=rpms \
                --data initial_comment="Please build with: \`fedpkg build --target='$side_tag'\`
${bug:+
Relates to https://bugzilla.redhat.com/show_bug.cgi?id=$bug.
}" \
                "https://src.fedoraproject.org/api/0/rpms/$package/pull-request/new" \
                | jq '.full_url // .'
        )
        if [[ $response == "{*" ]]; then
            echo "Could not find pull request URL in Pagure response"
            echo "$response"
            exit 2
        else
            response="${response#\"}"
            response="${response%\"}"
            pull_request_urls+=("$response")
        fi
    fi
    cd - >/dev/null
    rm -rf "$tmp_dir/$package"
    i=$((i + 1))
done

## If we had permission to push to all of the repos ourselves, we could
## do this here, rather than raising and waiting for the pull requests.
# fedpkg chain-build --target="$side_tag" : $packages
# bodhi updates new --from-tag "$@" "$side_tag"

summary="Tree-sitter and dependent packages are being rebuilt for
$verrel in side tag $side_tag.  Completed builds
will appear at:
    https://koji.fedoraproject.org/koji/builds?inherited=0&tagID=${side_tag##*-}

There should be builds for each of:
    tree-sitter ${packages[*]}

${pull_request_urls:+The following pull requests have been created:
    ${pull_request_urls[*]}

}${skipped_packages:+The following packages were skipped:
    ${skipped_packages[*]}

}When all ${pull_request_urls:+pull requests are merged, and }packages are built, run:
    bodhi updates new --from-tag ${bug:+--bugs=$bug }... '$side_tag'"

echo "

$summary"

if [[ -n ${bug:-} ]]; then
    # We could probably use Kerberos here, but
    # https://bugzilla.redhat.com/docs/en/html/api/core/v1/general.html#authentication
    # says it's not supported.
    create_authorization_header_file bugzilla
    
    curl \
        ${quiet:+--silent --show-error} \
        ${quiet:+--output /dev/null} \
        --fail-with-body \
        --header @"$tmp_dir/bugzilla_authorization" \
        --variable "summary=$summary" \
        --expand-json "{\"id\": \"$bug\", \"comment\": \"{{summary:json}}\"}" \
        "https://bugzilla.redhat.com/rest/bug/$bug/comment"
fi

# Clean up.
rm -r .side-tag "$tmp_dir"
