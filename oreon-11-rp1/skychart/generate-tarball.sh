#!/bin/sh

VERSION=$1

tar -xJvf skychart-$VERSION-src.tar.xz

#Remove pre-built software
rm -rf skychart-$VERSION-src/tools/data/iridflar
rm -rf skychart-$VERSION-src/tools/data/quicksat
rm -rf skychart-$VERSION-src/skychart/sample_client/astrolabe/*.dll
rm -rf skychart-$VERSION-src/skychart/sample_client/ds2cdc/*.dll.zip

#Remove Mac and Windows unneeded stuff
rm -rf skychart-$VERSION-src/system_integration/Windows
rm -rf skychart-$VERSION-src/system_integration/MacOSX

#Remove libraries provided by separate package libpasastro
#they are here only for building the Win version
rm -rf skychart-$VERSION-src/skychart/library/getdss
rm -rf skychart-$VERSION-src/skychart/library/plan404
rm -rf skychart-$VERSION-src/skychart/library/wcs

#Remove NGC2000 catalog with license problem and no more used
rm -rf skychart-$VERSION-src/tools/cat/ngc2000

tar -cJvf skychart-$VERSION-src-nopatents.tar.xz skychart-$VERSION-src 

#Remove temporary directory
rm -rf skychart-$VERSION-src
