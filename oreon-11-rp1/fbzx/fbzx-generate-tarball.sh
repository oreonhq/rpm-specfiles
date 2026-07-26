#!/bin/sh

NAME=fbzx
VERSION=$1

mkdir $NAME
pushd $NAME
tar xvfz ../$NAME-$VERSION.tar.gz
rm -rf $NAME-$VERSION/data/spectrum-roms/
tar cvfz ../$NAME-$VERSION-noroms.tar.gz $NAME-$VERSION
popd
rm -rf $NAME

