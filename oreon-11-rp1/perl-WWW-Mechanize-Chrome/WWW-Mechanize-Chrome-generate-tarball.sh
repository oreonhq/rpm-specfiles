#!/bin/sh

VERSION=$1
PKG=WWW-Mechanize-Chrome

set -e
tar xf $PKG-$VERSION.tar.gz

rm $PKG-$VERSION/t/mixi_jp_index.html
rm $PKG-$VERSION/t/sophos_co_jp_index.html
echo 'use Test::More skip_all => "copyrighted pages removed"' > $PKG-$VERSION/t/50-mech-encoding.t

tar czf $PKG-$VERSION-nocopyright.tar.gz $PKG-$VERSION
rm -rf $PKG-$VERSION
