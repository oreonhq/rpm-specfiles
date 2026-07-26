#!/bin/bash
set -x
set -e

ORIGDIR=$(pwd)

TMPDIR=$(mktemp -d /var/tmp/parseconfig-XXXXXX)
pushd $TMPDIR

git clone https://github.com/datafolklabs/ruby-parseconfig.git
pushd ruby-parseconfig

VERSION=$(cat lib/version.rb | sed -n -e "s|^.*VERSION[ \t]*=[ \t]*'\(.*\)'.*|\1|p")
TARGZ=rubygem-parseconfig-${VERSION}-tests.tar.gz

tar czf $TARGZ tests/
mv $TARGZ $ORIGDIR

popd
rm -rf $TMPDIR
