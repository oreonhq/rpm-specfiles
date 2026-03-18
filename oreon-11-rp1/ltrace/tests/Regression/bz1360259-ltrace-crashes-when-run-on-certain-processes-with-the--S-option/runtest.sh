#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz1360259-ltrace-crashes-when-run-on-certain-processes-with-the--S-option
#   Description: Test for BZ#1360259 (ltrace crashes when run on certain processes with the -S option)
#   Author: Edjunior Machado <emachado@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2018 Red Hat, Inc.
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
PACKAGE="${PACKAGE:-$(rpm -qf --qf='%{name}\n' $BIN)}"

if rlIsRHEL ">=9" || rlIsFedora; then
    PROC_NAME=dbus-broker
    SERVICE_NAME=dbus-broker
elif rlIsRHEL 6; then
    PROC_NAME=dbus-daemon
    SERVICE_NAME=messagebus
else
    PROC_NAME=dbus-daemon
    SERVICE_NAME=dbus
fi

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "pgrep -x $PROC_NAME || service $SERVICE_NAME start" 0 "Checking/starting $SERVICE_NAME"
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "pushd $TmpDir"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "PID='$(pidof -s $PROC_NAME)'"
        # try to ltrace dbus-daemon. If there is a bug (BZ#1360259), it will crash
        rlWatchdog "ltrace -S -p $PID > output.log  2>&1" 30 INT
        rlAssertEquals "ltrace is expected to be terminated by watchdog" 1 "$?"
        rlLog "output.log: $(cat output.log)"
        rlAssertNotGrep "\(Assertion.*failed\|Segmentation fault\)" output.log
        rlAssertEquals "$PROC_NAME is expected to be still running" $PID "$(pidof -s $PROC_NAME)"
        rlFileSubmit output.log
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
        rlRun "service $SERVICE_NAME status --no-pager || service $SERVICE_NAME start" 0 "Checking/starting $SERVICE_NAME"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
