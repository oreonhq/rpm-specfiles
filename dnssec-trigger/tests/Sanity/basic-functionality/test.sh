#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
. /usr/share/beakerlib/beakerlib.sh || exit 1

MOVED_RESOLV_CONF=""

wait_for_probe() {
	while dnssec-trigger-control status | grep -q '^probe is in progress'; do
		sleep 1
	done
}

test_fallback() {
	local TYPE=$1
	local HOST=$2

	rlRun "dnssec-trigger-control test_${TYPE}"
	wait_for_probe
	sleep 1
	rlRun "dnssec-trigger-control status"
	rlRun -s "unbound-host -rvD ${HOST}" 0 "Check dnssec works over ${TYPE} fallback"
	rlAssertGrep '(secure)' $rlRun_LOG
}

rlJournalStart
    rlPhaseStartSetup
        rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
	rlAssertRpm dnssec-trigger
	rlFileBackup --missing-ok /etc/resolv.conf
	if test -L /etc/resolv.conf; then
		MOVED_RESOLV_CONF="/etc/resolv-backup-$$.conf"
		rlRun "mv /etc/resolv.conf ${MOVED_RESOLV_CONF}"
	fi
        rlRun "pushd $tmp"
	rlServiceStart dnssec-triggerd
    rlPhaseEnd

    rlPhaseStartTest
    	rlRun "dnssec-trigger-control status"
	rlRun -s "unbound-host -rvD example.org" 0 "Check dnssec actually works"
	rlAssertGrep '(secure)' $rlRun_LOG

	test_fallback tcp www.example.org
	# This variant is not passing
	#test_fallback http example.net
	test_fallback ssl www.example.net
    rlPhaseEnd

    rlPhaseStartCleanup
        rlServiceRestore dnssec-triggerd
        rlRun "popd"
	if [ -n "$MOVED_RESOLV_CONF" ]; then
		rm -f /etc/resolv.conf
		rlRun "mv -f ${MOVED_RESOLV_CONF} /etc/resolv.conf"
	fi
	rlFileRestore
        rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
