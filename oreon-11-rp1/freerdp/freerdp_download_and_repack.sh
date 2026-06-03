#!/bin/sh
set -e
version="${1:?version required}"
srcdir="${2:-.}"

cd "$srcdir"
test -f "FreeRDP-${version}.tar.gz" || \
  curl --fail --silent --location \
    "https://github.com/FreeRDP/FreeRDP/archive/${version}/FreeRDP-${version}.tar.gz" \
    --output "FreeRDP-${version}.tar.gz"

gzip -dc "FreeRDP-${version}.tar.gz" > "FreeRDP-${version}.tar"
tar --file "FreeRDP-${version}.tar" --delete "*/winpr/libwinpr/crt/unicode_builtin.c"
gzip --best --no-name "FreeRDP-${version}.tar" --stdout > "FreeRDP-${version}-repack.tar.gz"
rm -f "FreeRDP-${version}.tar"
