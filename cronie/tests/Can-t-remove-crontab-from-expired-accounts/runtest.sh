#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/Can-t-remove-crontab-from-expired-accounts
#   Description: Test for Can't remove crontab from expired accounts
#   Author: Karel Volny <kvolny@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2017 Red Hat, Inc.
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
TestUser="usertest"
ct_file="/var/spool/cron/$TestUser"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "pushd $TmpDir"
        rlRun "useradd $TestUser" 0 "Adding the testing user"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "echo '1 1 1 1 1 nonsense' | crontab -u $TestUser -" 0 "Setting up crontab for the testing user"
        rlRun -s "crontab -u $TestUser -l" 0 "Checking the testing crontab"
        rlAssertGrep "nonsense" $rlRun_LOG
        rlRun "chage -E 1 $TestUser" 0 "Expiring the testing user account"
        rlRun "crontab -u $TestUser -r" 0 "Removing the testing crontab"
        rlAssertNotGrep "not allowed" $rlRun_LOG
        rlRun -s "crontab -u $TestUser -l" 1 "Checking the testing crontab (should not exist)"
        rlAssertGrep "no crontab for $TestUser" $rlRun_LOG
        rlAssertNotGrep "not allowed" $rlRun_LOG
        rlAssertNotExists "$ct_file"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "userdel $TestUser" 0 "Deleting the testing user"
        rlRun "popd"
        rlRun "rm -rf $TmpDir $ct_file" 0 "Removing tmp directory and possible cruft"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
