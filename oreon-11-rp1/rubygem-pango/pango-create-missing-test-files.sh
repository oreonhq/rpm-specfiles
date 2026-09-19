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

TMPDIR=$(mktemp -d /tmp/pango-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/ruby-gnome2/ruby-gnome2.git
cd ruby-gnome2/

git reset --hard $VERSION || true
tar czf $CURDIR/pango-${VERSION}-test-missing-files.tar.gz pango/test/*

popd
rm -rf $TMPDIR

