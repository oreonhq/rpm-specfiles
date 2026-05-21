#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
cd "$here"
version="${1:-7.0.9}"
linux="linux-${version}.tar.xz"
url="https://www.kernel.org/pub/linux/kernel/v7.x/${linux}"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
curl -fsSL "$url" -o "$work/$linux"
tar -xJf "$work/$linux" -C "$work"
cd "$work/linux-${version}"
ARCH_LIST="arm arm64 loongarch powerpc riscv s390 x86"
bundle="$work/bundle"
mkdir -p "$bundle"
for karch in $ARCH_LIST; do
  echo "headers_install ARCH=$karch"
  make ARCH=$karch INSTALL_HDR_PATH="$bundle/arch-$karch" headers_install -j"$(nproc)"
done
out="$here/kernel-headers-${version}.tar.xz"
tar -cJf "$out" -C "$bundle" .
echo "Wrote $out"
