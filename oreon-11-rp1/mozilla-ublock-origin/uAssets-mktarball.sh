#!/bin/bash

set -e

tmp=$(mktemp -d)

trap cleanup EXIT
cleanup() {
    set +e
    [ -z "$tmp" -o ! -d "$tmp" ] || rm -rf "$tmp"
}

unset CDPATH
pwd=$(pwd)
name=uAssets
version=$(rpmspec -q --qf '%{version}' ./mozilla-ublock-origin.spec)
commit_master=0bdd716c769e2ba6fc436b32fb8f5734de4e49fc
commit_gh_pages=a8bca5b245b5c239bca48819faf6e1848eb4dfed
url_master=https://github.com/uBlockOrigin/uAssets/archive/${commit_master}/${name}-${commit_master}.tar.gz
url_gh_pages=https://github.com/uBlockOrigin/uAssets/archive/${commit_gh_pages}/${name}-${commit_gh_pages}.tar.gz
pushd "$tmp"
curl -L ${url_master} | tar xzf -
mv ${name}-${commit_master} main
# Peter Lowe's adservers list is non-commercial-only
# https://github.com/uBlockOrigin/uAssets/issues/7657
rm -r main/thirdparties/pgl.yoyo.org
curl -L ${url_gh_pages} | tar xzf -
mv ${name}-${commit_gh_pages} prod
tar czf "$pwd"/${name}-${version}.tar.gz main prod
popd
