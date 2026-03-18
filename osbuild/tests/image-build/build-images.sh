#!/usr/bin/bash
set -euxo pipefail

MANIFESTS_DIR=$1
# check that MANIFESTS_DIR is a directory
if [ ! -d "$MANIFESTS_DIR" ]; then
    echo "Error: $MANIFESTS_DIR is not a directory"
    exit 1
fi

# ensure that we are running on x86_64 architecture
if [ "$(uname -m)" != "x86_64" ]; then
    echo "Error: this script is only supported on x86_64 architecture"
    exit 1
fi

. /etc/os-release

case "${ID}-${VERSION_ID}" in
    fedora-*)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/fedora.json"
        ;;
    rhel-8.*)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/rhel-8.json"
        ;;
    rhel-9.*)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/rhel-9.json"
        ;;
    centos-8)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/centos-8.json"
        ;;
    centos-9)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/centos-9.json"
        ;;
    centos-10)
        IMAGE_MANIFEST="${MANIFESTS_DIR}/centos-10.json"
        ;;
    *)
        echo "Error: unsupported OS: ${ID}-${VERSION_ID}"
        exit 1
        ;;
esac

OUTPUT_DIR=/var/tmp/osbuild-output
STORE_DIR=/var/tmp/osbuild-store
sudo mkdir -p "${OUTPUT_DIR}"
sudo mkdir -p "${STORE_DIR}"

# all the images are built with qcow2 format, so export it
EXPORT_PIPELINE="qcow2"

sudo osbuild --output-directory "${OUTPUT_DIR}" --store "${STORE_DIR}" --export "${EXPORT_PIPELINE}" "${IMAGE_MANIFEST}"
