#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Sanity/testsuite
#   Description: upstream tests for ltrace
#   Author: Martin Cermak <mcermak@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2015 Red Hat, Inc.
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

CMD='ltrace'
BIN=$(which --skip-alias $CMD)
PACKAGE="${PACKAGE:-$(rpm -qf $BIN)}"
export PACKAGE

GCC=${GCC:-gcc}
export GCC

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun -l "rpm -qf $(which $GCC)" 0 "Checking gcc rpm version"
        rlRun "NVR=$(rpm -q --qf='%{NAME}-%{VERSION}-%{RELEASE}' $PACKAGE)"
        rlRun "TMP=`mktemp -d`"
        rlRun "pushd $TMP"

        set -x
        dnf download --disablerepo='*' --enablerepo=test-artifacts --source $NVR || \
            cp /var/share/test-artifacts/$NVR.src.rpm . || \
            rlFetchSrcForInstalled ltrace
        set +x

        rlRun "dnf builddep -y $NVR.src.rpm"
        rlRun "rpm --define='_topdir $TMP' -Uvh $NVR.src.rpm"
        rlRun "${RPMBUILD_GCC:+CC=$RPMBUILD_GCC} rpmbuild --define='_topdir $TMP' -bc SPECS/${CMD}.spec"

        MAKEFILE_PATH=$(ls BUILD/${CMD}-*/Makefile 2>/dev/null)
        if [[ -z "$MAKEFILE_PATH" ]]; then
            MAKEFILE_PATH=$(ls BUILD/${CMD}-*/${CMD}-*/Makefile 2>/dev/null)
        fi
        rlLogInfo "MAKEFILE_PATH=$MAKEFILE_PATH"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "pushd ${MAKEFILE_PATH%/Makefile}"

        # known issues to be ignored
        ignore_list=''
        rlRun "ignore_list+=' system_calls.exp'" 0 "Failure reported bz#1963110"

        # define --ignore parameter for 'make check' if there is any testcase to be ignored
        [ -n "$ignore_list" ] && rlRun "ignore_param=\"--ignore '$ignore_list'\"" 0 "Ignored testcases that will not be run: $ignore_list"

        # test
        set -o pipefail
        rlRun "make check RUNTESTFLAGS=\"--tool_exec=$BIN CC_FOR_TARGET=$GCC $ignore_param\" |& tee $TMP/check.log"
        rlRun "popd"

        # no unexpected results should appear
        rlRun -l "grep '^FAIL:' check.log" 1
        rlRun -l "grep '^# of unexpected' check.log" 1

        rlFileSubmit "$TMP/check.log" "$PACKAGE-check.log"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TMP"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
