#!/bin/bash

# Copyright (c) 2016 Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# Author: David Jez <djez@redhat.com>

# Include Beaker environment
. /usr/bin/rhts-environment.sh || exit 1
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGES=${PACKAGES:-lsscsi}
UTILITY=${UTILITY:-lsscsi}

SCSI_HOSTS="3"
SCSI_TARGETS="4"
SCSI_DEVICES="$(($SCSI_HOSTS * $SCSI_TARGETS))"

set -o pipefail

# check utility version
check_version () {
    # <utility> <option> should return name (or "version" string) and some version like N.N
    rlRun "$1 $2 2>&1 | tee output.log" 0 "check version for $1"
    rlAssertGrep "(([vV]ersion( string)?:)|($1)).*\d+\.\d+" output.log "-P"
}

# check for help option
check_help () {
    # --help should return help, that's mean '--help' at least
    rlRun "$UTILITY $2 2>&1 | tee output.log" 0 "check $1 for help"
    rlAssertGrep "\-{2}help" output.log "-P"
    rlAssertGrep "usage:" output.log "-i"
}

# Choose first scsi_debug SCSI host
choose_host () {
        set -x
        SCSI_CHOOSEN_HOST=`lsscsi -H | grep -m 1 scsi_debug | sed -r 's/^[^0-9]*([0-9]+).*$/\1/'`
        set +x
}

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm --all

        # reload scsi_generic module with our configuration hosts x targets
        rlRun "modprobe -r scsi_debug"
        sleep 1
        rlRun "modprobe -v scsi_debug add_host=$SCSI_HOSTS num_tgts=$SCSI_TARGETS"
        sleep 1
        choose_host
        if [ "$SCSI_CHOOSEN_HOST" != "" ]; then
                rlLogInfo "Use scsi_debug SCSI host [$SCSI_CHOOSEN_HOST] for testing."
        else
                rlDie "scsi_debug init failed. No SCSI host found!"
        fi

        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "pushd $TmpDir"
    rlPhaseEnd

    rlPhaseStartTest
        check_version "$UTILITY" "--version"
        check_version "$UTILITY" "-V"

        check_help "$UTILITY" "--help"
        check_help "$UTILITY" "-h"

        rlRun "$UTILITY 2>&1 | tee output.log"
        rlAssertEquals "Count scsi_debug devices" "$SCSI_DEVICES" "$(grep scsi_debug output.log | wc -l)"

        rlRun "$UTILITY -v 2>&1 | tee output.log"
        rlAssertGrep "scsi_debug" "output.log"
        rlAssertGrep "dir" "output.log"

        rlRun "$UTILITY -vvv 2>&1 | tee output.log"
        rlAssertGrep "scsi_debug" "output.log"
        rlAssertGrep "dir" "output.log"

        rlRun "$UTILITY -c 2>&1 | tee output.log"
        rlAssertGrep "scsi_debug" "output.log"
        rlAssertGrep "Host:.*Channel:.*Target:" "output.log" "-P"
        rlAssertGrep "Vendor:.*Model.*Rev:" "output.log" "-P"
        rlAssertGrep "(Type:)|(Revision:)" "output.log" "-P"

        rlRun "$UTILITY -d 2>&1 | tee output.log"
        rlAssertGrep "/dev/.*\[.*\]" "output.log" "-P"

        rlRun "$UTILITY -g 2>&1 | tee output.log"
        rlAssertGrep "/dev/sg" "output.log"

        rlRun "$UTILITY -H 2>&1 | tee output.log"
        rlAssertEquals "Count scsi_debug hosts" "$SCSI_HOSTS" "$(grep scsi_debug output.log | wc -l)"

        rlRun "$UTILITY -l 2>&1 | tee output.log"
        rlAssertGrep "state=" "output.log"

        rlRun "$UTILITY -ll 2>&1 | tee output.log"
        rlAssertGrep "queue" "output.log"

        rlRun "$UTILITY -lll $SCSI_CHOOSEN_HOST:*:* 2>&1 | tee output-lll.log"
        rlAssertNotGrep "=.*=" "output-lll.log" "-P"

        rlRun "$UTILITY -L $SCSI_CHOOSEN_HOST:*:* 2>&1 | tee output.log"
        rlAssertNotDiffer "output-lll.log" "output.log" || rlLogWarning "$(diff -u output-lll.log output.log)"

        rlRun "$UTILITY -dgkv 2>&1 | tee output.log"
        rlAssertGrep "dir" "output.log"
        rlAssertGrep "/dev/.*\[.*\]" "output.log" "-P"
        rlAssertGrep "/dev/sg" "output.log"

        rlRun "$UTILITY -Lptvvv 2>&1 | tee output.log"
        rlAssertGrep "dir" "output.log"
        rlAssertNotGrep "error" "output.log" "-i"
        rlAssertNotGrep "fail" "output.log" "-i"
        rlAssertGrep "transport" "output.log"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"

        # remove scsi_generic
        rlRun "modprobe -r scsi_debug"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
