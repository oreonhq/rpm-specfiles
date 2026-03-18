#!/bin/bash
set -e

name=log4j
version="$(sed -n 's/Version:\s*//p' *.spec)"

# RETRIEVE
wget "https://archive.apache.org/dist/logging/log4j/${version}/apache-log4j-${version}-src.tar.gz" -O "${name}-${version}.orig.tar.gz"
wget "https://archive.apache.org/dist/logging/log4j/${version}/apache-log4j-${version}-src.tar.gz.asc" -O "${name}-${version}.orig.tar.gz.asc"
wget "https://www.apache.org/dist/logging/KEYS" -O "${name}-${version}.keyring"

# VERIFY
$(rpm -E '%{gpgverify}') --keyring="${name}-${version}.keyring" --signature="${name}-${version}.orig.tar.gz.asc" --data="${name}-${version}.orig.tar.gz"

rm -rf tarball-tmp
mkdir tarball-tmp
pushd tarball-tmp
tar -xf "../${name}-${version}.orig.tar.gz"

# CLEAN TARBALL
find -name '*.jar' -delete
find -name '*.class' -delete
find -name '*.zip' -delete
find -name '*.dll' -delete
rm -rf "apache-log4j-${version}-src/src/site"

tar -czf "../${name}-${version}.tar.gz" *
popd
rm -r tarball-tmp "${name}-${version}.orig.tar.gz"
