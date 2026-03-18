#!/bin/bash -
set -e
set -x

# This only makes sure that libguestfs isn't totally broken.

# Fix libvirt.
systemctl restart virtqemud virtsecretd virtstoraged virtnetworkd

libguestfs-test-tool
