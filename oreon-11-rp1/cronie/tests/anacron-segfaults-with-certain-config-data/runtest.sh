#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/anacron-segfaults-with-certain-config-data
#   Description: Test for anacron segfaults with certain config data
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
    rlPhaseStartSetup "Set anacron"
        rlAssertRpm $PACKAGE
	TESTDIR="${PWD}"

	rlFileBackup "/etc/anacrontab"

	rlRun "echo 'START_HOURS_RANGE=0' > /etc/anacrontab"

	# Prepare coredump handler
	rlServiceStop crond
	rlRun "chmod +x ${TESTDIR}/core.sh"

	rlRun "cat /proc/sys/kernel/core_pattern > /tmp/core_pattern"
	rlRun "echo \"|${TESTDIR}/core.sh %e\" > /proc/sys/kernel/core_pattern"
    rlPhaseEnd

    rlPhaseStartTest
    	rlRun "anacron"

	rlRun "sleep 2" 0 "Wait for kernel"

	# Anacron segfaults
	rlAssertNotExists "/tmp/core.lock"
	if [ -s "/tmp/core.lock" ]; then
		rlAssertNotGrep "anacron" "/tmp/core.lock"
	fi
    rlPhaseEnd

    rlPhaseStartCleanup
	rlRun "cat /tmp/core_pattern > /proc/sys/kernel/core_pattern"

	rm -f /tmp/core.lock
	rm -f /tmp/core_pattern
	killall anacron

    	rlFileRestore
	rlServiceRestore crond
	#avoid systemd failing to start crond due start-limit
	sleep 10
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
