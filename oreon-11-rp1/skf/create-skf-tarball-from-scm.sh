#!/bin/bash

set -x

VERSION=${VERSION:-1.99.2}
DATE=$(date '+%Y%m%dT%H%M')
tmppath=$(mktemp -d /var/tmp/tmpXXXXXX)

CURRENTDIR=$(pwd)
TARBALLNAME=skf_$VERSION-cvs$DATE.tar.gz

pushd $tmppath
rm -rf skf-current

cvs -d :pserver:anonymous@cvs.sourceforge.jp:/cvsroot/skf co skf-current
ln -sf skf-current skf-$VERSION-cvs$DATE

tar czf $TARBALLNAME skf-$VERSION-cvs$DATE/./
mv $TARBALLNAME $CURRENTDIR
popd

rm -rf $tmppath

echo "Done"
