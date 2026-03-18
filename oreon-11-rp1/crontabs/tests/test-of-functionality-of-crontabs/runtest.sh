#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/crontabs/Sanity/test-of-functionality-of-crontabs
#   Description: test of functionality of crontabs
#   Author: Petr Sklenar <psklenar@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2011 Red Hat, Inc. All rights reserved.
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

# Include rhts environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="crontabs"
#how long should we wait:
COUNT=5
rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
	user="petr$RANDOM"
        rlRun "rm -rf /tmp/test.createdbypetr /tmp/test.createdbyroot" 0 "Removing tmp directory"
	rlRun "useradd $user"
	rlRun "rlServiceStart crond"
	rlFileBackup /etc/crontab
    rlPhaseEnd

    rlPhaseStartTest
	echo "*  *  *  *  * root echo root >> /tmp/test.createdbyroot" >> /etc/crontab
	rlAssert0 "added first entry into crontab" $?
	echo "*  *  *  *  * $user echo petr >> /tmp/test.createdbypetr" >> /etc/crontab
	rlAssert0 "added second entry into crontab" $?
	#sleep a while
	rlRun "sleep ${COUNT}m" 0 "sleeping for 5m to wait for cron to create files"
    rlPhaseEnd

    rlPhaseStartTest "check content"
	byroot=`grep root /tmp/test.createdbyroot | wc -l`
	bypetr=`grep petr /tmp/test.createdbypetr | wc -l`
	if [ "$byroot" -ge "${COUNT}" ];then
		rlPass "there is $byroot line"
	else
		rlFail "there is $byroot line"
	fi

        if [ "$bypetr" -ge "${COUNT}" ];then
                rlPass "there is $bypetr line"
        else
                rlFail "there is $bypetr line"
        fi
    rlPhaseEnd

   rlPhaseStartTest "check permissions of created files"
	/bin/ls -la /tmp/test.createdbyroot | grep "root root"
	rlAssert0 "permissions are root root" $?
	/bin/ls -la /tmp/test.createdbypetr | grep "$user $user"
	rlAssert0 "permissions are $user $user" $?
   rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm -rf /tmp/test.createdbypetr /tmp/test.createdbyroot" 0 "Removing tmp directory"
	rlRun "userdel -rf $user"
	rlRun "rlServiceRestore crond"
	rlFileRestore
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
