#!/bin/bash

if [ 2 -ne $# ]
then
    echo "Two arguments required: postgresql_anonymizer version and cargo-pgrx version"
    exit 1
fi


VERSION="$1"
PACKAGE="postgresql_anonymizer"
PGRXVER="$2"
PGRX="cargo-pgrx"

echo "Creating vendored tarball for ${PACKAGE} version ${VERSION}"

tar -xvf "${PACKAGE}-${VERSION}.tar.bz2" || exit 1
pushd "${PACKAGE}-${VERSION}" || exit 1
    cargo vendor --versioned-dirs
    # copy vendor directory for the subsequent commands to not overwrite needed versions of dependencies
    mkdir vendor.old
    cp -r vendor/* vendor.old/
    cargo add "${PGRX}@${PGRXVER}"
    cargo vendor --versioned-dirs --locked
    cargo vendor --versioned-dirs -s "vendor/${PGRX}-${PGRXVER}/Cargo.toml"
    cp -r vendor.old/* vendor/
    rm -r vendor.old
    tar -Jcvf "../${PACKAGE}-${VERSION}-vendored.tar.xz" vendor/
popd || exit 1

echo "Vendored tarball created"
echo "Please remember to upload this using 'fedpkg sources' also"
