#!/bin/bash

set -x
set -e

REPONAME=xml-simple
GITURL=https://github.com/maik/${REPONAME}.git

VERSION=${VERSION:-1.1.9}
GITHASH=${GITHASH:-7b8bdf7b33ab872bb4d1fb8eeecba5c5e1a4a421}

TESTTARBALL=${REPONAME}-tests-${VERSION}.tar.gz

PWDDIR=$(pwd)
TMPDIR=$(mktemp -d /var/tmp/${REPONAME}-XXXXXX)
pushd $TMPDIR

git clone $GITURL
cd ${REPONAME}

git checkout -b fedora-${VERSION} ${GITHASH}
tar czf $TESTTARBALL test/
cp -a $TESTTARBALL $PWDDIR
cd ..

popd
rm -rf $TMPDIR

