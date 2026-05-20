#!/usr/bin/env bash
# Regenerate doxywizard-icons.tar.xz from Fedora 44 doxygen SRPM (not on lookaside).
set -euo pipefail
cd "$(dirname "$0")"
srpm=doxygen-1.16.1-3.fc44.src.rpm
url="https://kojipkgs.fedoraproject.org/packages/doxygen/1.16.1/3.fc44/src/${srpm}"
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT
curl -fsSL "$url" -o "$tmpdir/$srpm"
( cd "$tmpdir" && rpm2cpio "$srpm" | cpio -idmv doxywizard-icons.tar.xz )
cp -f "$tmpdir/doxywizard-icons.tar.xz" .
echo "Wrote $(pwd)/doxywizard-icons.tar.xz"
