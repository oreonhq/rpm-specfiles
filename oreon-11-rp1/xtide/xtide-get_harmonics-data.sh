#!/bin/sh

DATE=${DATE:-20081228}
INSTALL_DIR=${INSTALL_DIR:-/usr/share/xtide-harmonics/}

FILE=harmonics-dwf-${DATE}-nonfree.tar.bz2
INSTALLFILE=${FILE%.tar.bz2}.tcd

if [ "`id -u -n`" != "root" ] ; then
    echo "You must do this by root"
    exit 1
fi

TMPDIR=$(mktemp -d /tmp/xtide-XXXXXXX)
cd $TMPDIR

wget -N ftp://ftp.flaterco.com/xtide/$FILE || \
    { echo ; echo "Downloading failed." ; exit 1 ; }

bzip2 -dc $FILE | tar xf -
mkdir -p -m 0755 $INSTALL_DIR
install -m 644 $INSTALLFILE $INSTALL_DIR
cd
rm -f $TMPDIR/harmonics*
rmdir $TMPDIR

echo "Installed $INSTALLFILE to $INSTALL_DIR."
