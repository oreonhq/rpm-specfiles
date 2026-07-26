#!/bin/bash

name=etr
delfiles="data/fonts/outline.ttf"

set -e

usage() {
    cat << EOF >&2
Usage: $0 $name-<VERSION>.tar.xz $name-<VERSION>.p.tar.xz
EOF
    exit 1;
}

if [ $# -ne 2 ]; then
    usage
fi

src="$1"
dst="$2"

dstregex="^$name-\([0-9]\+\(\.[0-9]\+\)*\.p\)\.tar\.\(gz\|bzip2\|xz\)\$"
srcregex="$(echo "$dstregex" | sed 's|\\\.p||g')"

fail=0
if [ -n "$(echo "$src" | sed "s/$srcregex//g")" ]; then
    echo "Invalid source tarball filename" >&2
    fail=1
fi
if [ -n "$(echo "$dst" | sed "s/$dstregex//g")" ]; then
    echo "Invalid destination tarball filename" >&2
    fail=1
fi
if [ $fail -ne 0 ]; then
    usage
fi

eval `echo "$src" | sed "s/$srcregex/srcver='\1'\;srcext='\3'/g"`
eval `echo "$dst" | sed "s/$dstregex/dstver='\1'\;dstext='\3'/g"`

case "$srcext" in
    gz)
        unpack=zcat
        ;;
    bz2)
        unpack=bzcat
        ;;
    xz)
        unpack=xzcat
        ;;
    *)
        echo "Invalid source extension: $srcext" >&2
        fail=1
        ;;
esac

case "$dstext" in 
    gz)
        pack=gzip
        ;;
    bz2)
        pack=bzip2
        ;;
    xz)
        pack=xz
        ;;
    *)
        echo "Invalid destination extension: $dstext" >&2
        fail=1
esac

if [ $fail -ne 0 ]; then
    usage
fi

tmpdir="$(mktemp -d)"
trap "rm -rf '$tmpdir'" EXIT

cwd="$PWD"
"$unpack" "$src" | (cd "$tmpdir" && tar xf -)
for f in $delfiles; do
    rm -f "${tmpdir}/${name}-${srcver}/$f"
done
mv "${tmpdir}/${name}-${srcver}" "${tmpdir}/${name}-${dstver}"
(cd "$tmpdir" && tar cvf - "${name}-${dstver}") | \
    "$pack" > "${name}-${dstver}.tar.${dstext}"
