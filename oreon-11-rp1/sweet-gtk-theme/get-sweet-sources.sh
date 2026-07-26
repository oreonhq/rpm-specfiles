#!/bin/bash

set -eu -o pipefail

function print_help() {
	echo "Usage: get-sweet-sources PATH_TO_SPEC_FILE"
	echo "       get-sweet-sources MASTER_COMMIT AMBAR_COMMIT AMBAR_BLUE_COMMIT AMBAR_BLUEDARK_COMMIT MARS_COMMIT NOVA_COMMIT"
}

function download() {
	REPO_URL="https://github.com/EliverLara/Sweet"
	SUFFIX="$1"
	COMMIT="$2"

	DOWNLOAD_URL="${REPO_URL}/archive/${COMMIT}/Sweet-${COMMIT}.tar.gz"
	echo "Downloading \"${DOWNLOAD_URL}\""

	curl --no-progress-meter --location --remote-name "${DOWNLOAD_URL}"
	if [[ ! -z "${SUFFIX}" ]]; then
		mv -v "Sweet-${COMMIT}.tar.gz" "Sweet-${SUFFIX}-${COMMIT}.tar.gz"
	fi
}


if [[ "$#" -ne 1 ]] && [[ "$#" -ne 6 ]]; then
	print_help
	exit 1
fi

if [[ "$1" == "--help" ]]; then
	print_help
	exit
fi


if [[ "$#" -eq 1 ]]; then
	MASTER_COMMIT="$(grep "$1" -e '%global git_commit_master ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
	AMBAR_COMMIT="$(grep "$1" -e '%global git_commit_ambar ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
	AMBAR_BLUE_COMMIT="$(grep "$1" -e '%global git_commit_ambar_blue ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
	AMBAR_BLUEDARK_COMMIT="$(grep "$1" -e '%global git_commit_ambar_blue_dark ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
	MARS_COMMIT="$(grep "$1" -e '%global git_commit_mars ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
	NOVA_COMMIT="$(grep "$1" -e '%global git_commit_nova ' | grep --only-matching -E -e '[0-9a-fA-F]{40}$')"
else
	MASTER_COMMIT="$1"
	AMBAR_COMMIT="$2"
	AMBAR_BLUE_COMMIT="$3"
	AMBAR_BLUEDARK_COMMIT="$4"
	MARS_COMMIT="$5"
	NOVA_COMMIT="$6"
fi


download "Master" "${MASTER_COMMIT}"
download "Ambar" "${AMBAR_COMMIT}"
download "Ambar-Blue" "${AMBAR_BLUE_COMMIT}"
download "Ambar-Blue-Dark" "${AMBAR_BLUEDARK_COMMIT}"
download "Mars" "${MARS_COMMIT}"
download "Nova" "${NOVA_COMMIT}"
