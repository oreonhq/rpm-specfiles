#!/usr/bin/sh
#
# Script to prepare a GIAC spkg for Fedora.  This script is only for the
# package maintainer.
#

VERSION="2.0.0"
VERSIONREV="19"

# The upstream tarball name is: giac"$SOURCEORIG".tar.gz
SOURCEORIG=_"$VERSION"-"$VERSIONREV"

# The name of the output file without tar.gz or tar.bz2 extension
OUTPUTFILEBASENAME=giac-"$VERSION"."$VERSIONREV"

echo >&2 "Testing if the output file already exist in one of gz or bz2 format"
if [ -f "$OUTPUTFILEBASENAME".tar.gz -o -f "$OUTPUTFILEBASENAME".tar.bz2 ] ; then
    echo >&2 "there is already a giac archive of this version"
    exit 1
fi

echo >&2 "Build a temporary working dir"
mkdir -p giac-src
cd giac-src

echo >&2 "Downloading upstream source ..."
wget "https://www-fourier.univ-grenoble-alpes.fr/~parisse/debian/dists/stable/main/source/giac$SOURCEORIG.tar.gz"

echo >&2 "Untar upstream source ..."
tar -xzf giac"$SOURCEORIG".tar.gz


echo >&2 "Removing javagiac ..."
rm -rf giac-"$VERSION"/src/javagiac*

echo >&2 "Removing french html doc, but keep keywords, and working makefiles.
 NB: the french html doc is huge and not GPL.
 It is freely redistibuable only for non commercial purposes ..."
cd giac-"$VERSION"/doc/fr
rm -rf [^Mkx]*
rm -rf *.pdf *.eps *.pdf *.png *.cxx *.cas *.jpg *.tex *.stamp *html* cas* *.fig fig*

echo >&2 "Repair the build procedure with a minimal Makefile.am ..."
echo -e "EXTRA_DIST = xcasmenu xcasex keywords\n\nlocaldocdir = \$(docdir)/fr \n\n\
dist_localdoc_DATA = xcasmenu xcasex keywords html_mall html_mtt html_vall">Makefile.am

echo >&2 "Copy and adjust a minimal Makefile.in ..."
cp ../local/Makefile.in ./
sed -ie 's|localdocdir = $(docdir)/local|localdocdir = $(docdir)/fr|' Makefile.in
sed -ie 's|doc/local|subdir = doc/fr|g' Makefile.in
#
touch html_mall
touch html_mtt
touch html_vall
#


echo >&2 "Building giac source tarball ..."
cd ../../../
tar -cz giac-"$VERSION" -f "$OUTPUTFILEBASENAME".tar.gz
mv "$OUTPUTFILEBASENAME".tar.gz ../
cd ../

echo >&2 "Cleaning extracted dir ..."
rm -rf giac-src

echo >&2 "Finished."
