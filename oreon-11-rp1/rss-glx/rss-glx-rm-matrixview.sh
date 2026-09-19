#!/bin/bash

MV_FILES="matrixview.1 matrixview.c matrixview.desktop matrixview_textures matrixview_textures.h matrixview.xml"
mv_files=
for i in $MV_FILES; do
    mv_files="$mv_files src/$i"
done

usage() {
    cat << EOF
Usage: $0 original_tarball diff-file new_tarball
E.g.: $0 rss-glx_0.8.1.tar.bz2 rss-glx-0.8.1-0.8.1.p.diff rss-glx_0.8.1.p.tar.bz2
Required tools for operation: mktemp patch aclocal automake autoconf tar
EOF
}

tar_type() {
    local filename="$1"
    case "$filename" in
    *.tar.gz|*.tgz)
        echo -z
        ;;
    *.tar.bz2|*.tbz2)
        echo -j
        ;;
    *.tar)
        ;;
    *)
        usage
        exit 1
    esac
}

tar_dir() {
    local filename="$1"
    local dirname="${filename##*/}"
    dirname="${dirname%.tar.bz2}"
    dirname="${dirname%.tbz2}"
    dirname="${dirname%.tar.gz}"
    dirname="${dirname%.tgz}"
    dirname="${dirname%.tar}"
    #dirname="${dirname/rss-glx_/rss-glx-}"
    echo "$dirname"
}

if [ "$#" -ne 3 ]; then
    usage
    exit 1
fi

orig_tb="$1"
if [ "$orig_tb" = "${orig_tb#/}" ]; then
    orig_tb="$PWD/$orig_tb"
fi
orig_tb_type="$(tar_type "$orig_tb")"
orig_tb_dir="$(tar_dir "$orig_tb")"
diff_file="$2"
if [ "$diff_file" = "${diff_file#/}" ]; then
    diff_file="$PWD/$diff_file"
fi
new_tb="$3"
if [ "$new_tb" = "${new_tb#/}" ]; then
    new_tb="$PWD/$new_tb"
fi
new_tb_type="$(tar_type "$new_tb")"
new_tb_dir="$(tar_dir "$new_tb")"

echo "Creating temporary directory."

if ! TEMP_DIR="$(mktemp -d)"; then
    echo "mktemp failed to create a temporary directory. Aborting."
    exit 1
fi

echo "Changing to temporary directory ${TEMP_DIR}."
pushd "$TEMP_DIR"

echo "Unpacking original tarball."
set -x
tar -x "$orig_tb_type" -f "$orig_tb" || exit 3
set +x

pushd "$orig_tb_dir"

echo "Removing files:"
set -x
for i in $mv_files; do
    rm -r "$i" || exit 4
done

echo "Applying diff file."
cat "$diff_file" | patch -p1 || exit 5
set +x


echo 'Regenerating auto* files:'
set -x
rm -f config.guess config.sub ltmain.sh || :
autoreconf -i || exit 6
rm -rf autom4te.cache || :
set +x

popd

echo "Renaming directory:"
set -x
mv -f "$orig_tb_dir" "$new_tb_dir" || exit 9
set +x

echo "Creating new tarball:"
set -x
tar -c "$new_tb_type" -f "$new_tb" "$new_tb_dir" || exit 10
set +x
echo "Created ${new_tb}."

popd
echo "Removing temporary directory ${TEMP_DIR}."
rm -rf "$TEMP_DIR" || exit 11

echo "Done."
