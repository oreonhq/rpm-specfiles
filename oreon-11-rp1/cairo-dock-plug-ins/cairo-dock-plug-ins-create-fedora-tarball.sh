#!/bin/bash

set -e
set -x

umask 0022

VERSION=${VERSION:-3.5.0}
VERSION_PARENT=${VERSION%.[0-9]}

REPONAME=cairo-dock-plug-ins
TARNAME=cairo-dock-plugins

SOURCE_TOP_URL=https://github.com/Cairo-Dock/${REPONAME}/archive/
GIT_URL=https://github.com/Cairo-Dock/${REPONAME}.git

CURRENT_DIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)

GITTAR_VERSION=${VERSION}
FEDORA_TAR_VERSION=${VERSION}

pushd $TMPDIR

if [ "x${USE_GIT}" != "x" ] ; then
	mkdir HASH
	cd HASH

	git clone --depth 1 ${GIT_URL}
	cd ${REPONAME}
	GITDATE=$(git log | sed -n -e 's|^Date:[ \t]*||p' | sed -e 's| \([+-][0-9][0-9]*\)$| UTC\1|')
	GITDAME_B="$(date -d "${GITDATE}" '+%Y%m%d')"
	GITHASH="$(git log | sed -n -e 's|^commit[ \t]||p')"
	SHORTHASH=$(echo ${GITHASH:0:7})
	cd ..
	cd ..

	GITTAR_VERSION=${GITHASH}
	FEDORA_TAR_VERSION=${VERSION}-${GITDAME_B}git${SHORTHASH}
else
	true
fi

TARBALL_NAME=${TARNAME}-${FEDORA_TAR_VERSION}.tar.gz
SOURCE_URL=${SOURCE_TOP_URL}/${GITTAR_VERSION}/${TARBALL_NAME}

wget -N ${SOURCE_URL}
rm -rf ${TARNAME}-${GITTAR_VERSION}
tar xzf ${TARBALL_NAME}

if [ -d ${REPONAME}-${GITTAR_VERSION} ] ; then
	mv ${REPONAME}-${GITTAR_VERSION} ${TARNAME}-${FEDORA_TAR_VERSION}
fi

pushd ${TARNAME}-${FEDORA_TAR_VERSION}

rm -rf Scooby-Do/
sed -i -e '\@SCOOBY_DO@,\@endif@d' -e '\@with_scooby_do@d' CMakeLists.txt

pushd desklet-rendering
rm -f data/starcraft2.png
sed -i -e '\@starcraft2@d' data/CMakeLists.txt
sed -i src/rendering-desklet-decorations.c -e '\@_register_desklet_decorations.*none@i REMOVE_TO_HERE'
sed -i src/rendering-desklet-decorations.c \
	-e '\@_register_desklet_decorations.*futuristic@,\@REMOVE_TO_HERE@s@^@REMOVE_HERE@'
sed -i src/rendering-desklet-decorations.c -e '\@_register_desklet_decorations.*futuristic@d'
sed -i src/rendering-desklet-decorations.c \
	-e '\@REMOVE_HERE@s@^.*$@@'
popd

cp -p ./weather/data/themes/Classic/na.png ./weather/data/broken.png

popd

tar czf ${TARNAME}-fedora-${FEDORA_TAR_VERSION}.tar.gz ${TARNAME}-${FEDORA_TAR_VERSION}/
mv ${TARNAME}-fedora-${FEDORA_TAR_VERSION}.tar.gz ${CURRENT_DIR}/

popd
rm -rf $TMPDIR

