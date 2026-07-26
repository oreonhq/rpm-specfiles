#!/bin/sh

VERSION=$1

tar -xzvf phd2-$VERSION.tar.gz

#Remove pre-built software
rm -rf phd2-$VERSION/WinLibs
rm -rf phd2-$VERSION/extra_frameworks
rm -rf phd2-$VERSION/thirdparty/*.zip
rm -rf phd2-$VERSION/thirdparty/*.tar.gz
rm -rf phd2-$VERSION/thirdparty/*.tar.bz2
rm -rf phd2-$VERSION/thirdparty/frameworks
rm -rf phd2-$VERSION/thirdparty/HID_Utilities
rm -rf phd2-$VERSION/thirdparty/include
rm -rf phd2-$VERSION/thirdparty/openssag
rm -rf phd2-$VERSION/thirdparty/VidCapture
find . -name "*.dll" -type f -delete
find . -name "*.lib" -type f -delete
find . -name "*.dylib" -type f -delete
find . -name "*.a" -type f -delete
find . -name "*.so" -type f -delete
find . -name "*.so.*" -type f -delete
rm -rf phd2-$VERSION/cameras/qhyccdlibs/qhyfirmware.zip

tar -cJvf phd2-$VERSION-purged.tar.xz phd2-$VERSION 

#Remove temporary directory
rm -rf phd2-$VERSION
