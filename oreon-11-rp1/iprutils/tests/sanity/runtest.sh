#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/which/Sanity/basic-functionality-test
#   Description: tests basic functionality
#   Author: Than Ngo <than@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2019 Red Hat, Inc.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PACKAGES="iprutils man-db coreutils rpm"
SERVICES="iprdump iprinit iprupdate"

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
	rlPhaseStartSetup
		for p in $PACKAGES ; do
			rlAssertRpm $p
		done
		rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
		rlRun "pushd $TmpDir"
	rlPhaseEnd
	# test the sercives
	rlPhaseStartTest "Services: iprdump, iprinit, iprupdate"
		for s in $SERVICES ; do
			rlServiceStart $s
			rlRun "systemctl status -l $s"
			rlServiceStop $s
		done
	rlPhaseEnd
	rlPhaseStartTest "Smoke, sanity and function tests"
		rlRun "VERSION=\$( rpm -q --qf '%{VERSION}' iprutils )"
		rlRun -s "iprconfig --version" 0 "It ought show the version"
		rlAssertGrep "iprconfig: $VERSION" $rlRun_LOG
		rlRun "iprconfig -c show-config" 0 "Show ipr configuration"
		rlRun "iprconfig -c show-alt-config" 0 "Show alternate ipr configuration information"
		rlRun "iprconfig -c show-ioas" 0 "Show all ipr adapters"
		rlRun "iprconfig -c show-arrays" 0 "Show all ipr arrays"
		# rlRun "iprconfig -c show-battey-info" 0 "Show cache battery information for specified IOA"
		# rlRun "iprconfig -c show-details sda" 0 "Show device details for specified device"
		rlRun "iprconfig -c show-hot-spares" 0 "Show all configured hot spares"
		rlRun "iprconfig -c show-af-disks" 0 "Show  disks formatted for Advanced Function that are not configured in an array or as a hot spare"
		rlRun "iprconfig -c show-all-af-disks" 0 "Show all disks formatted for Advanced Function"
		rlRun "iprconfig -c show-jbod-disks" 0 "Show all disks formatted for JBOD Function"
		rlRun "iprconfig -c show-slots" 0 "Show all disks slots available on the system"
		# iprconfig -c status /dev/sda || echo FAILED $?
		# iprconfig -c alt-status /dev/sda || echo FAILED $?
		# iprconfig -c query-aid-ceate || echo FAILED $?
		# iprconfig -c query-aid-delete || echo FAILED $?
		# iprconfig -c query-hot-spae-ceate || echo FAILED $?
		# iprconfig -c query-hot-spae-delete || echo FAILED $?
		rlRun "iprconfig -c query-raid-consistency-check" 0 "Show all RAID arrays that are candidates for a RAID consistency check"
		rlRun "iprconfig -c query-format-for-jbod" 0 "Show all disks that can be reformatted for JBOD function"
		rlRun "iprconfig -c query-reclaim" 0 "Show all IOAs that may need a reclaim cache storage"
		rlRun "iprconfig -c query-arrays-raid-include" 0 "Show all RAID arrays that can have disks included in them to increase their capacity"
		# iprconfig -c query-devices-aid-include || echo FAILED $?
		# iprconfig -c query-suppoted-aid-levels || echo FAILED $?
		# iprconfig -c query-include-allowed || echo FAILED $?
		# iprconfig -c query-max-devices-in-aay || echo FAILED $?
		# iprconfig -c query-min-devices-in-aay || echo FAILED $?
		# iprconfig -c quey-min-mult-in-aay || echo FAILED $?
		# iprconfig -c quey-supp-stipe-sizes || echo FAILED $?
		# iprconfig -c query-ecommended-stipe-size || echo FAILED $?
		rlRun "iprconfig -c query-recovery-format" 0 "Show all disks that can be formatted for error recovery purposes"
		rlRun "iprconfig -c query-raid-rebuild" 0 "Show all disks in RAID arrays that can be rebuilt"
		rlRun "iprconfig -c query-format-for-raid" 0 "Show all disks that can be formatted such that they can be used in a RAID array or as a hot spare"
		# iprconfig -c query-ucode-level || echo FAILED $?
		# iprconfig -c ssd-report || echo FAILED $?
		rlRun "iprconfig -c show-ucode-levels" 0 "Show  the microcode level that is currently loaded for every device and adapter in the system"
		# iprconfig -c query-format-timeout || echo FAILED $?
		# iprconfig -c query-qdepth || echo FAILED $?
		# iprconfig -c query-tcq-enable || echo FAILED $?
		# iprconfig -c query-log-level || echo FAILED $?
		rlRun "iprconfig -c query-add-device" 0 "Show all empty disk slots that can have a disk concurrently added"
		rlRun "iprconfig -c query-remove-device" 0 "Show  all disk slots which are either empty or have disks in them which can be concurrently removed from the running system"
		# iprconfig -c query-initiator-id || echo FAILED $?
		# iprconfig -c query-bus-speed || echo FAILED $?
		# iprconfig -c query-bus-width || echo FAILED $?
		rlRun "iprconfig -c query-path-status" 0 "Show the current dual path state for the SAS devices attached specified IOA"
		# iprconfig -c query-path-details || echo FAILED $?
		# iprconfig -c query-arrays-raid-migrate || echo FAILED $?
		# iprconfig -c query-devices-raid-migrate || echo FAILED $?
		# iprconfig -c query-raid-levels-raid-migrate || echo FAILED $?
		# iprconfig -c query-stripe-sizes-raid-migrate || echo FAILED $?
		# iprconfig -c query-devices-min-max-raid-migrate || echo FAILED $?
		rlRun "iprconfig -c query-ioas-asymmetric-access" 0 "Show the IOAs that support asymmetric access"
		rlRun "iprconfig -c query-arrays-asymmetric-access" 0 "Show the disk arrays that are candidates for setting their asymmetric access mode to Optimized or Non-Optimized"
		# iprconfig -c query-ioa-asymmetric-access-mode || echo FAILED $?
		# iprconfig -c query-aay-asymmetric-access-mode || echo FAILED $?
		# iprconfig -c query-ioa-caching || echo FAILED $?
		# iprconfig -c query-array-label || echo FAILED $?
		# iprconfig -c query-array-rebuild-rate || echo FAILED $?
		# iprconfig -c query-array-rebuild-verify || echo FAILED $?
		# iprconfig -c query-array || echo FAILED $?
		# iprconfig -c query-device || echo FAILED $?
		# iprconfig -c query-location || echo FAILED $?
		# iprconfig -c query-write-cache-policy || echo FAILED $?
		# iprconfig -c raid-create || echo FAILED $?
		# iprconfig -c raid-delete || echo FAILED $?
		# iprconfig -c raid-include || echo FAILED $?
		# iprconfig -c raid-migrate || echo FAILED $?
		# iprconfig -c format-for-raid || echo FAILED $?
		# iprconfig -c format-for-jbod || echo FAILED $?
		# iprconfig -c recovey-format || echo FAILED $?
		# iprconfig -c hot-spare-create || echo FAILED $?
		# iprconfig -c hot-spare-delete || echo FAILED $?
		# iprconfig -c disrupt-device || echo FAILED $?
		# iprconfig -c reclaim-cache || echo FAILED $?
		# iprconfig -c reclaim-unknown-cache || echo FAILED $?
		# iprconfig -c raid-consistency-check || echo FAILED $?
		# iprconfig -c raid-rebuild || echo FAILED $?
		# iprconfig -c update-ucode || echo FAILED $?
		rlRun "iprconfig -c update-all-ucodes" 0 "Update the microcode of every device with the latest version found in the system"
		# iprconfig -c set-format-timeout || echo FAILED $?
		# iprconfig -c set-qdepth || echo FAILED $?
		# iprconfig -c set-tcq-enable || echo FAILED $?
		# iprconfig -c set-log-level || echo FAILED $?
		# iprconfig -c set-write-cache-policy || echo FAILED $?
		# iprconfig -c identify-disk || echo FAILED $?
		# iprconfig -c identify-slot || echo FAILED $?
		# iprconfig -c remove-disk || echo FAILED $?
		# iprconfig -c remove-slot || echo FAILED $?
		# iprconfig -c add-slot || echo FAILED $?
		# iprconfig -c set-initiator-id || echo FAILED $?
		# iprconfig -c set-bus-speed || echo FAILED $?
		# iprconfig -c set-bus-width || echo FAILED $?
		# iprconfig -c primary || echo FAILED $?
		# iprconfig -c secondary || echo FAILED $?
		rlRun "iprconfig -c set-all-primary" 0 "Set all attached ipr adapters as the preferred primary adapter"
		rlRun "iprconfig -c set-all-secondary" 0 "Set all attached ipr adapters to indicate they are not the preferred primary adapter"
		# iprconfig -c query-ha-mode || echo FAILED $?
		# iprconfig -c set-ha-mode || echo FAILED $?
		# iprconfig -c set-aay-asymmetic-access-mode || echo FAILED $?
		# iprconfig -c set-ioa-asymmetric-access-mode || echo FAILED $?
		# iprconfig -c set-ioa-caching || echo FAILED $?
		# iprconfig -c set-array-rebuild-verify || echo FAILED $?
		# iprconfig -c set-array-rebuild-rate || echo FAILED $?
		# iprconfig -c get-live-dump || echo FAILED $?
		rlRun "iprconfig -c dump" 0 "Display detailed hardware and system information on standard output"

		# should not segfault
		rlRun -s "iprdump --version" 0 "Print iprdump version"
		rlAssertGrep "iprdump: $VERSION" $rlRun_LOG
		rlRun -s "iprinit --version" 0 "Print iprinit version"
		rlAssertGrep "iprinit: $VERSION" $rlRun_LOG
		# iprsos --version
		rlRun -s "iprupdate --version" 0 "Print iprupdate version"
		rlAssertGrep "iprupdate: $VERSION" $rlRun_LOG

		# check man page
		for m in iprconfig iprdbg iprdump iprinit iprsos iprupdate ; do
			rlRun "man -P head $m" 0 "Show the $m man page"
		done

		# check for sane license and readme file
		rlRun "head /usr/share/licenses/iprutils/LICENSE" 0 "Check for license file"
		rlRun "head /usr/share/doc/iprutils/README" 0 "Check for README file"
	rlPhaseEnd
	rlPhaseStartCleanup
		rlRun "popd"
		rlRun "rm -fr $TmpDir" 0 "Removing tmp directory"
	rlPhaseEnd
rlJournalPrintText
rlJournalEnd
