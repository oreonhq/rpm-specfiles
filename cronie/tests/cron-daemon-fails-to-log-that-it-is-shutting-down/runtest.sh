#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/cron-daemon-fails-to-log-that-it-is-shutting-down
#   Description: Test for cron daemon fails to log that it is shutting down.
#   Author: Robin Hack <rhack@redhat.com>
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

PACKAGE="cronie"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
	rlServiceStop crond
    rlPhaseEnd

    rlPhaseStartTest
    start_time=$(timedatectl | grep "Local time" | awk '{print$4" "$5}')
    rlServiceStart crond
    sleep 20
    rlRun "journalctl --since \"$start_time\" | grep \"(CRON) INFO\"" 0 "cron startup"
	rlServiceStop crond
	# give dbus and cronie some time to shut down...
	sleep 20
    rlRun "journalctl --since \"$start_time\" | grep \"(CRON) INFO (Shutting down)\"" 0 "cron shutdown"
    # DEBUG
    journalctl _COMM=cron --since="$start_time"
    rlPhaseEnd

    rlPhaseStartCleanup
    	rlServiceRestore crond
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
