#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/byacc/Regression/upstream-testsuite
#   Description: Runs the upstream byacc testsuite.
#   Author: Arjun Shankar <ashankar@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2016 Red Hat, Inc.
#
#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 2 of
#   the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see http://www.gnu.org/licenses/.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="byacc"
REQUIRES="byacc gcc glibc-devel make sed rpm-build"
MY_USER="byacctestuser"
DOTEST=$(mktemp)

cat > $DOTEST <<-EOF
#!/bin/bash
set -xe
_BASEDIR=\$1
_TMP=\$(mktemp -d)
rpm --define="_topdir \$_TMP" -Uvh \$_BASEDIR/byacc*.src.rpm
rpmbuild --define="_topdir \$_TMP" -bc \$_TMP/SPECS/byacc.spec
pushd \$(find \$_TMP/BUILD/ -name yacc -type f -exec dirname {} \;)
# In case the test fails, the existcode of make check is non-zero.
# In such case this script fails too because of set -e above.
make check
popd
set -xe
EOF

rlJournalStart
    rlPhaseStartSetup
	rlRun "useradd $MY_USER" 0,9
	rlRun "chown $MY_USER:$MY_USER $DOTEST"
        rlAssertRpm --all
        rlRun "TMP=\$(mktemp -d)"
	rlRun "chmod a+rx $TMP"
        rlRun "pushd $TMP"
        rlFetchSrcForInstalled $PACKAGE
	rlRun "chmod a+r byacc*.src.rpm"
    rlPhaseEnd

    rlPhaseStartTest
	rlRun "su - $MY_USER -c 'bash $DOTEST $(pwd)'"
    rlPhaseEnd

    rlPhaseStartCleanup
	rlRun "popd"
	rlRun "rm -rf $TMP $DOTEST"
	rlRun "userdel -f $MY_USER"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
