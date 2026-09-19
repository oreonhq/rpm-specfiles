#!/bin/sh

REL=$1
#SHORTCOMMIT=${COMMIT:0:7}

wget https://github.com/pwaller/pyfiglet/archive/v$REL/pyfiglet-$REL.tar.gz

tar -xzvf pyfiglet-$REL.tar.gz

mv pyfiglet-$REL pyfiglet-$REL

rm -rf pyfiglet-$REL/pyfiglet/fonts-contrib

tar -czvf pyfiglet-$REL-no-contrib-font.tar.gz pyfiglet-$REL

# Cleaning
rm -rf pyfiglet-$REL/
rm -f pyfiglet-$REL.tar.gz
