#!/bin/bash -e

# Log program and kernel versions
echo "Important package versions:"
(
    uname -r
    rpm -qa | egrep 'podman|conmon|crun|runc|iptable|slirp|systemd|container-selinux' | sort
) | sed -e 's/^/  /'

# Log environment; or at least the useful bits
echo "Environment:"
env | grep -v LS_COLORS= | sort | sed -e 's/^/  /'

bats /usr/share/oci-seccomp-bpf-hook/test/system
