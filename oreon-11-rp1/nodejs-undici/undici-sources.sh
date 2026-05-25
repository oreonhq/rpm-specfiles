#!/bin/sh
set -e
check_deps() {
    deps_ec=0
    for dep in "$@"; do
        command -v "$dep" >/dev/null || {
            printf 'Missing dependency: %s\n' "$dep" >&2
            deps_ec="$((deps_ec + 1))"
        }
    done
    return "$deps_ec"
}
check_deps curl rpm npm nodejs-packaging-bundler

UNDICI_VERSION="$(rpm --specfile nodejs-undici.spec --qf '%{VERSION}\n')"; readonly UNDICI_VERSION

RPKG=fedpkg
RELEASE=""
OFFLINE=false

usage() {
    echo "${0##*/} - download and re-package upstream undici sources."
    echo
    echo Options:
    printf '\t%s\n' '-h, --help: Show this info and exit.'
    printf '\t%s\n' '-r<TOOL>, --rpkg=<TOOL>: Use <TOOL> for dist-git interaction [default: fedpkg].'
    printf '\t%s\n' '--release=<RELEASE>: Tell <TOOL> to assume working on <RELEASE> [default: detected from current branch].'
    printf '\t%s\n' '-n, --offline: Do not upload prepared sources to lookaside cache.'
}

# Construct upstream archive URL
github_archive_url() {
    readonly gh_version="${1-${UNDICI_VERSION}}"
    printf 'https://github.com/nodejs/undici/archive/v%s/undici-v%s.tar.gz' "${gh_version}" "${gh_version}"
}

# Fetch upstream release
# stdout: name of the original/upstream archive
fetch() {
    readonly fetch_version="${1-${UNDICI_VERSION}}"
    # npm archive does not contain everything (i.e. build scripts).
    # Fetch the github archive instead.
    fetch_url="$(github_archive_url "${fetch_version}")"; readonly fetch_url
    curl --location --remote-name "${fetch_url}"
    printf '%s\n' "${fetch_url##*/}"
}

# Delete any file where a WASM blob is detected
# stdout: relative paths to deleted files
nuke_wasm() {
    find "${1-.}" -type f \
        -exec grep -q --text -Pe '\x{0}asm|AGFzb' '{}' \; \
        -print \
        -delete
}

# Remove husky (git hook manager) from prepare scripts
remove_husky() {
    cd "${1-undici-v${UNDICI_VERSION}/}" >/dev/null
    if grep -q 'husky' package.json; then
        npm pkg delete scripts.prepare
    fi
    cd - >/dev/null
}

# Package the sources into stripped archive
repackage() {
    readonly repackage_version="${1-${UNDICI_VERSION}}"
    readonly repackage_rootdir="${2-undici-v${repackage_version}/}"

    tar -czf "undici-${repackage_version}-stripped.tar.gz" "${repackage_rootdir}"
    echo "undici-${repackage_version}-stripped.tar.gz"
}

# shellcheck disable=SC2046
set -- $(getopt -n "${0##*/}" --unquoted -o hr:n -l help,rpkg:,release:,offline -- "$@")
while test -n "$1"; do
    case "$1" in
        -h|--help) usage >&2 && exit;;
        -r|--rpkg) RPKG="$2"; shift 2;;
        -n|--offline) OFFLINE=true; shift 1;;
        --release) RELEASE="$2"; shift 2;;
        --) break;;
        *) printf 'Unknown argument: %s\n' "$1" >&2; exit 2;;
    esac
done

printf '=== %s ===\n' 'Fetching and unpacking upstream tarball' >&2
original="$(fetch "${UNDICI_VERSION}")"; readonly original
tar -xzf "${original}"
rootdir="$(ls -d "undici-${UNDICI_VERSION}/")"; readonly rootdir
rm  -rf  "${original}"

printf '=== %s ===\n' 'Removing following WASM blobs' >&2
nuke_wasm "${rootdir}" >&2

printf '=== %s ===\n' 'Cleaning package scripts' >&2
remove_husky "${rootdir}"

printf '=== %s ===\n' 'Re-packaging clean archive' >&2
repackage "${UNDICI_VERSION}" "${rootdir}"

printf '=== %s ===\n' 'Bundling dependencies' >&2
nodejs-packaging-bundler undici "${UNDICI_VERSION}" "undici-${UNDICI_VERSION}-stripped.tar.gz"
install -p -m0644 -t "${PWD}" "$(rpm -E '%{_sourcedir}')"/undici-"${UNDICI_VERSION}"-*

printf '=== %s ===\n' 'Updating dist-git sources' >&2
# shellcheck disable=SC2086,SC2046
${RPKG} $(test -n "${RELEASE}" && echo --release="${RELEASE}") new-sources $("$OFFLINE" && echo --offline) \
    "undici-${UNDICI_VERSION}-stripped.tar.gz" \
    "undici-${UNDICI_VERSION}-nm-prod.tgz" \
    "undici-${UNDICI_VERSION}-nm-dev.tgz" \
    "undici-${UNDICI_VERSION}-bundled-licenses.txt"

printf '=== %s ===\n' 'Detecting bundled versions' >&2
awk '/^#define LLHTTP_VERSION/{print $NF;}' "${rootdir}/deps/llhttp/include/llhttp.h" \
| xargs printf 'llhttp: %d.%d.%d\n'
