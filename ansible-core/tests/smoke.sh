#!/usr/bin/bash -x

set -euo pipefail

ansible --version

cat <<EOF >inventory
[all]
localhost ansible_connection=local
EOF
export ANSIBLE_INVENTORY=inventory

chroot="fedora-rawhide-x86_64"

ansible localhost -bm setup |& tee out

if ! grep Fedora out; then
    chroot="epel-9-x86_64"
fi

ansible localhost -b \
    -m package \
    -a name=filesystem \
  |& tee out
grep -F 'localhost | SUCCESS' out
(! grep -F 'localhost | CHANGED' out)

ansible localhost -b \
    -m community.general.copr \
    -a "name=gotmax23/community.general.copr_integration_tests chroot=${chroot}" \
  |& tee out
grep -F 'localhost | CHANGED' out

ansible localhost -b \
    -m package \
    -a name=copr-module-integration-dummy-package \
  |& tee out
grep -F 'localhost | CHANGED' out

rpm -ql copr-module-integration-dummy-package
