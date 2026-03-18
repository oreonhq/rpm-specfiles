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

PACKAGE="$(rpm -qf $(which ltrace))"

rlJournalStart
    rlPhaseStartSetup "Gathering information"
        rlAssertRpm $PACKAGE
        rlAssertRpm $(rpm -qf $(which gcc))
        rlShowRunningKernel
    rlPhaseEnd

    rlPhaseStartTest "Running tar inside ltrace"
        rlRun "ltrace -o ltrace-test.log tar" 0 "ltrace is crunching tar"
        rlAssertNotGrep "SIGILL" ltrace-test.log -A1
    rlPhaseEnd

    rlPhaseStartCleanup "Doing clean-up"
        rlBundleLogs "ltrace-outputs" ltrace-test.log
        rlRun "rm -f ltrace-test.log"
    rlPhaseEnd
    rlJournalPrintText
rlJournalEnd
