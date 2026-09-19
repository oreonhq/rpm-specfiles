#!/bin/bash

VERSION=140.9.0
URL=https://ftp.mozilla.org/pub/firefox/releases/${VERSION}esr/linux-x86_64/xpi/

for u in $URL; do
  mkdir -p langpacks && pushd langpacks
  wget -erobots=off -c -r -l1 -nd -nc -A.xpi -U langpacks $u
popd
done
#pushd langpacks
#for u in `ls *.xpi`; do
#  mv $u icecat-${VERSION}.$u
#done
#find . -type f -name '*.xpi' | while read FILE ; do
#  newfile="$(echo ${FILE} |sed -e 's/.xpi/.langpack.xpi/g')" ;
#  mv "${FILE}" "${newfile}" ;
#done
#popd
rm -f icecat-*-langpacks.tar.gz
tar -zcvf icecat-${VERSION}-langpacks.tar.gz langpacks
rm -rf langpacks
exit 0
