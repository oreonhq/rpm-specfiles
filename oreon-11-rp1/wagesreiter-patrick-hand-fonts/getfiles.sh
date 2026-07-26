#!/bin/bash
#Try to get upstream latest files

DATE=$(date -u +%Y%m%d)
ARCHIVE=wagesreiter-patrick-hand-fonts-$DATE
SUBDIR=ofl/patrickhand
TMPDIR=$(mktemp -d --tmpdir=/var/tmp getfiles-XXXXXXXXXX)
[ $? != 0 ] && exit 1
umask 022
pushd "$TMPDIR"
git init git
cd git
git config core.sparseCheckout true
cat > .git/info/sparse-checkout << EOF
${SUBDIR}/*
EOF
git remote add -f origin https://github.com/google/fonts/
git pull origin master
cd ..
install -m 0755 -d "$ARCHIVE"
cp -pr git/${SUBDIR}/* "$ARCHIVE"
tar -cvJf "$ARCHIVE.tar.xz" "$ARCHIVE"
popd
mv "$TMPDIR/$ARCHIVE.tar.xz" .
rm -fr "$TMPDIR"
