#!/bin/sh

# customize this where needed
PACKAGE="opal-prd opal-utils"
SERVICE="opal-prd"

# source the test script helpers
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
	rlPhaseStartSetup
		for p in $PACKAGE ; do
			rlAssertRpm $p
		done
		rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
		rlRun "cp * $TmpDir" 0 "Copying test files"
		rlRun "pushd $TmpDir"
	rlPhaseEnd
	rlPhaseStartTest "Smoke, sanity and function tests"
		for i in getscom putscom opal-prd pflash; do
			rlRun "/usr/sbin/$i -h" 0 "It ought show the usage"
		done
		for i in getscom putscom; do
			rlRun "/usr/sbin/$i -v" 0 "It ought show the version"
		done
		rlAssertExists "/usr/lib/systemd/system/opal-prd.service"
		# opal-prd only runs on bare-metal (powernv) machines
		if [ -d /sys/firmware/devicetree/base/ibm,opal/diagnostics ] ; then
			rlServiceStart $SERVICE
			rlRun "systemctl status -l $SERVICE"
			rlServiceStop $SERVICE
		fi
		rlRun "/usr/sbin/opal-gard -p -e -8 -f data1.bin list" 0
		rlRun "/usr/sbin/opal-gard -p -e -8 -f data1.bin show 1" 0
		rlRun "/usr/sbin/opal-gard -p -e -f data-p9.bin --p9 show 1" 0
		rlRun "/usr/sbin/opal-gard -p -e -f blank.bin create $TmpDir/doesnt_exist0" "1-255" "It ought to be failed"
	rlPhaseEnd
	rlPhaseStartCleanup
		rlRun "popd"
		rlRun "rm -fr $TmpDir" 0 "Removing tmp directory"
	rlPhaseEnd
rlJournalPrintText
rlJournalEnd
