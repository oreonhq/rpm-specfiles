#!/bin/sh
set -o nounset
set -o errexit

FORGEURL='https://github.com/wtclarke/pymapvbvd'

print_help()
{
	cat <<EOF
Usage: $1 VERSION

Generate a source archive containing the test data files for pyMapVBVD that are
tracked in git LFS and are not included in the default source archive. The
result will be named pymapvbvd-test-data.tar.zst and will be written
into the current working directory.

The script attempts to produce a reproducible archive to avoid uploading
near-duplicate archives to the lookaside cache when the test data does not
change from one version to the next. Accordingly, the top-level directory
pymapvbvd-\${VERSION}/ is omitted from the archived paths.
EOF
}

if [ "$#" != '1' ]
then
	exec 1>&2
	print_help "${0}"
	exit 1
elif [ "${1-}" = '-h' ] || [ "${1-}" = '--help' ]
then
	print_help "${0}"
	exit 0
fi

if ! git lfs help >/dev/null 2>/dev/null
then
	exec 1>&2
	echo 'Please install the git-lfs package to use this script.'
	exit 1
fi

VERSION="${1}"
TAG="${VERSION}"
GITDIR="$(echo "${FORGEURL}" | sed -r 's@.*/@@')"

#SOURCE0="${FORGEURL}/archive/${VERSION}/pdfminer.six-${VERSION}.tar.gz"
#TARNAME="$(basename "${SOURCE0}")"
TARDIR="pymapvbvd-${VERSION}"
NEWTAR='pymapvbvd-test-data.tar.zst'

SAVEDIR="${PWD}"
XDIR="$(mktemp -d)"
trap "rm -rvf '${XDIR}'" INT TERM EXIT

cd "${XDIR}"
git clone "${FORGEURL}" "${GITDIR}"
cd "${GITDIR}"
git checkout "${TAG}"
git lfs pull
ls -lh tests/test_data
git lfs ls-files -n |
	while read -r fn
	do
		DESTDIR="${XDIR}/${TARDIR}/$(dirname "${fn}")"
		mkdir -p "${DESTDIR}"
		ln "${fn}" "${DESTDIR}/$(basename "${fn}")"
	done

cd "${XDIR}/${TARDIR}"
# https://www.gnu.org/software/tar/manual/html_section/Reproducibility.html
# We discard mtimes entirely, since git doesn’t store mtimes and they are just
# the time we did the git clone.
TZ=UTC LC_ALL=C tar \
		--create --verbose \
		--sort=name \
		--format=posix \
		--numeric-owner --owner=0 --group=0 \
		--mode=go+u,go-w \
		--pax-option='delete=atime,delete=ctime' \
		--clamp-mtime --mtime='@0' \
		. |
	zstdmt --ultra -22 > "${XDIR}/${NEWTAR}"

cd "${SAVEDIR}"
mv -v "${XDIR}/${NEWTAR}" .
