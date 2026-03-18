#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/acpica-tools/acpica-tools-tests/misc
#   Description: sanity tests for iasl(1) to confirm it fails gracefully when given bad AML code to compile
#   Author: Mike Gahagan <mgahagan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2015 Red Hat, Inc.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include Beaker environment
#. /usr/bin/rhts-environment.sh
#. /usr/share/beakerlib/beakerlib.sh
TESTNAME=$(basename $TEST)
. ../include/include.sh


PACKAGE="acpica-tools"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun mk_test_dirs
        rlRun acpica-tools_prep
    rlPhaseEnd

    rlPhaseStartTest
        rlShowRunningKernel
        pushd ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER}/tests
        rlRun "./run-misc-tests.sh /usr/bin $RPM_VER > $log_dir/run-misc-tests.sh.out 2>&1" 0 "Running ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER}/tests/run-misc-tests.sh...."
        retval=$?
        if [[ $retval -ne 0 || $DeBug -ne 0 ]] ; then
          cp misc/badcode misc/badcode.asl.result misc/grammar misc/grammar.asl.result $log_dir
          diff $log_dir/badcode $log_dir/badcode.asl.result > $log_dir/badcode.diff
          diff $log_dir/grammar $log_dir/grammar.asl.result > $log_dir/grammar.diff
        fi
        popd
    rlPhaseEnd

    rlPhaseStartCleanup
      submit_logs
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
