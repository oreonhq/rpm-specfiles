#!/bin/bash

# This script creates source tarball from git
# $1 - revision number to checkout. Use HEAD to checkout the latest revision

: ${1?"You must either provide desired revision number \"X\" to checkout: `basename ${0}` X
                                or fetch the latest revision by: `basename ${0}` HEAD"}

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "${tmp}" -o ! -d "${tmp}" ] || rm -rf "${tmp}"
}

unset CDPATH
pwd="$(pwd)"
name=non-ntk
version=20190925

pushd "${tmp}" > /dev/null
echo "Archiving git revision: ${1}"
git clone git://git.tuxfamily.org/gitroot/non/fltk.git "${name}"
cd "${name}"
commit=$(git rev-list --abbrev-commit --max-count=1 ${1})
git archive --format=tar --prefix="${name}-${version}/" ${1} | xz > "${pwd}/${name}-${version}-git${commit}.tar.xz"
echo "Written: ${name}-${version}-git${commit}.tar.xz"
popd >/dev/null
