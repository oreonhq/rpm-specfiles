#!/bin/bash
#
#       run the misc tests: we need to do this in a script since
#       these are expected to fail which would normally cause %check
#       to stop.  however, this is expected behavior.  we are running
#       iasl precisely because we expect it to stop when presented with
#       faulty ASL.
#
#       this script assumes it is in the source 'tests' directory at
#       start.
#

PWD=$(pwd)
BINDIR="/usr/bin"
VERSION=$($BINDIR/iasl -v | grep Optimizing | cut -d" " -f5)

# create file to compare against
pushd ./grammar > /dev/null
sed -e "s/VVVVVVVV/$VERSION/" \
    grammar.asl.result > grammar.asl.expected

# see if grammar.asl failed as expected
# NB: the -f option is required so we can see all of the errors
$BINDIR/iasl -f grammar.asl > grammar.asl.actual 2>&1
diff grammar.asl.actual grammar.asl.expected >/dev/null 2>&1
RET=$?
popd > /dev/null

if [ $RET -eq 0 ]
then
	echo PASS grammar
else
	echo FAIL grammar
fi
exit $RET
