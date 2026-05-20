#!/usr/bin/env bash
# Extract javapackages-bootstrap component *.tar.zst from Fedora 44 SRPM (for offline source prep).
set -euo pipefail
cd "$(dirname "$0")"
version="${1:-1.27.0}"
release="${2:-2.fc44}"
srpm="javapackages-bootstrap-${version}-${release}.src.rpm"
url="https://kojipkgs.fedoraproject.org/pub/fedora/linux/releases/44/Everything/source/tree/Packages/j/${srpm}"
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT
curl -fsSL "$url" -o "$tmpdir/$srpm"
mkdir -p archive
rpm2cpio "$tmpdir/$srpm" | (cd archive && cpio -idmv '*.tar.zst')
echo "Wrote $(find archive -name '*.tar.zst' | wc -l) archives under $(pwd)/archive/"
