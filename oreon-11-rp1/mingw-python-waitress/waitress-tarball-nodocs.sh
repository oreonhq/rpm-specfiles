#!/bin/bash

if [ $# -lt 1 ]; then
	echo "Usage: $0 version"
	exit 1
fi

VERSION="$1"

srcurl="https://files.pythonhosted.org/packages/source/w/waitress/waitress-$VERSION.tar.gz"
if [ ! -f "waitress-$VERSION.tar.gz" ]; then
    wget $srcurl
fi

if [ -d waitress-$VERSION ] || [ -d waitress-$VERSION-nodocs ]; then
    echo "waitress-$VERSION or waitress-$VERSION-nodocs in the way, please remove and rerun this script"
    exit 1
fi

tar xvf waitress-$VERSION.tar.gz
mv waitress-$VERSION{,-nodocs} && pushd waitress-$VERSION-nodocs
rm -rf docs
popd

tar cvf waitress-$VERSION-nodocs.tar.xz waitress-$VERSION-nodocs
