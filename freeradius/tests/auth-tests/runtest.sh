#!/bin/bash
# SPDX-License-Identifier: LGPL-2.1+
# ~~~
#   runtest.sh of freeradius
#   Description:  RADIUS server
#
#   Author: Susant Sahani <susant@redhat.com>
#   Copyright (c) 2018 Red Hat, Inc.
# ~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="freeradius"

RADIUS_CLIENT_CONF="/etc/raddb/clients.conf"
RADIUD_PALIN_TEXT_AUTH_FILE="/etc/raddb/mods-config/files/authorize"

generate_cert(){
    pushd /etc/raddb/certs/
    #remove certificates if exists;generate new certificates
    if [[ -f /etc/raddb/certs/bootstrap ]]; then
        rlLog "Destroy and create new default certificates via bootstrap script"
        rm -f *.pem *.der *.csr *.crt *.key *.p12 serial* index.txt* dh
        rlRun "sh /etc/raddb/certs/bootstrap" 0 "Gnenerating certificates"
    else
        rlLogWarning "!!! WARNING bootsrap file does not exist !!!"
        rlLog "Destroy and create new default certificates via make scripts"
        make destroycerts -C /etc/raddb/certs/
        #create new certificates
        make -C /etc/raddb/certs/
        chown root:radiusd dh ca.* client.* server.*
        chmod 640 dh ca.* client.* server.*
    fi
    popd
}

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "systemctl stop firewalld" 0,5
        rlRun "systemctl stop radiusd.service"
        rlRun "setenforce 0"
        rlFileBackup "$RADIUS_CLIENT_CONF"
        rlFileBackup "$RADIUD_PALIN_TEXT_AUTH_FILE"

        rlRun "cp freeradius-tests.py /usr/bin/"
        rlRun "cp clients.conf $RADIUS_CLIENT_CONF"
        rlRun "cp authorize $RADIUD_PALIN_TEXT_AUTH_FILE"
        rlRun "systemctl daemon-reload"
        generate_cert
    rlPhaseEnd

    rlPhaseStartTest
        rlLog "Starting radius auth tests ..."
        rlRun "/usr/bin/python3 /usr/bin/freeradius-tests.py"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm /usr/bin/freeradius-tests.py"
        rlRun "systemctl start firewalld" 0,5
        rlRun "setenforce 1"
        rlFileRestore
        rlLog "freeradius tests done"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd

rlGetTestState
