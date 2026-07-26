#!/bin/bash

# This script is intended to make a xine-ui snapshot.
# If no argument is provided, it will make a snapshot of HEAD.
# If the svn revision is provided as an argument, it will make a snapshot of
# this revision.

TMPDIR=$(mktemp -d)
pushd "$TMPDIR" || exit
echo -n "Cloning xine-ui "
[ -n "$1" ] && echo "revision $1" || echo "HEAD"
[ -n "$1" ] && OPT="-u $1 " || OPT=""
hg clone $OPT http://hg.code.sf.net/p/xine/xine-ui xine-ui
cd xine-ui || exit
autoreconf -vif
./configure
make dist
popd || exit
cp -p "$TMPDIR"/xine-ui/xine-ui-*.tar.xz .
rm -rf "$TMPDIR"
