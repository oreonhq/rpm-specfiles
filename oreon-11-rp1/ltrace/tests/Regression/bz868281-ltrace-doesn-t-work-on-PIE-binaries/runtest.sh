#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz868281-ltrace-doesn-t-work-on-PIE-binaries
#   Description: Test for BZ#868281 (ltrace doesn't work on PIE binaries)
#   Author: Miroslav Franc <mfranc@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2013 Red Hat, Inc. All rights reserved.
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

LTRACE_RPM=$(rpm -qf `which ltrace`)
GCC="${GCC:-$(which gcc)}"
GCC_RPM=$(rpm -qf $GCC)
BINUTILS_RPM=$(rpm -qf `which ld`)

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $LTRACE_RPM
        rlAssertRpm $GCC_RPM
        rlAssertRpm $BINUTILS_RPM
        ARCH="$(rlGetPrimaryArch)"
        SARCH="$(rlGetSecondaryArch)"
        for arch in $ARCH $SARCH; do
            rlCheckRpm glibc.$arch
        done
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "cp reproducer.c $TmpDir"
        rlRun "pushd $TmpDir"

        if [ -d /usr/lib64 ]; then
            if [[ $ARCH =~ s390.* ]]; then
                if rlIsRHEL '>=8'; then
                    rlLogInfo "RHEL-8 and newer do not support s390x 31-bit compilation"
                    MBITS=
                else
                    MBITS=31
                    if [[ "$LTRACE_RPM" =~ devtoolset-(9|10) ]] ; then
                        rlLogInfo "devtoolset-(9|10)-gcc do not support s390, hence using base gcc"
                        rlRun "GCC=/usr/bin/gcc"
                        rlAssertRpm $(rpm -qf $GCC)
                    fi
                fi
            elif [[ $ARCH =~ ia64|aarch64|ppc64le ]]; then
                rlLogInfo "$ARCH does not support 32-bit compilation"
                MBITS=
            elif rlIsRHEL ">=10"; then
                rlLogInfo "RHEL >=10 does not support 32-bit packages"
                MBITS=
            else
                MBITS=32
            fi
        fi

        rlLogInfo "MBITS=$MBITS"

        rlRun "$GCC -fPIE -pie -x c reproducer.c -o a-native.out"
        rlAssertExists a-native.out

        if [ -n "$MBITS" ]; then
            rlRun "$GCC -fPIE -pie -m$MBITS -x c reproducer.c -o a-$MBITS.out"
            rlAssertExists a-$MBITS.out
        fi
    rlPhaseEnd

    rlPhaseStartTest "Native binary testing"
        rlRun "ltrace ./a-native.out > log 2>&1"
        LIBC_START_MAIN=true
        if [[ "$ARCH" = "x86_64" ]]; then
            if rlIsRHEL '>=8' || rlIsFedora; then
                rlLogInfo "x86_64: Since RHEL-8 __libc_start_main has been optimized into non-PLT call, no longer ltraced (bz#1654734)"
                LIBC_START_MAIN=false
            fi
        fi
        if $LIBC_START_MAIN; then
            rlAssertGrep "__libc_start_main" log
        fi
        rlAssertGrep "alarm(42)" log
        rlAssertGrep "exited (status 0)" log
        rlLog "log file:\n$(cat log)"
    rlPhaseEnd

    if [ -n "$MBITS" ]; then
        rlPhaseStartTest "$MBITS bit binary testing"
            rlRun "ltrace ./a-$MBITS.out > log-$MBITS 2>&1"
            rlAssertGrep "__libc_start_main" log-$MBITS
            rlAssertGrep "alarm(42)" log-$MBITS
            rlAssertGrep "exited (status 0)" log-$MBITS
            rlLog "log file:\n$(cat log-$MBITS)"
        rlPhaseEnd
    fi

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
