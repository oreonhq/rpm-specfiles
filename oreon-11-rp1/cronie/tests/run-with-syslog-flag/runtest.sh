#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/run-with-syslog-flag
#   Description: Test for cronie has a bug when run with syslog flag
#   Author: Jakub Prokes <jprokes@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2016 Red Hat, Inc.
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
declare -r sysConfig="/etc/sysconfig/crond";
declare -r cronJobFile=/etc/cron.d/testjob

rlJournalStart
    rlPhaseStart FAIL "Setup"
        ## nasty hack for journalctl
        export PAGER=""
        rlAssertRpm $PACKAGE
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "pushd $TmpDir"
        rlServiceStart rsyslog
    rlPhaseEnd

    rlPhaseStartTest
        rlFileBackup ${sysConfig};
        crondOpts="$(sed -n '/^\s*CRONDARGS/s/^\s*CRONDARGS\s*=//p' ${sysConfig})";
        rlLog "Old CRONDARGS=\"${crondOpts}\"";
        if echo "$crondOpts" | grep '"'; then
            ## strip trailing quotes
            crondOpts="$(echo "$crondOpts" | sed 's/\(^"\)\|\("$\)//g')";
        fi
        crondOpts="$crondOpts -s -m off";
        rlLog "New CRONDARGS=\"${crondOpts}\"";
        echo "CRONDARGS=\"${crondOpts}\"" > ${sysConfig};
        phrase="$(tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c 32)";
        echo "* * * * * root /bin/echo $phrase" > ${cronJobFile};
        cp /var/log/cron ./oldLog;
        [[ -f ./oldLog ]] || touch ./oldLog;
        rlServiceStop crond;
        sleep 1
        rlServiceStart crond;
        sleep 65;
        rlRun "diff ./oldLog /var/log/cron |grep -v '/bin/echo' \
            | grep '$phrase'" 0 "Output is logged correctly." \
            || rlLog "$(tail -n 5 /var/log/cron)"
    rlPhaseEnd

    rlPhaseStart WARN "Cleanup"
        rlRun "rm ${cronJobFile}";
        rlFileRestore;
        rlRun "rlServiceRestore crond";
        rlServiceRestore rsyslog
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
