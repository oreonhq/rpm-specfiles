#!/usr/bin/bash

set -e

NAME=xwayland-satellite
SPEC="${NAME}.spec"
VERSION=$(rpmspec -q --srpm --queryformat "%{version}" ${SPEC})

spectool -g ${SPEC}

tar -xzf ${NAME}-${VERSION}.tar.gz

pushd ${NAME}-${VERSION}
cargo vendor --versioned-dirs vendor
tar -Jcf ../${NAME}-${VERSION}-vendor.tar.xz vendor/
popd

rm -rf ${NAME}-${VERSION}/

