#!/bin/bash -
set -e
set -x

# This only makes sure that virt-v2v isn't totally broken.
# virt-v2v is extensively tested on real guests by the QE
# team using a mix of automated and manual testing.

# Fix libvirt.
systemctl restart virtqemud virtsecretd virtstoraged virtnetworkd

virt-builder fedora-30
virt-v2v -i disk fedora-30.img -o null
