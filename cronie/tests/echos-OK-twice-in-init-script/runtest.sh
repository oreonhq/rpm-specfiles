#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/echos-OK-twice-in-init-script
#   Description: Test for echos "OK" twice in init script
#   Author: Martin Cermak <mcermak@redhat.com>
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

PACKAGE="cronie"

function makeUser() {
    local userName="$(tr -dc "[:lower:]" < /dev/urandom | head -c 5 | sed 's/^/qa_/')";
    while getent passwd $userName; do
        userName="$(tr -dc "[:lower:]" < /dev/urandom | head -c 5 | sed 's/^/qa_/')";
    done
    useradd -d $tmpDir $userName;
    echo $userName;
}

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlServiceStop crond
        rlRun "tmpDir=\$(mktemp -d)" 0 "Creating tmp directory";
        testUser="$(makeUser)";
    rlPhaseEnd

    rlPhaseStartTest
        rlRun -s "service crond restart"
        rlAssertNotGrep "FAILED" $rlRun_LOG
    rlPhaseEnd

    if ! rpm -q systemd &>/dev/null; then
        rlPhaseStartTest
            su -l $testUser -c "service crond restart";
            rlAssertEquals "Expected result of call initscript by unprivileged user is 4" $? 4
        rlPhaseEnd
    fi

    rlPhaseStartCleanup
        rm -f $rlRun_LOG
        rm -rf $tmpDir;
        userdel -rf $testUser;
        rlServiceRestore crond
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd

