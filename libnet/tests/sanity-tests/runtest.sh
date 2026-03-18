#!/bin/bash
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   runtest.sh of libnet
#   Description: Tests for libnet
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
# ~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="libnet"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE

        rlLog "Setting up veth Interface "
        rlRun "ip link add veth-test type veth peer name veth-peer"
        rlRun "ip addr add 192.168.50.5 dev veth-test"
        rlRun "ip addr add 192.168.50.6 dev veth-peer"
        rlRun "ip link set dev veth-test up"
        rlRun "ip link set dev veth-peer up"

        rlRun "cp test-libnet /usr/bin/"
        rlRun "systemctl daemon-reload"
    rlPhaseEnd

    rlPhaseStartTest
        rlLog "Starting libnet tests ..."
        rlRun "/usr/bin/test-libnet"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm /usr/bin/test-libnet"
        rlRun "ip link del veth-test"
        rlLog "libnet tests done"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd

rlGetTestState
