#!/usr/bin/bash
# Execute snapm unit tests from a checked out dist-git repo

set -euxo pipefail

source /etc/os-release

# Move to the directory with sources
cd ${TMT_SOURCE_DIR}

# Extract the Source0 basename without extension
SRC_DIR=$(spectool --source 0 snapm.spec | sed 's/.\+\(snapm-[0-9.]\+\)\.tar\.gz/\1/')

# Move to the extracted sources directory (patches are applied by default)
cd "${SRC_DIR}"

# Configure snapm
cp -r etc/snapm/ /etc
cp systemd/*.service systemd/*.timer /usr/lib/systemd/system
cp systemd/tmpfiles.d/snapm.conf /usr/lib/tmpfiles.d
systemctl daemon-reload
systemd-tmpfiles --create /usr/lib/tmpfiles.d/snapm.conf

# Run tests
sudo pytest -v --log-level=debug tests/
