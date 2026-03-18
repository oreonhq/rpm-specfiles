#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/crond-subtask-abnormal-termination-removes-pid-file-in-error
#   Description: Test for crond subtask abnormal termination removes pid
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

	rlRun "cp ./run-job.sh /tmp/"
	rlRun "chmod +x /tmp/run-job.sh"
	rm -f /tmp/run-job.lock

	rlServiceStop crond
	rlServiceStart crond
	rlRun "crontab -u root ./crontab-job"
	rlRun "sleep 60" 0 "Wait for cron job to run"
    rlPhaseEnd

    rlPhaseStartTest
 	if [ -s /var/run/crond.pid ]; then
		rlPass "Crond pid file exists";
	else
		rlFail "Cront pid file doesn't exists or is empty"
	fi

	# /tmp/run-job.lock contains PPID of my job
	rlRun "kill -SIGTERM $(cat /tmp/run-job.lock)"

	# Cut and pasta! Check file again!
	# We love boiler plate code in our tests!
 	if [ -s /var/run/crond.pid ]; then
		rlPass "Crond pid file exists";
	else
		rlFail "Cront pid file doesn't exists or is empty"
	fi
    rlPhaseEnd

    rlPhaseStartCleanup
	killall sleep
	crontab -u root -r
	rm -f /tmp/run-job.sh
	rm -f /tmp/run-job.lock

	rlServiceStop crond
	rlServiceRestore crond
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
