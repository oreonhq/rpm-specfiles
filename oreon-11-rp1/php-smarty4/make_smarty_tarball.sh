#!/bin/bash
#
VERSION=$1
TAG=v${VERSION}
TMPDIR=$(mktemp -d )
pushd ${TMPDIR}
git clone https://github.com/smarty-php/smarty.git
cd smarty
cat > .git/info/attributes << EOF
# tests
/tests -export-ignore
/phpunit.xml -export-ignore
EOF
git archive ${TAG} --format tar.gz --prefix smarty-${VERSION}/ -o ../smarty-${VERSION}.tar.gz
popd
mv ${TMPDIR}/smarty-${VERSION}.tar.gz .
rm -rf ${TMPDIR}
