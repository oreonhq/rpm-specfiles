#!/usr/bin/bash
# Prepare the host environment for running the osbuild unit tests.
# This includes installing missing dependencies and tools.

set -euxo pipefail

source /etc/os-release

# Move to the checked out git repo with the test plans
# this should be the root of the dist-git repo
cd "${TMT_TREE}"

# install all test dependencies
sudo dnf install -y \
    rpmdevtools \
    python3-mako \
    python3-pip \
    rpm-ostree \
    dosfstools \
    gdisk \
    python3-tomli-w
sudo dnf builddep -y osbuild.spec

# Install pytst from pip, because the version in some RHEL / CentOS releases is too old
sudo pip3 install pytest

# Make sure that /usr/lib/systemd/boot/efi/linuxx64.efi.stub is available to enable pe32p tests
case "${ID}-${VERSION_ID}" in
    rhel-8.* | centos-8)
        sudo dnf install -y systemd-udev
        ;;
    *)
        sudo dnf install -y systemd-boot-unsigned
        ;;
esac
