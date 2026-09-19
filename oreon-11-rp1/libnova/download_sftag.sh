#!/bin/sh

set -e

TAG=$1

git clone --depth 1 --branch $TAG https://git.code.sf.net/p/libnova/libnova libnova-$TAG
tar -I 'zstd -9' -cf libnova-$TAG.tar.zst libnova-$TAG

#Clean up
rm -rf libnova-$TAG
