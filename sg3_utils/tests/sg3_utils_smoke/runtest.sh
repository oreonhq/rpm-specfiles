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

PACKAGES=${PACKAGES:-sg3_utils}

set -o pipefail

# Choose first disk device
choose_device () {
        set -x
        SG_DEVICE=`sg_map -sd -i | grep -m 1 "scsi_debug" | sed 's/\([^ ]\+\) \+\([^ ]\+\).*/\1/'`
        SD_DEVICE=`sg_map -sd -i | grep -m 1 "scsi_debug" | sed 's/\([^ ]\+\) \+\([^ ]\+\).*/\2/'`
        set +x
}

# check utility version
check_version () {
        # <utility> <option> should return name (or "version" string) and some version like N.N
        rlRun "$1 $2 2>&1 | tee output.log" 0 "check version for $1"
        rlAssertGrep "(([vV]ersion( string)?:)|($1)).*\d+\.\d+" output.log "-P"
}

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm --all

        # Choose first scsi_debug disk device
        rlRun "modprobe -v scsi_debug scsi_level=2"
        sleep 1
        choose_device
        if [ "$SD_DEVICE" != "" ]; then
                rlLogInfo "Use scsi_debug block device '$SG_DEVICE $SD_DEVICE' for testing."
        else
                rlDie "scsi_debug init failed. No SCSI block device (e.g. '/dev/sda') found!"
        fi

        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "pushd $TmpDir"
    rlPhaseEnd

    rlPhaseStartTest
        check_version sg_dd -V
        check_version sgm_dd -V
        check_version sgp_dd -V
        check_version sg_emc_trespass -V
        check_version sg_format -V
        check_version sg_get_config -V
        check_version sg_ident -V
        check_version sginfo -v
        check_version sg_inq -V
        check_version sg_logs -V
        check_version sg_luns -V
        check_version sg_map -V
        check_version sg_map26 -V
        check_version sg_modes -V
        check_version sg_opcodes -V
        check_version sg_persist -V
        check_version sg_prevent -V
        check_version sg_raw -V
        check_version sg_rbuf -V
        check_version sg_rdac -V
        check_version sg_read --version
        check_version sg_read_buffer -V
        check_version sg_readcap -V
        check_version sg_read_long -V
        check_version sg_reassign -V
        check_version sg_requests -V
        check_version sg_reset -V
        check_version sg_rmsn -V
        check_version sg_rtpg -V
        check_version sg_safte -V
        check_version sg_sat_identify -V
        check_version sg_sat_set_features -V
        check_version sg_scan -V
        check_version sg_senddiag -V
        check_version sg_ses -V
        check_version sg_start -V
        check_version sg_stpg -V
        check_version sg_sync -V
        check_version sg_test_rwbuf -V
        check_version sg_turs -V
        check_version sg_verify -V
        check_version sg_vpd -V
        check_version sg_write_buffer -V
        check_version sg_write_long -V
        check_version sg_wr_mode -V

        for UTILITY in $(echo "sg_dd sgm_dd sgp_dd") ; do
                rlRun "$UTILITY if=$SD_DEVICE of=test_file bs=512 count=10000 time=1 verbose=1" 0 "$UTILITY default"

                # allow direct I/O for test and restore it back
                set -x
                OLD_DIO=`cat /proc/scsi/sg/allow_dio`
                echo 1 > /proc/scsi/sg/allow_dio
                set +x
                rlRun "$UTILITY if=$SD_DEVICE of=test_file bs=512 count=8192 time=1 verbose=1 dio=1" 0 "$UTILITY direct IO for $SD_DEVICE"
                rlRun "$UTILITY if=$SG_DEVICE of=test_file bs=512 count=8192 time=1 verbose=1 dio=1" 0 "$UTILITY direct IO for $SG_DEVICE"
                set -x
                echo $OLD_DIO > /proc/scsi/sg/allow_dio
                set +x

        done

        rlRun "sginfo -l"
        rlRun "sginfo -a $SD_DEVICE"
        rlRun "sginfo -6 $SD_DEVICE"
        rlRun "sginfo -i $SD_DEVICE"
        rlRun "sginfo -r $SD_DEVICE"
        rlRun "sginfo -s $SD_DEVICE"

        rlRun "sg_inq -v $SD_DEVICE"
        rlRun "sg_inq -i $SD_DEVICE"

        rlRun "sg_luns -d $SD_DEVICE"
        rlRun "sg_luns -v $SD_DEVICE"

        rlRun "sg_map -a"
        rlRun "sg_map -i"
        rlRun "sg_map -scd"
        rlRun "sg_map -sd"
        rlRun "sg_map -sr"
        rlRun "sg_map -st"
        rlRun "sg_map -x"

        rlRun "sg_map26 -v $SD_DEVICE"

        rlRun "sg_modes -a $SD_DEVICE"
        rlRun "sg_modes -f $SD_DEVICE"
        rlRun "sg_modes -l $SD_DEVICE"
        rlRun "sg_modes -6 $SD_DEVICE"
        rlRun "sg_modes -v $SD_DEVICE"

        rlRun "sg_read if=$SD_DEVICE bs=512 count=1MB verbose=1"
        rlRun "sg_read if=$SD_DEVICE bs=512 count=1MB verbose=1 time=1"
        rlRun "sg_read if=$SD_DEVICE bs=512 count=1MB verbose=1 time=2"

        rlRun "sg_scan -a"
        rlRun "sg_scan -i"
        rlRun "sg_scan -n"
        rlRun "sg_scan -x"

        rlRun "sg_sync -v $SD_DEVICE"

        rlRun "sg_verify -vvv $SD_DEVICE" "0,5,9"

        rlRun "sg_vpd -e"
        rlRun "sg_vpd -v $SD_DEVICE"
        rlRun "sg_vpd -i $SD_DEVICE"
        rlRun "sg_vpd -l $SD_DEVICE"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"

        # remove scsi_generic
        rlRun "modprobe -r scsi_debug"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
