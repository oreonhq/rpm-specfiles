#!/bin/bash
#
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
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="$(rpm -qf --queryformat '%{name}' $(which ltrace))"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlAssertRpm $(rpm -qf $(which gcc))
        rlShowRunningKernel
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "cp reproducer.c $TmpDir"
        rlRun "pushd $TmpDir"
    rlPhaseEnd

    rlPhaseStartTest "ltrace with -o and -c options tracing testing binary"
        rlRun "gcc -x c -o test.bin reproducer.c"
        rlRun "ltrace -o ltrace-test.log -c ./test.bin" 0 "ltrace is crunching a testing binary"
        rlRun -l "cat ltrace-test.log"
        rlAssertGrep "alarm" ltrace-test.log
        rlAssertGreater "There has to be something in output file" $(cat ltrace-test.log | wc -l) 5
    rlPhaseEnd

    rlPhaseStartTest "ltrace with -o and -c options tracing system binary"
        rlRun "ltrace -o ltrace-test-sys.log -c ls" 0 "ltrace is crunching ls"
        rlRun -l "cat ltrace-test-sys.log"
        if rlIsRHEL 8; then
            case "$PACKAGE" in
                "ltrace")
                    # bz#1655368 was fixed on ltrace-0.7.91-28.el8.x86_64, but it is still reproducible on ppc64le
                    if [ "$(arch)" = "ppc64le" ]; then
                        rlLogWarning "RHEL8 ltrace fails to trace system binaries on ppc64le due to bz#1618748/bz#1655368, hence skipping failure checking"
                        skip_system_binary_test=1
                    fi
                    ;;
                "gcc-toolset-9-ltrace" | "gcc-toolset-10-ltrace")
                    if [ "$(arch)" = "ppc64le" ]; then
                        rlLogWarning "RHEL8 gcc-toolset-9-ltrace/gcc-toolset-10-ltrace fails to trace system binaries on ppc64le due to bz#1731119, hence skipping failure checking"
                        skip_system_binary_test=1
                    fi
                    ;;
            esac
        elif rlIsRHEL ">=9" && [[ $PACKAGE =~ ^ltrace ]] && [ "$(arch)" = "ppc64le" ]; then
            rlLogWarning "RHEL >=9 ltrace fails to trace system binaries on ppc64le due to bz#1906881, hence skipping failure checking"
            skip_system_binary_test=1
        elif rlIsFedora 33 && [ "$(arch)" = "ppc64le" ]; then
            rlLogWarning "FC33 ltrace fails to trace system binaries on ppc64le due to bz#1902770, hence skipping failure checking"
            skip_system_binary_test=1
        fi

        # ltrace no longer reports __libc_start_main on rhel-8 x86_64 (rhbz#1654734)
        # search for either malloc or ioctl.
        func_found=0
        for traced_func in "malloc" "ioctl"; do
            if grep "$traced_func" ltrace-test-sys.log; then
                func_found=1
            fi
        done
        if [ $func_found -ne 0 ]; then
            if [ $skip_system_binary_test ]; then
                rlLogWarning "Test was skipped but it seems ok. Review skip check."
            fi
        else
            if [ $skip_system_binary_test ]; then
                rlLogInfo "ltrace output does not contain ioctl or malloc calls (expected failure)"
            else
                rlFail "ltrace output does not contain ioctl or malloc calls"
            fi
        fi

        rlRun "n_lines=$(grep -c . ltrace-test-sys.log)"
        if [ $n_lines -gt 10 ]; then
            if [ $skip_system_binary_test ]; then
                rlLogWarning "Test was skipped but it seems ok. Review skip check."
            fi
        else
            if [ $skip_system_binary_test ]; then
                rlLogInfo "ltrace output does not contain more than 10 lines (expected failure)"
            else
                rlFail "ltrace output does not contain more than 10 lines"
            fi
        fi
    rlPhaseEnd

    rlPhaseStartCleanup "Doing clean-up"
        rlFileSubmit ltrace-test.log
        rlFileSubmit ltrace-test-sys.log
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
    rlPhaseEnd
    rlJournalPrintText
rlJournalEnd
