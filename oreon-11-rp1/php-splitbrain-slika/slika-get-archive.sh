#!/bin/bash

set -eu -o pipefail

if [[ "$#" -lt 1 ]]; then
	echo "slika-get-archive: You need to provide the version" >&2
	exit 1
fi

git clone 'https://github.com/splitbrain/slika' --branch "${1}" "slika-${1}"
pushd "slika-${1}"
git lfs checkout
rm -rf .git/ .github/
popd

zip -9 "slika-${1}.zip" -r "slika-${1}/"
rm -rf "slika-${1}/"

