#!/bin/sh

VERSION=$1

tar -xzvf toolshed-$VERSION.tar.gz

# Remove objectionable bits of source...
rm -rf toolshed-$VERSION/{cocoroms,dwdos,hdbdos,superdos,disks}

tar -czvf toolshed-$VERSION-noroms.tar.gz toolshed-$VERSION
