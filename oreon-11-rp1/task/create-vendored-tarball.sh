#!/bin/bash

# Copyright 2025 Ankur Sinha
# Author: Ankur Sinha <sanjay DOT ankur AT gmail DOT com> 
# File : create-vendored-tarball.sh

if [ 1 -ne $# ]
then
    echo "One argument required: version"
    exit -1
fi


VERSION="$1"
PACKAGE="task"

echo "Creating vendored tarball for ${PACKAGE} version ${VERSION}"

tar -xvf "${PACKAGE}-${VERSION}.tar.gz"
pushd "${PACKAGE}-${VERSION}"
    rm Cargo.lock -f
    cargo vendor --versioned-dirs
    tar -Jcvf ../"${PACKAGE}-${VERSION}-vendored.tar.xz" vendor/
popd

echo "Vendored tarball created"
echo "Please remember to upload this using 'fedpkg sources' also"
