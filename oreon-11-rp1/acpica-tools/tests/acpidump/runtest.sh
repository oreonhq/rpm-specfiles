#!/bin/bash
#
#       simple script to run acpidump and verify we got
#	some output.
#

PWD=$(pwd)
BINDIR="/usr/bin"

# see if acpidump runs
rm -f /tmp/acpi.tables
$BINDIR/acpidump -o /tmp/acpi.tables 2>&1
RET=$?
if [ $RET -ne 0 ]
then
	echo FAIL acpidump
	exit $RET
fi

RET=2
sz=$(ls -s /tmp/acpi.tables | cut -d' ' -f1)
[[ $sz -gt 0 ]] && RET=0
if [ $RET -ne 0 ]
then
	echo FAIL acpidump
	exit $RET
fi

echo PASS acpidump
exit $RET
