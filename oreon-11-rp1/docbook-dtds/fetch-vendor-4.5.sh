#!/usr/bin/env bash
# Regenerate docbook-dtds-vendor-4.5.tar.xz (4.5 RNG/XSD zips from Fedora F44 SRPM).
set -euo pipefail
cd "$(dirname "$0")"
srpm=docbook-dtds-1.0-91.fc44.src.rpm
url="https://dl.fedoraproject.org/pub/fedora/linux/releases/44/Everything/source/tree/Packages/d/docbook-dtds-1.0-91.fc44.src.rpm"
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT
curl -fsSL "$url" -o "$tmpdir/$srpm"
( cd "$tmpdir" && rpm2cpio "$srpm" | cpio -idmv docbook-rng-4.5.zip docbook-xsd-4.5.zip )
tar -cf docbook-dtds-vendor-4.5.tar -C "$tmpdir" docbook-rng-4.5.zip docbook-xsd-4.5.zip
xz -9f docbook-dtds-vendor-4.5.tar
mv -f docbook-dtds-vendor-4.5.tar.xz .
echo "Wrote $(pwd)/docbook-dtds-vendor-4.5.tar.xz"
