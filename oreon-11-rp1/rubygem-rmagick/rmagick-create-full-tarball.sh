#!/bin/bash

if [ $# -lt 1 ]
then
  echo "$0 <version>"
  exit 1
fi

preserve_timestamps()
{
	while read f
	do
		unixtime=$(git log -n 1 --pretty='%ct' -- $f)
		touch -d "@${unixtime}" $f
	done < <(git ls-tree -r --name-only HEAD)

}

set -x
set -e

CURRDIR=$(pwd)

TMPDIRPATH=$(mktemp -d /var/tmp/rmagick-tar-XXXXXX)
pushd $TMPDIRPATH

NAME=rmagick
VERSION=$1

VERSION_TAG=$(
echo $VERSION | sed -e 's|\.| |g' | while read major minor release
do
  echo -n -e "${major}-${minor}-${release}"
done
)


VERSION_TAG=RMagick_${VERSION_TAG}

git clone https://github.com/rmagick/$NAME.git
pushd ${NAME}
git reset --hard ${VERSION_TAG}
preserve_timestamps
popd

ln -sf ${NAME} ${NAME}-${VERSION}
tar czf ${CURRDIR}/rubygem-${NAME}-${VERSION}-full.tar.gz ${NAME}-${VERSION}/./

popd

rm -rf $TMPDIRPATH
