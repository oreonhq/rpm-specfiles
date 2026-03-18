#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/cronie/Regression/anacron-segfaults-with-certain-config-data-2
#   Description: try some invalid configs for anacron to check config parser
#   Author: Jakub Prokes <jprokes@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2014 Red Hat, Inc.
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

assertRpms() {
    rlRun "rpm -q $*" 0-$((${#@}-1)) "One of required packages was found";
    RC=$?;
    [[ $RC -lt ${#@} ]] && return 0;
    return $RC;
}

PACKAGES="${PACKAGES:-cronie vixie-cron}"

rlJournalStart
    rlPhaseStartSetup
        assertRpms $PACKAGES
    rlPhaseEnd

    rlPhaseStartTest
        for scenario in ./configs/*; do
            [[ ! -f $scenario ]] && rlFail "$scenario isn't regular file";
            ## File name has 'special' format: scenario-X_Y where X is scenario number and Y is expected
            ## exit code. And of course there must be some issues related to RHEL 5 :-)
            if rlIsRHEL 5; then
                rlRun "anacron -f -u -d -t $(readlink -f $scenario)" 0 "Testing $(basename ${scenario%_[0-9]})";
            else
                if rlRun "anacron -T -t $scenario;" ${scenario##*_} "Verifying $(basename ${scenario%_[0-9]})"; then
                    rlRun "anacron -f -u -d -t $scenario" 0 "Testing $(basename ${scenario%_[0-9]})";
                else
                    [[ $? -eq 139 ]] && cat $scenario;
                fi
           fi
        done
    rlPhaseEnd

    rlPhaseStartCleanup
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
