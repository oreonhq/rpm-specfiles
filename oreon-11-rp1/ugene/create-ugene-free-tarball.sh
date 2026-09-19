#!/bin/bash

set -e
set -x

umask 0022

VERSION=${VERSION:-40.1}
FEDORA_TAR_VERSION=${VERSION}

REPONAME=ugene
TARNAME=${REPONAME}

SOURCE_TOP_URL=https://github.com/ugeneunipro/${REPONAME}/archive/

CURRENT_DIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)


pushd $TMPDIR

TARBALL_NAME=${TARNAME}-${FEDORA_TAR_VERSION}.tar.gz
SOURCE_URL=${SOURCE_TOP_URL}/${VERSION}/${TARBALL_NAME}

wget -N ${SOURCE_URL}
rm -rf ${TARNAME}-${VERSION}
tar xzf ${TARBALL_NAME}

pushd ${TARNAME}-${VERSION}

echo "Removing nonfree code"
for NONFREE in \
	src/plugins_3rdparty/psipred
do
	rm -rf $NONFREE
done

echo "done"
popd

tar czf ${TARNAME}-free-${FEDORA_TAR_VERSION}.tar.gz ${TARNAME}-${VERSION}/
mv ${TARNAME}-free-${FEDORA_TAR_VERSION}.tar.gz ${CURRENT_DIR}/

popd
rm -rf $TMPDIR

