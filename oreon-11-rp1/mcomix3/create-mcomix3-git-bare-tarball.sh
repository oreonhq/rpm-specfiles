#!/bin/bash

set -x
set -e

REPONAME=mcomix3
GITURL=https://github.com/multiSnow/${REPONAME}.git

DATE=$(date '+%Y%m%d')
TIME=$(date '+%H%M')

TARNAME=${REPONAME}-${DATE}T${TIME}.tar.bz2

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)
pushd $TMPDIR

git clone --mirror $GITURL

mkdir TMP
pushd TMP
git clone ../${REPONAME}.git
cd ${REPONAME}
git log --format=fuller | head -n 12
echo
popd

tar cjf ${TARNAME} ${REPONAME}.git/

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
