#!/bin/sh

VERSION=$1

tar -xzvf astrometry.net-$VERSION.tar.gz

#Remove nonfree software
unlink astrometry.net-$VERSION/astrometry
rm -rf astrometry.net-$VERSION/demo
rm -rf astrometry.net-$VERSION/gsl-an

tar -cJvf astrometry.net-$VERSION-clean.tar.xz astrometry.net-$VERSION 

#Remove temporary directory
rm -rf astrometry.net-$VERSION
