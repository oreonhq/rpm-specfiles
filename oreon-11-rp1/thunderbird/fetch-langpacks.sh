#!/bin/bash
set -euo pipefail
ver="${1:?version required}"
base="https://archive.mozilla.org/pub/thunderbird/releases/${ver}/linux-x86_64/xpi"
out="thunderbird-langpacks"
rm -rf "$out"
mkdir -p "$out"
langs="af ar ast be bg br ca cak cs cy da de dsb el en-CA en-GB es-AR es-ES es-MX et eu fi fr fy-NL ga-IE gd gl he hr hsb hu hy-AM id is it ja ka kab kk ko lt lv ms nb-NO nl nn-NO pa-IN pl pt-BR pt-PT rm ro ru sk sl sq sr sv-SE th tr uk uz vi zh-CN zh-TW"
for lang in $langs; do
  curl -sfL -o "$out/${lang}.xpi" "${base}/${lang}.xpi"
done
echo "langpacks built under $out"
