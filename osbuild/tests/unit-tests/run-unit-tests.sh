#!/usr/bin/bash
# Execute osbuild unit tests from a checked out dist-git repo

set -euxo pipefail

source /etc/os-release

# The 'test/run/test_assemblers.py::test_tar' test case uses system tar to extract the built tar archive.
# However, files in the tar archive can have SELinux context not present in the system policy. Therefore,
# in order for the system tar to be able to set it when extracting the archive, it must be labeled with
# 'install_exec_t' type.

ORIGINAL_TAR_CONTEXT="$(matchpathcon -n "$(which tar)")"
sudo chcon "system_u:object_r:install_exec_t:s0" "$(which tar)"
function restore_tar_context() {
    sudo chcon "${ORIGINAL_TAR_CONTEXT}" "$(which tar)"
}
trap restore_tar_context EXIT

# Run the unit tests
# Note:
# - Ignore the boot test, because it requires qemu-system-x86_64 not available on all distributions.
# - Ignore source code tests, which run linters, since we can't ensure that all linters are available
#   and of the same version as in upstream.
# - Explicitly mark btrfs as unsupported on CentOS / RHEL

if [ "${ID}" == "centos" ] || [ "${ID}" == "rhel" ]; then
    UNSUPPORTED_FS="--unsupported-fs btrfs"
fi

TEST_SELECTION_EXPR="not (TestBoot and boot)"

# disable some tests on RHEL-8
if ([ "${ID}" == "rhel" ] || [ "${ID}" == "centos" ]) && [ "${VERSION_ID%%.*}" == "8" ]; then
    # qemu-img info in RHEL-8 produces "raw" as the image format for "vdi" images, which causes tests to fail. Skip it.
    TEST_SELECTION_EXPR="${TEST_SELECTION_EXPR} and not (test_qemu[ext4-vdi] or test_qemu[xfs-vdi])"
    TEST_SELECTION_EXPR="${TEST_SELECTION_EXPR} and not (TestStages and test_qemu)"
fi

# Move to the directory with sources
cd "${TMT_SOURCE_DIR}"

# Extract the Source0 basename without extension
SRC_DIR=$(spectool --source 0 osbuild.spec | sed 's/.\+\(osbuild-[0-9]\+\)\.tar\.gz/\1/')

# Move to the extracted sources directory (patches are applied by default)
cd "${SRC_DIR}"

sudo python3 -m pytest \
    --rootdir "$(pwd)" \
    --ignore "$(pwd)/test/src" \
    ${UNSUPPORTED_FS:-} \
    -k "${TEST_SELECTION_EXPR}" \
    -v \
    "$(pwd)/test/"
