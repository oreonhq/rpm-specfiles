#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/acpica-tools/dump-tables
#   Description: Uses the utilities in acpica-tools to dump the ACPI tables on a system and upload to Beaker.
#   Author: Mike Gahagan <mgahagan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2017 Red Hat, Inc.
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

# Include Beaker environment
. /usr/bin/rhts-environment.sh
. /usr/share/beakerlib/beakerlib.sh
TESTNAME=$(basename $TEST)
OUTPUTDIR=/mnt/testarea/$TESTNAME
log_dir=$OUTPUTDIR/logs
# RHEL uses /usr/bin/acpidump-acpica, Fedora uses /usr/bin/acpidump
#ACPIDUMP_BIN="${ACPIDUMP_BIN:-acpidump-acpica}"
ACPIDUMP_BIN="${ACPIDUMP_BIN:-acpidump}"
PACKAGE="acpica-tools"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        [ $? -eq 0 ] || rlDie "$PACKAGE must be installed!... aborting.."
        rlGetDistroRelease
        rlGetDistroVariant
        rlShowRunningKernel
        rlGetPrimaryArch
        rlGetSecondaryArch
        rlRun "mkdir -p $OUTPUTDIR/{bin,logs,asl,hex}" 0 "Making output directories"
        [ $? -eq 0 ] || rlDie "Cannot make output directories!... aborting.."
	rlLog "Using acpidump binary: $ACPIDUMP_BIN"
    rlPhaseEnd

    rlPhaseStartTest
        pushd $OUTPUTDIR/bin
	    if [[ $ACPIDUMP_BIN = "_sys_firmware" ]] ; then 
          rlLog "Dumping tables from /sys/firmware/acpi/tables..."
          find /sys/firmware/acpi/tables/ -type f | while read f ; do
            name="$(basename $f | tr '[[:upper:]]' '[[:lower:]]').dat"
            cat $f > $name
            done
	    else
          rlRun "$ACPIDUMP_BIN -bz" 0 "Dumping binary ACPI info..."
        fi
        rlRun "acpinames dsdt.dat > ../logs/DSDT-ACPI-namespace.out 2>&1" 0 "Extracting namespace information from DSDT"
        rlLog "Decompiling binary files"
        for f in $(ls *.dat) ; do
          rlRun "iasl -d $f" 0 "Decompiling $f"
        done
        rlRun "mv *.dsl ../asl" 0 "Moving source files to $OUTPUTDIR/asl"
        popd
        if [[ $ACPIDUMP_BIN != "_sys_firmware" ]]; then
          rlRun "$ACPIDUMP_BIN -o $OUTPUTDIR/hex/$HOSTNAME-ACPI-TABLE.hex" 0 "Dumping hex-encoded ACPI info"
        fi
    rlPhaseEnd

    rlPhaseStartCleanup
      rlRun "tar -Jcf $log_dir/$HOSTNAME-ACPI-TABLE-AML.tar.xz $OUTPUTDIR/bin" 0 "Archiving aml files..."
      rlRun "tar -Jcf $log_dir/$HOSTNAME-ACPI-TABLE-ASL.tar.xz $OUTPUTDIR/asl" 0 "Archiving asl files..."
      if [ -f $OUTPUTDIR/hex/$HOSTNAME-ACPI-TABLE.hex ]; then
        rlRun "cp $OUTPUTDIR/hex/$HOSTNAME-ACPI-TABLE.hex $log_dir" 0 "Copying hex-encoded ACPI info to log directory"
      fi
      for f in $log_dir/*; do
        if [ -f $f ] ; then
          rlFileSubmit $f
        fi
      done
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
