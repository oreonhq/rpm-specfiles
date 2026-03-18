#!/bin/bash
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   LLDPD integration test
#   Description: Test for lldpd:implementation of IEEE 802.1ab (LLDP)
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
#~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="lldpd"
LldpdPidFile="/var/run/lldpd.pid"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "cp lldpd-tests.py /usr/bin/"
    rlPhaseEnd

    rlPhaseStartTest
        rlLog "lldpd tests"
        rlRun "/usr/bin/python3 /usr/bin/lldpd-tests.py"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm /usr/bin/lldpd-tests.py"
        rlLog "lldpd tests done"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd

rlGetTestState
