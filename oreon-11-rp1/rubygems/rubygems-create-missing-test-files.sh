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

PKGNAME=rubygems
TMPDIR=$(mktemp -d /var/tmp/${PKGNAME}-XXXXXX)
CURDIR=$(pwd)
GITTOPDIR=${PKGNAME}-${VERSION}

pushd $TMPDIR

git clone http://github.com/ruby/${PKGNAME} ${GITTOPDIR}
cd ${PKGNAME}-$VERSION

git checkout -b fedora-$VERSION v$VERSION
cd ..

tar czf $CURDIR/${PKGNAME}-${VERSION}-test-missing-files.tar.gz \
	${GITTOPDIR}/test/ \

popd
rm -rf $TMPDIR

