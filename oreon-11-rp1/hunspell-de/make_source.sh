#!/bin/sh

datestr=$(date +%Y%m%d)
rm -rf dict-de-$datestr dict-de-$datestr.tar.xz
mkdir dict-de-$datestr
pushd dict-de-$datestr

wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/COPYING_GPLv2
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/COPYING_GPLv3
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/README_de_DE_frami.txt
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/README_extension_owner.txt
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_AT_frami.aff
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_AT_frami.dic
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_CH_frami.aff
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_CH_frami.dic
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_DE_frami.aff
wget --content-disposition https://cgit.freedesktop.org/libreoffice/dictionaries/plain/de/de_DE_frami.dic

popd

tar cfJ dict-de-$datestr.tar.xz dict-de-$datestr
rm -rf dict-de-$datestr
echo "Created dict-de-$datestr.tar.xz!"
