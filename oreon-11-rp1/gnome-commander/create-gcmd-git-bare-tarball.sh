#!/bin/bash

set -x
set -e

REPONAME=gnome-commander
GITURL=https://gitlab.gnome.org/GNOME/${REPONAME}.git
BRANCH=master

DATE=$(date '+%Y%m%d')
TIME=$(date '+%H%M')

TARNAME=${REPONAME}-${DATE}T${TIME}.tar.gz

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)
pushd $TMPDIR

git clone --mirror $GITURL
tar czf ${TARNAME} ${REPONAME}.git/

pushd ${REPONAME}.git/
git log --first-parent --format=fuller ${BRANCH} | head -n 12
popd

cp -p ${TARNAME} $PWDDIR
popd
rm -rf $TMPDIR
