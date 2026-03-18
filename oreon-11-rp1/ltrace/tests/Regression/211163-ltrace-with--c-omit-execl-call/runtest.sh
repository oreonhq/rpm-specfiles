#!/bin/bash

# Copyright (c) 2008 Red Hat, Inc. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Author: Michal Nowak <mnowak@redhat.com>

# source the test script helpers
. /usr/bin/rhts_environment.sh
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE=$(rpm -qf $(which ltrace))

rlJournalStart
    rlPhaseStartSetup "Gathering information & compiling"
        rlAssertRpm $PACKAGE
        rlAssertRpm $(rpm -qf $(which gcc))
        rlShowRunningKernel

        rlRun "gcc reproducer.c -o reproducer" 0 "Compiling the reproducer"
    rlPhaseEnd

    rlPhaseStartTest "Counting the number of calls noted by ltrace"
        rlRun "ltrace -o ltrace-test-c.log -c ./reproducer" 0 "Execute reproducer"
        rlRun "cat -n ltrace-test-c.log"
        # Check if exec is not omitted (rhbz#797761)
        rlAssertGrep "exec" ltrace-test-c.log

        # Check if ltrace is able to trace system binaries with execl /bin/ls (rhbz#1618748/rhbz#1655368/rhbz#1731119)
        if rlIsRHEL 8; then
            case "$PACKAGE" in
                ltrace*)
                    # bz#1655368 was fixed on ltrace-0.7.91-28.el8.x86_64, but it is still reproducible on ppc64le
                    if [ "$(arch)" = "ppc64le" ]; then
                        rlLogWarning "RHEL8 ltrace fails to trace system binaries on ppc64le due to bz#1618748/bz#1655368, hence skipping failure checking"
                        skip_test=1
                    fi
                    ;;
                gcc-toolset-*)
                    if [ "$(arch)" = "ppc64le" ]; then
                        rlLogWarning "RHEL8 gcc-toolset-*-ltrace fails to trace system binaries on ppc64le due to bz#1731119, hence skipping failure checking"
                        skip_test=1
                    fi
                    ;;
            esac
        elif rlIsRHEL ">=9" && [[ $PACKAGE =~ ^ltrace ]] && [ "$(arch)" = "ppc64le" ]; then
            rlLogWarning "RHEL >=9 ltrace fails to trace system binaries on ppc64le due to bz#1906881, hence skipping failure checking"
            skip_test=1
        elif rlIsFedora 33 && [ "$(arch)" = "ppc64le" ]; then
            rlLogWarning "FC33 ltrace fails to trace system binaries on ppc64le due to bz#1902770, hence skipping failure checking"
            skip_test=1
        fi

        rlRun "n_lines_c=$(grep -c . ltrace-test-c.log)"
        if [ $n_lines_c -gt 20 ]; then
            if [ $skip_test ]; then
                rlLogWarning "Test was skipped but it seems ok. Review skip check."
            fi
        else
            if [ $skip_test ]; then
                rlLogInfo"'ltrace -c ./reproducer' does not report more than 20 lines of trace summary output (expected failure)"
            else
                rlFail "'ltrace -c ./reproducer' does not report more than 20 lines of trace summary output"
            fi
        fi
    rlPhaseEnd

    rlPhaseStartTest "Looking for SEGFAULT of reproducer under ltrace"
        rlRun "ltrace -o ltrace-test.log ./reproducer" 0 "Execute reproducer"
        rlRun "cat -n ltrace-test.log"
        # Check if neither segfault nor 'unexpected breakpoint' errors occur (rhbz#211163)
        rlAssertNotGrep "SIGSEGV" ltrace-test.log
        rlAssertNotGrep "unexpected breakpoint" ltrace-test.log
        # Check if exec is not omitted (rhbz#797761)
        rlAssertGrep "exec" ltrace-test.log

        # Check if ltrace is able to trace system binaries with execl /bin/ls (rhbz#1618748/rhbz#1655368/rhbz#1731119)
        rlRun "n_lines=$(grep -c . ltrace-test.log)"
        if [ $n_lines -gt 20 ]; then
            if [ $skip_test ]; then
                rlLogWarning "Test was skipped but it seems ok. Review skip check."
            fi
        else
            if [ $skip_test ]; then
                rlLogInfo"'ltrace ./reproducer' does not report more than 20 lines of trace summary output (expected failure)"
            else
                rlFail "'ltrace ./reproducer' does not report more than 20 lines of trace summary output"
            fi
        fi
    rlPhaseEnd

    rlPhaseStartCleanup "Doing clean-up"
        rlBundleLogs "ltrace-outputs" ltrace-test.log ltrace-test-c.log
        rlRun "rm -f ltrace-test.log ltrace-test-c.log reproducer"
    rlPhaseEnd
    rlJournalPrintText
rlJournalEnd
