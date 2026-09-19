#!/bin/bash

set -eu -o pipefail

SPECFILE="$(basename "${PWD}").spec"

NAME="$(rpmspec -q --qf '%{NAME}' "${SPECFILE}")"
URL="$(rpmspec -q --qf '%{URL}' "${SPECFILE}")"
VERSION="$(rpmspec -q --qf '%{VERSION}' "${SPECFILE}")"

if [[ -d "${NAME}-${VERSION}" ]]; then
	echo "Directory \"${NAME}-${VERSION}\" is in the way, remove first!" 2>&1
	exit 1
fi

git clone --branch "${VERSION}" --depth 1 "${URL}.git" "${NAME}-${VERSION}"
rm -rf "${NAME}-${VERSION}/.git"

zip -9 "${NAME}-${VERSION}.zip" -r "${NAME}-${VERSION}/"
rm -rf "${NAME}-${VERSION}"
