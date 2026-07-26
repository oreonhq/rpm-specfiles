#!/bin/sh

VERSION=$1

tar -xzvf fuse-$VERSION.tar.gz
rm fuse-$VERSION/roms/*.rom
sed -i -e 's/include roms\/Makefile.am//' fuse-$VERSION/Makefile.am
sed -i -e 's/\$(srcdir)\/roms\/Makefile.am//' fuse-$VERSION/Makefile.in
sed -i -e 's/ROMS =/NOROMS =/' fuse-$VERSION/Makefile.in
sed -i -e 's/roms /\//' fuse-$VERSION/Makefile.in
sed -i -e 's/roms //' fuse-$VERSION/Makefile.in

tar -czvf fuse-$VERSION-noroms.tar.gz fuse-$VERSION

