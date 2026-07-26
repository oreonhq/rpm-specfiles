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

TMPDIR=$(mktemp -d /tmp/gio2-XXXXXX)
CURDIR=$(pwd)

pushd $TMPDIR

git clone https://github.com/ruby-gnome2/ruby-gnome2.git
cd ruby-gnome2/

git reset --hard $VERSION || true
tar czf $CURDIR/gio2-${VERSION}-test-missing-files.tar.gz gio2/test/fixture/

popd
rm -rf $TMPDIR

