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
pushd ./converterSample > /dev/null
sed -e "s/VVVVVVVV/$VERSION/" \
    converterSample.asl.result > converterSample.asl.expected

# see if converterSample.asl compiles as expected
$BINDIR/iasl converterSample.asl > converterSample.asl.actual 2>&1
diff converterSample.asl.actual converterSample.asl.expected >/dev/null 2>&1
RET=$?
popd > /dev/null

if [ $RET -eq 0 ]
then
	echo PASS converterSample
else
	echo FAIL converterSample
fi
exit $RET
