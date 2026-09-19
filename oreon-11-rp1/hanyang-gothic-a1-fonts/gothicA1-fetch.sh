#!/bin/bash

set -eu

# -- verify commit hash

if [[ "$#" -lt 1 ]]; then
	echo "Error: You must provide a git commit hash"
	exit 1
fi

COMMIT_HASH="$1"
if ! echo "${COMMIT_HASH}" | grep --quiet -E -e '^[0-9a-fA-F]{40}$'; then
	echo "Error: The provided argument does not look like a 40-character git commit hash"
	exit 1
fi

# -- create target dir

TARGET_DIR="HanYang-GothicA1-${COMMIT_HASH}"
if [[ -d "${TARGET_DIR}" ]]; then
	echo "Error: Target directory \"${TARGET_DIR}\" already exists"
	exit 3
fi

if ! mkdir "${TARGET_DIR}"; then
	echo "Error: Failed to create target directory \"${TARGET_DIR}\""
	exit 4
fi

# -- fetch files

URL="https://github.com/google/fonts/raw/${COMMIT_HASH}/ofl/gothica1/"

FILE_LIST=(
	GothicA1-Black.ttf
	GothicA1-Bold.ttf
	GothicA1-ExtraBold.ttf
	GothicA1-ExtraLight.ttf
	GothicA1-Light.ttf
	GothicA1-Medium.ttf
	GothicA1-Regular.ttf
	GothicA1-SemiBold.ttf
	GothicA1-Thin.ttf
	OFL.txt
)
FILES_TOTAL=${#FILE_LIST[@]}
FILES_DOWNLOADED=0

OLDDIR="$(pwd)"
cd "${TARGET_DIR}"

ATTEMPTS=3
while [[ "${ATTEMPTS}" -gt 0 ]]; do
	for FILE in ${FILE_LIST[@]}; do
		if [[ -f "${FILE}" ]]; then continue; fi

		echo -n "${FILE}" $'\t'
		if curl --silent --location --remote-time --output "${FILE}" "${URL}${FILE}"; then
			echo "OK ($(stat --format "%s" "${FILE}") bytes)"
			((FILES_DOWNLOADED=FILES_DOWNLOADED+1))
		else
			rm "${FILE}" || true  # Remove any partial downloads
			echo "FAIL"
		fi
	done

	if [[ "${FILES_DOWNLOADED}" -eq "${FILES_TOTAL}" ]]; then
		break
	fi

	((ATTEMPTS=ATTEMPTS-1))
	if [[ "${ATTEMPTS}" -eq 0 ]]; then
		break
	fi

	echo -n "Failed to download some files (${ATTEMPTS} attempts left). Re-trying in 15 seconds."
	sleep 5

	echo -n '.'
	sleep 5

	echo -n '.'
	sleep 5

	echo ""
done

cd "${OLDDIR}"

# -- zip everything up

if [[ "${FILES_DOWNLOADED}" -ne "${FILES_TOTAL}" ]]; then
	echo "Failed to download some files:"
	for FILE in ${FILE_LIST[@]}; do
		if [[ ! -f "${FILE}" ]]; then
			echo "- ${FILE}"
		fi
	done
	exit 11
fi

echo "All files downloaded successfully."
echo -n "Zipping..." $'\t'

if ! zip --quiet -9 "${TARGET_DIR}.zip" -r "${TARGET_DIR}"; then
	echo "Failed!"
	exit 10
fi

echo "Done! (${TARGET_DIR}.zip)"

echo ""
fc-scan \
	-f "%{family[0]};%{style[0]};%{fullname[0]};%{width};%{weight};%{slant};%{fontversion};%{file}\n" \
	"${TARGET_DIR}" \
	| sort -t ';' -k1,1d -k4,4n -k5,5n -k6,6n -k2,2d -k7,7dr \
	| uniq \
	| column --separator ';' -t

