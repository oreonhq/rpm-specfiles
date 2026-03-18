#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/libpfm/Sanity/libpfm-testsuite
#   Description: libpfm-testsuite testing by upstream testsuite
#   Author: Michal Kolar <mkolar@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2021 Red Hat, Inc.
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

BUILD_USER=${BUILD_USER:-lbpfmbld}
TESTS_COUNT_MIN=${TESTS_COUNT_MIN:-1}
PACKAGE="libpfm"
REQUIRES="$PACKAGE rpm-build make gcc"
if rlIsFedora; then
  REQUIRES="$REQUIRES dnf-utils"
else
  REQUIRES="$REQUIRES yum-utils"
fi

rlJournalStart
  rlPhaseStartSetup
    rlShowRunningKernel
    rlAssertRpm --all
    rlRun "TmpDir=\$(mktemp -d)"
    rlRun "pushd $TmpDir"
    rlFetchSrcForInstalled $PACKAGE
    rlRun "useradd -M -N $BUILD_USER" 0,9
    [ "$?" == "0" ] && rlRun "del=yes"
    rlRun "chown -R $BUILD_USER:users $TmpDir"
  rlPhaseEnd

  rlPhaseStartSetup "build libpfm"
    rlRun "rpm -D \"_topdir $TmpDir\" -U *.src.rpm"
    rlRun "yum-builddep -y $TmpDir/SPECS/*.spec"
    rlRun "su -c 'rpmbuild -D \"_topdir $TmpDir\" -bp $TmpDir/SPECS/*.spec &>$TmpDir/rpmbuild.log' $BUILD_USER"
    rlRun "rlFileSubmit $TmpDir/rpmbuild.log"
    rlRun "cd \"$TmpDir\"/BUILD/libpfm-*-build/libpfm-*/tests 2>/dev/null || cd \"$TmpDir\"/BUILD/libpfm-*/tests"
    rlRun "su -c 'make PFMLIB=`rpm -ql libpfm | grep .so | head -n 1`' $BUILD_USER"
    rlRun "ldd validate | tee $TmpDir/ldd.log"
    rlRun "grep -q 'libpfm.so' $TmpDir/ldd.log"
  rlPhaseEnd

  rlPhaseStartTest "run testsuite"
    rlRun "su -c './validate &>$TmpDir/testsuite.log' $BUILD_USER"
    rlRun "rlFileSubmit $TmpDir/testsuite.log"
  rlPhaseEnd

  rlPhaseStartTest "evaluate results"
    rlRun "cd $TmpDir"
    rlRun "grep -q 'All tests passed' testsuite.log"
    rlRun "tests_count=\$(grep -o -E '^\s*[0-9]+' testsuite.log | awk '{sum+=\$1} END {print sum}')"
    [ "$tests_count" -ge "$TESTS_COUNT_MIN" ] && rlLogInfo "Test counter: $tests_count" || rlFail "Test counter $tests_count should be greater than or equal to $TESTS_COUNT_MIN"
  rlPhaseEnd

  rlPhaseStartCleanup
    rlRun "popd"
    rlRun "rm -r $TmpDir"
    [ "$del" == "yes" ] && rlRun "userdel -f $BUILD_USER"
  rlPhaseEnd
rlJournalPrintText
rlJournalEnd
