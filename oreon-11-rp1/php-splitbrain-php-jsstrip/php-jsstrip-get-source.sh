#!/bin/bash

set -eu -o pipefail

# Check args

if [[ "$#" -ne 1 ]]; then
	echo "Usage: php-jsstrip-get-source.sh <version>" >&2
	exit 1
fi

version="$1"

# Do the needful

repo_url="https://github.com/splitbrain/php-jsstrip"
repo_dir="php-jsstrip-${version}"

if [[ -d "${repo_dir}" ]]; then
	echo "Error: the \"${repo_dir}\" directory already exists" >&2
	exit 1
fi
if [[ -f "${repo_dir}.tar.gz" ]]; then
	echo "Error: the \"${repo_dir}.tar.gz\" file already exists" >&2
	exit 1
fi

git clone "${repo_url}" --branch "${version}" --depth 1 -- "${repo_dir}"
tar --create --file "${repo_dir}.tar.gz" --gzip --exclude-vcs --verbose -- "${repo_dir}"

rm -rf "${repo_dir}"
