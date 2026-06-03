#!/usr/bin/bash
set -e

VERSION="${1:?version required}"
srcdir="${2:-.}"
cd "$srcdir"

UPSTREAM="hplip-${VERSION}.tar.gz"
if ! test -f "$UPSTREAM"; then
  curl --fail --silent --location \
    "https://downloads.sourceforge.net/hplip/${UPSTREAM}" \
    -o "$UPSTREAM"
fi

rm -rf "hplip-${VERSION}"
tar -xaf "$UPSTREAM"
rm -f "hplip-${VERSION}/locatedriver"
tar -czf "hplip-${VERSION}-repack.tar.gz" "hplip-${VERSION}"
