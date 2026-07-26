#!/bin/sh
VERSION=$1
wget -N https://root.cern/download/root_v${VERSION}.source.tar.gz
tar -z -x -f root_v${VERSION}.source.tar.gz
find root-${VERSION}/fonts -type f -a '!' -name 'STIX*' -exec rm {} ';'
tar -J -c --group root --owner root -f root-${VERSION}.tar.xz root-${VERSION}
