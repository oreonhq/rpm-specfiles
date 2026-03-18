#!/bin/bash
set -e

name=jsr-305
version="$(sed -n 's/Version:\s*//p' *.spec)"

rm -rf "${name}-${version}"

git clone 'https://github.com/amaembo/jsr-305'
pushd 'jsr-305'
git checkout 'd7734b13c61492982784560ed5b4f4bd6cf9bb2c'
popd

mv 'jsr-305' "${name}-${version}"

rm -f "${name}-${version}.tar.gz"
tar -czf "${name}-${version}.tar.gz" "${name}-${version}"
rm -rf "${name}-${version}"
