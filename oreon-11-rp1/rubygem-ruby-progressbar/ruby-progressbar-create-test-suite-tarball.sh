#!/bin/bash

if [ $# -lt 1 ]
then
  echo "$0 <version>"
  exit 1
fi

set -x
set -e

CURRDIR=$(pwd)
NAME=ruby-progressbar

TMPDIRPATH=$(mktemp -d /var/tmp/${NAME}-tar-XXXXXX)
pushd $TMPDIRPATH

NAME=ruby-progressbar
VERSION=$1


VERSION_TAG=releases/v${VERSION}

git clone https://github.com/jfelchner/${NAME}.git
pushd ${NAME}
git checkout -b fedora-${VERSION} ${VERSION_TAG} ||
	git checkout -b fedora-${VERSION} master
popd

ln -sf ${NAME} ${NAME}-${VERSION}
tar czf ${CURRDIR}/rubygem-${NAME}-${VERSION}-testsuite.tar.gz ${NAME}-${VERSION}/./spec/

popd

rm -rf $TMPDIRPATH
