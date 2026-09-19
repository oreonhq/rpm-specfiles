#!/bin/bash

set -e
set -x

umask 0022

VERSION=${VERSION:-3.5.0}
VERSION_PARENT=${VERSION%.[0-9]}


REPONAME=cairo-dock-core
TARNAME=cairo-dock

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
	GITDATE=$(git log -1 | sed -n -e 's|^Date:[ \t]*||p' | sed -e 's| \([+-][0-9][0-9]*\)$| UTC\1|')
	GITDAME_B="$(date -d "${GITDATE}" '+%Y%m%d')"
	GITHASH="$(git log -1 | sed -n -e 's|^commit[ \t]||p')"
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

set +x
echo -n -e "Modifying source \t"

count=0
sed -i -e '\@AVOID_PATENT_CRAP@s@^.*$@@' src/gldit/gldi-config.h.in
grep -rIl AVOID_PATENT_CRAP src/ | while read f
do
	count=$((count + 1))
	mv $f $f.orig
	flag=1
	cat $f.orig | while IFS= read -r line
	do
		if ( echo "$line" | grep -q "#ifndef.*AVOID_PATENT_CRAP" ) ; then
			flag=10
			line=""
		fi
		if [[ ( $flag == 10  ) && ( $(echo "$line" | grep -q "#else" ; echo $? ) == 0 ) ]] ; then
			flag=5
			line=""
		fi
		if [[ ( $flag == 5  ) && ( $(echo "$line" | grep -q "#endif" ; echo $? ) == 0 ) ]] ; then
			flag=1
			line=""
		fi
		if [ $flag == 10 ] ; then
			line=""
		fi
		echo "$line" >> $f
	done
	rm -f $f.orig
	if [ $count -ge 10 ] ; then
		count=$((count - 10))
		echo -n -e "."
	fi
done

echo "done"
set -x
popd

tar czf ${TARNAME}-fedora-${FEDORA_TAR_VERSION}.tar.gz ${TARNAME}-${FEDORA_TAR_VERSION}/
mv ${TARNAME}-fedora-${FEDORA_TAR_VERSION}.tar.gz ${CURRENT_DIR}/

popd
rm -rf $TMPDIR

