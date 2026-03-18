#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Description: Test basic functionality of udica
#   Author: Jan Zarsky <jzarsky@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2019 Red Hat, Inc.
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

PACKAGE="udica"

CONTAINERS="fedora:latest fedora:rawhide ubi9 ubi8 ubi7 centos:stream9"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm "udica"
        rlAssertRpm "container-selinux"
        rlAssertRpm "policycoreutils"
        rlAssertRpm "podman"
        OUTPUT_FILE=$(mktemp)
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "udica --help"
        rlRun "PAGER=cat man udica"
    rlPhaseEnd

    for CONTAINER_NAME in ${CONTAINERS} ; do
        rlPhaseStartTest "Test basic scenario for ${CONTAINER_NAME} container"
            rlRun "podman run -dit --name test -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 ${CONTAINER_NAME}"
            rlRun "podman ps | grep test"
            rlRun "ps -efZ | grep bash"
            rlRun "ps -efZ | grep bash | grep container_t"

            rlRun "podman exec test ls /home" 1,2
            rlRun "podman exec test touch /var/spool/test" 1
            rlRun "podman exec test yum install nmap-ncat -y" 0
            rlWatchdog "rlRun \"podman exec test nc -l 53\"" 3

            CONT_ID=$(podman ps | grep test | cut -d ' ' -f 1)
            rlRun "podman inspect $CONT_ID | udica my_container >$OUTPUT_FILE"
            rlRun "podman stop test"
            rlRun "podman rm --force test"

            rlRun "cat $OUTPUT_FILE"
            rlAssertExists "my_container.cil"
            SEMODULE=$(cat $OUTPUT_FILE | grep "semodule -i" | cut -d '#' -f 2)
            rlRun "$SEMODULE"

            PODMAN_OPT=$(cat $OUTPUT_FILE | grep "security-opt" | cut -d '"' -f 2)
            rlRun "podman run -dit --name test2 $PODMAN_OPT -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 fedora"
            rlRun "podman ps | grep test2"
            rlRun "ps -efZ | grep bash"
            rlRun "ps -efZ | grep bash | grep my_container.process"

            rlRun "podman exec test2 ls /home" 0
            rlRun "podman exec test2 touch /var/spool/test" 0
            rlRun "podman exec test2 yum install nmap-ncat -y" 0
            rlWatchdog "rlRun \"podman exec test2 nc -l 53\" 2" 3

            rlRun "podman stop test2"
            rlRun "podman rm --force test2"

            rlRun "semodule -r my_container base_container net_container home_container"
            rlRun "rm my_container.cil"
        rlPhaseEnd
    done

    rlPhaseStartTest "Compare different ways of obtaining policy"
        rlRun "podman run -dit --name test -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 fedora"
        rlRun "podman ps | grep test"

        CONT_ID=$(podman ps | grep test | cut -d ' ' -f 1)
        rlRun "podman inspect $CONT_ID | udica my_container >pipe.result"

        rlRun "podman inspect $CONT_ID >container.json"
        rlRun "udica -j container.json my_container >json.result"

        rlRun "udica -i $CONT_ID my_container >id.result"

        rlRun "diff pipe.result json.result"
        rlRun "diff pipe.result id.result"

        rlRun "rm -f pipe.result json.result id.result container.json"
        rlRun "podman stop test"
        rlRun "podman rm test"
    rlPhaseEnd

    rlPhaseStartTest "Test loading modules"
        rlRun "podman run -dit --name test -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 fedora"
        rlRun "podman ps | grep test"

        CONT_ID=$(podman ps | grep test | cut -d ' ' -f 1)
        rlRun "podman inspect $CONT_ID | udica -l my_container"

        rlRun "podman stop test"
        rlRun "podman rm test"

        rlRun "semodule -l >$OUTPUT_FILE"
        rlAssertGrep "my_container" $OUTPUT_FILE
        rlAssertGrep "base_container" $OUTPUT_FILE
        rlAssertGrep "net_container" $OUTPUT_FILE
        rlAssertGrep "home_container" $OUTPUT_FILE

        rlRun "semodule -r my_container base_container net_container home_container"
        rlRun "rm my_container.cil"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm -f $OUTPUT_FILE"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
