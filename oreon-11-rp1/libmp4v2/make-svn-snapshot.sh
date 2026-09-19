#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
svn=$(date +%Y-%m-%d)
dirname=mp4v2-trunk
rev={$svn}
#mplayer_rev=HEAD

cd "$tmp"
svn checkout http://mp4v2.googlecode.com/svn/trunk/ $dirname
cd $dirname

svn_revision=`LC_ALL=C svn info 2> /dev/null | grep Revision | cut -d' ' -f2`
cd ..
tar jcf "$pwd"/$dirname-r$svn_revision.tar.bz2 $dirname
cd - >/dev/null
