#!/bin/sh

VERSION=$(grep Version bitcoin-core.spec | sed -e 's/.* //')

printf "Prepare official script to use a local keyring... "

rm -f bitcoin-offline-pubring.gpg* .#lk* verify.py

tar -xzf bitcoin-${VERSION}.tar.gz --strip-components=3 bitcoin-${VERSION}/contrib/verify-binaries/verify.py
patch -p3 -s -i bitcoin-verify-offline.patch

printf "done.\n"

printf "Creating GPG keyring with public keys that have signed release ${VERSION}... "

yes | ./verify.py --import-keys bin SHA256SUMS > /dev/null 2>&1

# Cleanup
rm -f bitcoin-offline-pubring.gpg~ .#lk* verify.py

printf "done.\n"
