#!/usr/bin/sh
set -ex

SOURCEDIR=$1

cd "${SOURCEDIR}" || exit 1

cabal update
cabal build --enable-tests --only-dependencies

cabal test
