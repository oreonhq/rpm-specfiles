#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Description: Compare udica output between podman and docker
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

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm "udica"
        rlAssertRpm "container-selinux"
        rlAssertRpm "policycoreutils"
        rlAssertRpm "podman"
        rlRun "rpm -qf /usr/bin/docker"
        rlRun "rlServiceStart docker"
        OUTPUT_FILE=$(mktemp)
    rlPhaseEnd

    rlPhaseStartTest
        for BACKEND in podman docker ; do
            rlRun "$BACKEND run -dit --name test -v /home:/home:ro -v /var/spool:/var/spool:rw -p 21:21 fedora"
            rlRun "$BACKEND ps | grep test"
            CONT_ID=$($BACKEND ps | grep test | cut -d ' ' -f 1)
            rlRun "udica -i $CONT_ID my_container"
            rlRun "mv my_container.cil my_cont_$BACKEND.cil"
            rlRun "$BACKEND stop test"
            rlRun "$BACKEND rm test"
        done

        rlRun "sed -i '/capability/d' my_cont_podman.cil"
        rlRun "diff -b -B my_cont_podman.cil my_cont_docker.cil"

        rlRun "rm my_cont_podman.cil my_cont_docker.cil"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm -f $OUTPUT_FILE"
        rlRun "rlServiceRestore docker"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
