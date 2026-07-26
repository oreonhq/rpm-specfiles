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

TMPDIR=$(mktemp -d /tmp/rcairo-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/rcairo/rcairo.git
cd rcairo/

git reset --hard v$VERSION
cd ..

tar czf $CURDIR/rcairo-${VERSION}-test-missing-files.tar.gz rcairo/test/fixture/

popd
rm -rf $TMPDIR

