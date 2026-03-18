#!/usr/bin/bash

set -xeuo pipefail

export NO_COLOR=1

TMP=$(mktemp -d)

trap "rm -rf $TMP" EXIT

testcase() {
    set +x
    echo
    echo
    echo "$1"
    echo
    echo
    set -x
}

fix_log() {
    tr '\n' ' ' <log | sponge log
}


cd $TMP
version="0.2.1"
git clone https://git.sr.ht/~gotmax23/ansible-collection-epel --branch="v${version}" --depth=1
cd ansible-collection-epel
mkdir abc
ansible-galaxy collection build .

run="unbuffer ansible-galaxy collection install gotmax23-epel-${version}.tar.gz"
warning="The installed collection will not be picked up in an Ansible run"

testcase "Control: Check plain collection install"
${run} |& tee log
fix_log
(! grep "${warning}" log)

testcase "Check special collection install"
${run} -p abc |& tee log
fix_log
grep "${warning}" log

testcase "Check special collection install with option"
ANSIBLE_GALAXY_COLLECTIONS_PATH_WARNING=1 ${run} -p abc |& tee log
fix_log
grep "${warning}" log

testcase "Check special collection install without option"
ANSIBLE_GALAXY_COLLECTIONS_PATH_WARNING=0 ${run} -p abc |& tee log
fix_log
(! grep "${warning}" log)
