#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz1051221-untraced-symbols-cause-sigsegv-ppc64
#   Description: The test tries to workaround of a bz1051221 a little.
#   Author: Michael Petlan <mpetlan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2014 Red Hat, Inc. All rights reserved.
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
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="ltrace"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "cp hello.c $TmpDir/"
        rlRun "pushd $TmpDir"
        rlRun "gcc -o hello-raw hello.c"
        rlRun "cp hello-raw hello-stripped"
        rlRun "strip ./hello-stripped"
        if rpm -q prelink; then
            rlRun "cp hello-raw hello-prelinked"
            rlRun "cp hello-raw hello-stripped-prelinked"
            rlRun "cp hello-raw hello-prelinked-stripped"
            rlRun "prelink ./hello-prelinked"
            rlRun "strip ./hello-stripped-prelinked"
            rlRun "prelink hello-stripped-prelinked"
            rlRun "prelink hello-prelinked-stripped"
            rlRun "strip hello-prelinked-stripped"
        fi
    rlPhaseEnd

    rlPhaseStartTest
        for binary in hello-*; do
            rlLog "==== TESTING $binary ===="
            rlRun "{ ltrace -e __libc_start_main ./$binary 2> err_$binary.log > out_$binary.log; } 2> superr_$binary.log"
            rlAssertNotGrep "Aborted" superr_$binary.log
            rlAssertNotGrep "SIGSEGV" superr_$binary.log
            rlAssertNotGrep "Segmentation fault" superr_$binary.log
            rlAssertNotGrep "killed" err_$binary.log
            rlAssertNotGrep "SIGSEGV" err_$binary.log
            rlAssertNotGrep "Segmentation fault" err_$binary.log
            rlLog "+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+"
        done
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
