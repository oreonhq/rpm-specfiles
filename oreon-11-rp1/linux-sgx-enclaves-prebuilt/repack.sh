#!/bin/sh

set -e

# @1: archive basename
# @*: paths to strip
repack() {
    basename=$1
    shift

    archive=$basename.tar.gz
    newarchive=$basename-repacked.tar.gz

    echo "Re-packing $archive"
    rm -rf repack
    mkdir repack
    (
	cd repack
	tar zxf ../$archive

	echo "Begin stripping files"
	for arg in "$@"
	do
	    find . -name "$arg" -delete -print
	done
	find . \( -name '*.h' -o -name '*.H' \) -delete -print
	echo "Done stripping files"

	tar zcf ../$newarchive *
    )
    rm -rf repack
    echo "Wrote $newarchive"
}

dcap_version=$(grep '%%global dcap_version\|%global dcap_version' linux-sgx*spec | head -1 | awk '{print $3}')

repack prebuilt_dcap_${dcap_version} \
       libcrypto.a \
       policy.wasm \
       libsgx_qve.signed.so
