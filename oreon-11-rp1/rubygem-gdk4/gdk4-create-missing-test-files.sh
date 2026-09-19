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

GEMN=gdk4

VERSION=$1

TMPDIR=$(mktemp -d /tmp/${GEMN}-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/ruby-gnome/ruby-gnome.git
cd ruby-gnome/

git reset --hard $VERSION || true
tar czf $CURDIR/${GEMN}-${VERSION}-test-missing-files.tar.gz ${GEMN}/test/

popd
rm -rf $TMPDIR

