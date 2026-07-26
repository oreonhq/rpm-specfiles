#!/bin/bash

usage() {
	echo "$0 <VERSION>"
}

set -e
set -x

if [ $# -lt 1 ] ; then
	usage
	exit 1
fi

VERSION=$1

TMPDIR=$(mktemp -d /tmp/unf-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/knu/ruby-unf.git unf
cd unf/

git reset --hard v$VERSION
tar czf $CURDIR/unf-${VERSION}-test-missing-files.tar.gz test/

popd
rm -rf $TMPDIR

