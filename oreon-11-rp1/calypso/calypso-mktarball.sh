#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
name=calypso
url=git://keithp.com/git/calypso
version=2.0
commit=7317d88263fb9658cd7f1174c6bbcfb0a7ae856a

pushd "$tmp"
git clone ${url}
cd ${name}
git checkout ${commit}
cd ..
mv ${name} ${name}-${commit}
tar cJf "$pwd"/${name}-${commit}.tar.xz --exclude=.git ${name}-${commit}
popd
