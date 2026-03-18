#!/bin/bash

# We always do a rebase to new upstream's tarball for Fedora Rawhide.
#
# For non-Rawhide Fedora releases, we can sometimes backport specific patches,
# if the rebase is not possible.
#
# This scripts automates this process.

# Since we are operating in a dist-git repository where we can't fix things with
# --force-push if something goes wrong, we need to be extra careful and exit
# immediately if something fails.
set -e

curl https://raw.githubusercontent.com/fedora-sysv/initscripts/master/initscripts.spec -o initscripts.spec || exit 1
spectool -g initscripts.spec

# Make a local scratch build in mock first. If it fails, do not upload new tarball!
# srpm_file="$(basename $(fedpkg srpm | grep -i "wrote" | cut -d ':' -f 2))"
# arch="$(uname -p)"

# mock -r "fedora-rawhide-${arch}" "${srpm_file}" || exit 2

# Scratch build passed, the build should pass in Koji as well. Let's proceed:
fedpkg new-sources "$(basename $(spectool -S -l initscripts.spec | gawk '{print $2;}'))" || exit 3
git add initscripts.spec
git commit -m "$(grep Version initscripts.spec | gawk '{print $2;}')"

git show
