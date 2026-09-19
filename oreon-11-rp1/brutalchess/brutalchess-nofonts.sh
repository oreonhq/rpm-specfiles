#!/usr/bin/sh

PROJECT=brutalchess
NAME=$PROJECT-alpha
VERSION=0.5.2
URL=http://sf.net/projects/$PROJECT/files/$NAME/$NAME-$VERSION/$NAME-$VERSION-src.tar.gz
DIR=`pwd`
pushd /tmp
mkdir $PROJECT
cd $PROJECT
wget -N $URL -O $PROJECT.tar.gz
tar xf $PROJECT.tar.gz
pushd $PROJECT-$VERSION/fonts
rm *.TTF *.ttf
popd
tar cJf $DIR/$NAME-$VERSION-nofonts.tar.xz $PROJECT-$VERSION
popd
