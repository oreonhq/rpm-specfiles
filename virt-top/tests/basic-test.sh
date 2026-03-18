#!/bin/bash -
set -e
set -x

# We need to start libvirtd, see:
# https://bugzilla.redhat.com/show_bug.cgi?id=1682780#c8
systemctl start libvirtd ||:

# I'd like to use the test:/// driver but it doesn't support the right
# APIs.
virt-top --stream -d 1 -n 3 --debug /dev/stdout
