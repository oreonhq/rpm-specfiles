#!/bin/sh

NAME="xtideuniversalbios"
REPO="https://www.xtideuniversalbios.org/svn/xtideuniversalbios/trunk/"

workdir="$(mktemp -d)"
trap 'rm -r "$workdir"' EXIT

revision="$(svn export "$REPO" "$workdir/$NAME" | awk '/Exported revision/ { print ($3+0) }')"
mv "$workdir/$NAME" "$workdir/$NAME-r${revision}"
tar -cvzf "$PWD/$NAME-r${revision}.tar.gz" -C "$workdir" "$NAME-r${revision}"
