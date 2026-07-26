#!/bin/bash

# Prune content from upstream tarballs, generate combined one:
# https://www.redhat.com/archives/fedora-legal-list/2009-February/msg00015.html
# https://www.redhat.com/archives/fedora-legal-list/2009-February/msg00020.html

set -e

if [ -z "$1" -o $# -ne 1 ]; then
  echo "Usage: $0 <validator-version>"
  exit 2
fi

unset CDPATH
tmpdir=
origdir=$(pwd)
version=$1
tbver=${version//./_}
pkg=w3c-markup-validator

# or https://github.com/w3c/markup-validator/archive/refs/tags/validator-1_3-release.tar.gz
url1=http://validator.w3.org/dist/validator-$tbver.tar.gz
url2=http://validator.w3.org/dist/sgml-lib-$tbver.tar.gz

trap cleanup EXIT
cleanup()
{
    set +e
    [ -z "$tmpdir" -o ! -d "$tmpdir" ] || rm -rf "$tmpdir"
}

tmpdir=$(mktemp -d)

cd $tmpdir

curl -O $url1
curl -O $url2

tar zxf $(basename $url1)
tar zxf $(basename $url2)

rm -r validator-$version/htdocs/sgml-lib/ISO-HTML
rm -r validator-$version/htdocs/images/valid_icons

tar cf $origdir/$pkg-$version.tar validator-$version
xz -f -v $origdir/$pkg-$version.tar
