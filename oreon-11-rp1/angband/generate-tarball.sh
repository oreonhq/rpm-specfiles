#!/bin/sh

set -e

VERSION="$(sed -n 's/Version:\s*//p' *.spec)"
GIT_TAG=${VERSION}

# Retrieve and set version
git clone https://github.com/angband/angband.git
 
pushd angband
git reset --hard "${GIT_TAG}"

# Remove restricted assets
## Shockbolt tileset aren't provided under a valid license
rm -rf lib/tiles/shockbolt

## Library binaries should not be distributed
rm -rf src/cocoa
rm -rf src/nds
rm -rf src/win

## Clean up
git apply ../fix-restricted.patch

rm -rf .git
popd

mv angband angband-$VERSION
tar -czvf angband-$VERSION-norestricted.tar.gz angband-$VERSION
rm -rf angband-$VERSION
