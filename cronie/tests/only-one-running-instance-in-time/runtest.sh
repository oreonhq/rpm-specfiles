#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/only-one-running-instance-in-time
#   Description: When crond is running in multiple instance, then cron jobs are executed multiple times. Is neccesary to prevent multiple instances of crond running in time.
#   Author: Jakub Prokes <jprokes@redhat.com>
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

PACKAGE="cronie"

rlJournalStart
    rlPhaseStartSetup
        rlServiceStart crond
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "kill -0 $(cat /var/run/crond.pid)" 0 "Service crond is running";
        rlRun "/usr/sbin/crond" 1 "Executing another instance fail";
        rlAssertEquals "There is stil one instance of crond" $(ps h -C crond -o pid | wc -l) 1;
    rlPhaseEnd

    rlPhaseStartCleanup
        rlServiceRestore crond
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
