#!/bin/bash
#
TAG=$1
TMPDIR=$(mktemp -d )
pushd ${TMPDIR}
git clone https://github.com/smarty-gettext/smarty-gettext.git
cd smarty-gettext
cat > .git/info/attributes << EOF
# tests
/phpunit.xml -export-ignore
/tests -export-ignore
/composer.json -export-ignore

# docs
/README.md -export-ignore
/COPYING -export-ignore
/CHANGELOG.md -export-ignore
/AUTHORS -export-ignore
EOF
git archive ${TAG} --format tar.gz --prefix smarty-gettext-${TAG}/ -o ../smarty-gettext-${TAG}.tar.gz
popd
mv ${TMPDIR}/smarty-gettext-${TAG}.tar.gz .
#rm -rf ${TMPDIR}
