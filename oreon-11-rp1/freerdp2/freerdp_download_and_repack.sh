#!/bin/sh
version=$(cat freerdp2.spec | grep "Version: " | tr --squeeze-repeats " " | cut --delimiter " " --fields 2)

echo "Downloading FreeRDP-$version.tar.gz"
curl --silent --location "https://github.com/FreeRDP/FreeRDP/archive/$version/FreeRDP-$version.tar.gz" --output "FreeRDP-$version.tar.gz" || exit 1

echo "Removing utf.h and utf.c"
gzip --decompress "FreeRDP-$version.tar.gz" || exit 1
tar --file "FreeRDP-$version.tar" --delete "*/winpr/libwinpr/crt/utf.h" --delete "*/winpr/libwinpr/crt/utf.c" || exit 1
gzip --best "FreeRDP-$version.tar" --stdout > FreeRDP-$version-repack.tar.gz
rm FreeRDP-$version.tar

echo "FreeRDP-$version-repack.tar.gz is prepared"
exit 0
