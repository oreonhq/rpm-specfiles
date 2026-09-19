#!/bin/bash

set -x
set -e

REPONAME=clover2
GITURL=https://github.com/ab25cq/${REPONAME}.git

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
git log 2>&1 | head -n 3
grep version README.md
echo
popd

tar czf ${TARNAME} ${REPONAME}.git/

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
