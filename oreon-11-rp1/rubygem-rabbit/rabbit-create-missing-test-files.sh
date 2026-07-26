#!/bin/bash

usage() {
	echo "$0 <VERSION>"
}

set -e
set -x

GEMNAME=rabbit

if [ $# -lt 1 ] ; then
	usage
	exit 1
fi

VERSION=$1

TMPDIR=$(mktemp -d /var/tmp/${GEMNAME}-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/rabbit-shocker/${GEMNAME}.git
cd ${GEMNAME}

git reset --hard $VERSION
cd ..
ln -sf ${GEMNAME} ${GEMNAME}-${VERSION}

tar czf $CURDIR/rubygem-${GEMNAME}-${VERSION}-test-missing-files.tar.gz ${GEMNAME}-${VERSION}/./test/

popd
rm -rf $TMPDIR

