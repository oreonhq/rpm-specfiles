#! /bin/sh
set -e
d=$(mktemp -d)
o=$(pwd)
cd "$d"
tar xzf "$o"/foobillard-3*.tar.gz
find \( -name '*.ttf' -o -name README.FONTS \) -print0 | xargs -0 rm
tar cjf "$o/foobillard-hobbled.tar.bz2" *
cd "$o"
rm -rf "$d"
