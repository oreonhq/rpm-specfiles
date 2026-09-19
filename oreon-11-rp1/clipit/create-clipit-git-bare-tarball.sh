#!/bin/bash

set -x
set -e

REPONAME=ClipIt
GITURL=https://github.com/CristianHenzel/${REPONAME}.git

DATE=$(date '+%Y%m%d')
TIME=$(date '+%H%M')

TARNAME=${REPONAME}-${DATE}T${TIME}.tar.gz

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)
pushd $TMPDIR

git clone --mirror $GITURL

mkdir TMP
pushd TMP
git clone ../${REPONAME}.git
cd ${REPONAME}
git log --format=fuller 2>&1 | head -n 8
#grep version README.md
echo
popd

tar czf ${TARNAME} ${REPONAME}.git/

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
