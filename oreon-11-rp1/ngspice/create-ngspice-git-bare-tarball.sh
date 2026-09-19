#!/bin/bash

set -x
set -e

REPONAME=ngspice
GITURL=https://git.code.sf.net/p/ngspice/${REPONAME}.git

DATE=$(date '+%Y%m%d')
TIME=$(date '+%H%M')

TARNAME=${REPONAME}-${DATE}T${TIME}.tar.gz

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/ngspice-XXXXXX)
pushd $TMPDIR

git clone --mirror $GITURL

cd ./${REPONAME}.git
git log --pretty=fuller | head -n 10
cd ..

tar czf ${TARNAME} ${REPONAME}.git/

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
