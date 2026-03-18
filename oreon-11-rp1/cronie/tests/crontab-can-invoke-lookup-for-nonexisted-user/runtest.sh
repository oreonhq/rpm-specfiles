#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k ft=beakerlib
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/crontab-can-invoke-lookup-for-nonexisted-user
#   Description: Test for Cron does uid lookups for non-existent users
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
declare -ri EXIT_FAILURE=1;
declare -ri EXIT_SUCCESS=0;
declare -r reportAllErrors=no;

function isTrue() {
    local string="$@";
    local oldOpt="shopt -p nocasematch";
    local -i rc=1;

    shopt -s nocasematch;
    [[ -z "$string" ]] && return 1;

    case $string in
         yes) rc=0;;
        true) rc=0;;
         ano) rc=0;;
           1) rc=0;;
          jo) rc=0;;
        yeah) rc=0;;
           y) rc=0;;
           a) rc=0;;
    esac;
    eval $oldOpt;
    return $rc;
}

## Is nice to know when things going wrong
function errorHandler() {
    local code="${?}";
    local lineNO="$1";

    case $code in
        127)
            rlFail "Command not found on line $lineNO"
            ;;
        *)
            isTrue $reportAllErrors && rlFail "Unhandled error $code near line $lineNO";
            ;;
    esac
}


rlJournalStart
    trap 'errorHandler ${LINENO}' ERR;
    rlPhaseStart FAIL "Setup"
        rlAssertRpm $PACKAGE;
        rlRun "rlServiceStop 'crond'"
        echo  > /var/log/cron
        rlRun "rlServiceStart 'crond'"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "sleep 61 | crontab -" &
        sleep 5
        fileName="$(ls /var/spool/cron/ | grep 'tmp' | head -n 1)";
        ls -lah /var/spool/cron/;
        rlRun "[[ -n '$fileName' ]]" 0 "$fileName found";
        rlRun "wait";
        rlRun "grep 'ORPHAN' /var/log/cron | grep '$fileName'" 1 ;
        tail -n 20 /var/log/cron;
    rlPhaseEnd

    rlPhaseStart WARN "Cleanup"
        rlRun "rlServiceRestore 'crond'"
        #avoid systemd failing to start crond due start-limit
        sleep 10
    rlPhaseEnd
    rlJournalPrintText
    trap - ERR;
rlJournalEnd
