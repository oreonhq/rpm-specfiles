#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/acpica-tools/acpica-tools-tests/aslts
#   Description: ACPICA ASL grammar validation Test Suite (ASLTS)
#   Author: Mike Gahagan <mgahagan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2015 Red Hat
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
        rlRun "./aslts.sh -u > $log_dir/aslts.sh.out 2>&1" 0 "Running ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER}/tests/aslts.sh... Logging to $log_dir/aslts.sh.out"
        retval=$?
        if [[ $retval -ne 0 || $DeBug -ne 0 ]] ; then
          echo "Creating tarball: $log_dir/aslts_run_log.tar.xz of ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER}/tests/aslts/tmp"
          tar -Jcf $log_dir/aslts_run_log.tar.xz ${RPMBUILDDIR}/BUILD/acpica-unix2-${RPM_VER}/tests/aslts/tmp
        fi
        popd
    rlPhaseEnd

    rlPhaseStartCleanup
        submit_logs
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
