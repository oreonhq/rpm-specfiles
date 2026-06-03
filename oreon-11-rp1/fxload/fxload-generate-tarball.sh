#!/bin/sh
set -e
VERSION="${1:?version required}"
srcdir="${2:-.}"
cd "$srcdir"

UPSTREAM="fxload-${VERSION}.tar.gz"
if ! test -f "$UPSTREAM"; then
  curl --fail --silent --location \
    "http://downloads.sourceforge.net/project/linux-hotplug/fxload/${VERSION}/${UPSTREAM}" \
    -o "$UPSTREAM"
fi

rm -rf "fxload-${VERSION}"
tar -xzf "$UPSTREAM"
rm -f "fxload-${VERSION}/a3load.hex"
tar -czf "fxload-${VERSION}-noa3load.tar.gz" "fxload-${VERSION}"
