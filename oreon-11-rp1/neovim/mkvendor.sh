#!/usr/bin/bash -x

set -euo pipefail

nvim_url="$(rpmspec -P neovim.spec | sed -En 's/^Source0:[[:space:]]+//p')"
nvim_archive="$(basename "$nvim_url")"
nvim_tmpdir="$(mktemp --tmpdir -d nvim-XXXXXXXX)"
nvim_srcdir="$(pwd)"

cleanup_tmpdir() {
    popd 2>/dev/null || true
    rm -rf "${nvim_tmpdir}"
}
trap cleanup_tmpdir SIGINT

cleanup_and_exit() {
    cleanup_tmpdir
    if test "$1" = 0 -o -z "$1" ; then
        exit 0
    else
        exit "${1}"
    fi
}

if [ ! -w "${nvim_archive}" ]; then
    curl -Lo "${nvim_archive}" "${nvim_url}"
    fedpkg new-sources "${nvim_archive}"
fi

mkdir -p "${nvim_tmpdir}/src"
tar -zxf "${nvim_srcdir}/${nvim_archive}" -C "${nvim_tmpdir}/src" --strip-components=1

pushd "${nvim_tmpdir}" || cleanup_and_exit 1

cmake \
    -S "${nvim_tmpdir}/src/cmake.deps" \
    -B "${nvim_tmpdir}/deps" -G Ninja \
    -DUSE_BUNDLED=OFF \
    -DUSE_BUNDLED_TS=ON \
    -DUSE_BUNDLED_TS_PARSERS=ON

readarray -t targets < <(basename -a "${nvim_tmpdir}/deps/build/downloads/"treesitter* | \
    xargs -I {} echo build/src/{}-stamp/{}-download)
ninja -C "${nvim_tmpdir}/deps" "${targets[@]}"

nvim_vendor="${nvim_archive%.tar.gz}-vendor"
nvim_vendor_archive="${nvim_vendor}.tar.gz"
tar -zcf "${nvim_srcdir}/${nvim_vendor_archive}" \
    -H pax \
    --numeric-owner \
    --owner=0:0 \
    -C "${nvim_tmpdir}/deps/build/downloads" . \
    --transform="s/^\\./${nvim_vendor}/"
popd

cksum -a sha512 "${nvim_archive}" "${nvim_vendor_archive}" | tee sources

echo
echo "Run: fedpkg new-sources ${nvim_archive} ${nvim_vendor_archive}"

cleanup_and_exit 0
