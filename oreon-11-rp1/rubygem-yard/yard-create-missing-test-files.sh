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

GEMNAME=yard
TMPDIR=$(mktemp -d /tmp/${GEMNAME}-XXXXXX)
CURDIR=$(pwd)
GITTOPDIR=${GEMNAME}-${VERSION}

pushd $TMPDIR

git clone http://github.com/lsegal/${GEMNAME} ${GITTOPDIR}
cd ${GEMNAME}-$VERSION

git checkout -b fedora-$VERSION v$VERSION
cd ..

tar czf $CURDIR/${GEMNAME}-${VERSION}-test-missing-files.tar.gz \
	${GITTOPDIR}/spec/ \

popd
rm -rf $TMPDIR

