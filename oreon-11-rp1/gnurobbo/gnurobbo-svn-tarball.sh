#!/bin/sh

#REV=415
REV=$1
VERSION=0.68svn`echo $REV`
NAME=gnurobbo

TMP=/tmp
URL=svn://svn.code.sf.net/p/$NAME/code/$NAME
FOLDER=$NAME-$VERSION

pushd $TMP
rm -rf $FOLDER || true
svn export --force -r $REV $URL $FOLDER || false
pushd $FOLDER
# do not ship unsupported platforms
rm -rfv win32 zaurus gp2x fremantle
rm -fv Makefile.* README.*
# legally questionable stuff
rm -rf data/skins/original data/skins/oily data/sounds
find data/skins -name \*.ttf -print -delete
rm -fv data/levels/original.dat
popd
tar cvJf $TMP/$FOLDER.tar.xz $FOLDER
popd
mv $TMP/$FOLDER.tar.xz .

