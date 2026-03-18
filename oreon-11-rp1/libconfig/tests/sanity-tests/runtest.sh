#!/bin/bash
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   runtest.sh of libconfig
#   Description: Tests for libconfig
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
# ~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="libconfig"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "cp test-libconfig /usr/bin/"
        rlRun "cp auth.cfg /var/run/"
    rlPhaseEnd

    rlPhaseStartTest
        rlLog "Starting libconfig tests ..."
        rlRun "/usr/bin/test-libconfig"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm /usr/bin/test-libconfig /var/run/auth.cfg"
        rlLog "libconfig tests done"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd

rlGetTestState
