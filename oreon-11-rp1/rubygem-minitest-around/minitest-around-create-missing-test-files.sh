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
REPONAME=minitest-around

TMPDIR=$(mktemp -d /var/tmp/minitest-around-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/splattael/${REPONAME}.git
cd ${REPONAME}/

git reset --hard v$VERSION
cd ..
ln -sf ${REPONAME} ${REPONAME}-${VERSION}
tar czf $CURDIR/${REPONAME}-${VERSION}-test-missing-files.tar.gz \
	${REPONAME}-${VERSION}/config/ \
	${REPONAME}-${VERSION}/features/ \
	${REPONAME}-${VERSION}/test/ \

popd
rm -rf $TMPDIR

