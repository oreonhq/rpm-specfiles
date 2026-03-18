#!/bin/bash -
set -e
set -x

# This is a difficult package to test in gating because building the
# virt-p2v ISO requires virt-builder, and even if we run it, it
# doesn't prove anything useful.  Doing a full P2V conversion is even
# more difficult (and requires virt-v2v which we are unlikely to
# have).  So just check that the virt-p2v binary looks sane.
tmpdir="$( mktemp -d )"
cd "$tmpdir"
xzcat /usr/lib64/virt-p2v/virt-p2v.xz > virt-p2v
chmod +x virt-p2v
./virt-p2v --version
./virt-p2v --help
./virt-p2v --long-options
./virt-p2v --short-options
cd
rm -r "$tmpdir"
