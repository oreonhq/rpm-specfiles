#!/bin/bash
#
#       simple script to run acpixtract and verify we got
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
	echo FAIL acpixtract-dump
	exit $RET
fi

RET=2
sz=$(ls -s /tmp/acpi.tables | cut -d' ' -f1)
[[ $sz -gt 0 ]] && RET=0
if [ $RET -ne 0 ]
then
	echo FAIL acpixtract-size
	exit $RET
fi

# see if acpixtract runs
$BINDIR/acpixtract -a /tmp/acpi.tables 2>&1
RET=$?
if [ $RET -ne 0 ]
then
	echo FAIL acpixtract-read
	exit $RET
fi

echo PASS acpixtract
exit $RET
