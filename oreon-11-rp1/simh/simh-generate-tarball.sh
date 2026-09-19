#!/bin/sh

VERSION=$1
MAJOR=${VERSION:0:1}
MINOR=${VERSION:2:2}
PATCH=${VERSION:5:1}

unzip -o simhv$MAJOR$MINOR-$PATCH.zip -d simh-$VERSION
rm simh-$VERSION/VAX/ka655*
rm -Rf simh-$VERSION/Ibm1130
sed -i -e "s/ ibm1130 / /" simh-$VERSION/makefile

tar -czvf simh-$VERSION-noroms.tar.gz simh-$VERSION
