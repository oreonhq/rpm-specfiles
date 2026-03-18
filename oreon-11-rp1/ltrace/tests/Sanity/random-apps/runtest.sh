#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Sanity/random-apps
#   Description: Runs random app which caused strace problems in the past
#   Author: Michal Nowak <mnowak@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2011 Red Hat, Inc. All rights reserved.
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
. /usr/share/beakerlib/beakerlib.sh || exit 1

CMD='ltrace'
BIN=$(which --skip-alias $CMD)
PACKAGE="$(rpm -qf --qf='%{name}\n' $BIN)"
#export MALLOC_PERTURB_=$(($RANDOM % 255 + 1))

rlJournalStart
	rlPhaseStartSetup
		rlAssertRpm $PACKAGE
		rlRun "TmpDir=\`mktemp -d\`" 0 "Creating tmp directory"
		cp *.c $TmpDir
		rlRun "pushd $TmpDir"
	rlPhaseEnd

	touch FAILED PASSED
	PASSED_CNT=0
	FAILED_CNT=0
	ALL_CNT=0
	for test in *.c; do
		RESULT="PASS"
		rlPhaseStartTest "Test ${test}"
			rlRun "gcc $test -o ${test}.bin -lpthread" 0 "Compile $test"
			rlAssertExists "${test}.bin"
			rlRun "ltrace -o ${test}.LOG -f ./${test}.bin" 0 "Run $test under ltrace"
			[ $? -ne 0 ] && RESULT=FAIL

			echo
			cat ${test}.LOG
			echo

			rlAssertNotGrep "\-\-\- SIGKILL" ${test}.LOG
			[ $? -ne 0 ] && RESULT=FAIL
			rlAssertNotGrep "\-\-\- SIGSEGV" ${test}.LOG
			[ $? -ne 0 ] && RESULT=FAIL
			rlAssertNotGrep "\-\-\- SIGILL" ${test}.LOG
			[ $? -ne 0 ] && RESULT=FAIL
			rlAssertNotGrep "\-\-\- SIGTRAP" ${test}.LOG
			[ $? -ne 0 ] && RESULT=FAIL
			rlAssertNotGrep "\-\-\- SIGINT" ${test}.LOG
			[ $? -ne 0 ] && RESULT=FAIL
			if [[ "$RESULT" == "PASS" ]]; then
				let "PASSED_CNT = $PASSED_CNT + 1"
				echo "$test $opt" >> PASSED
			else
				let "FAILED_CNT = $FAILED_CNT + 1"
				echo "$test $opt" >> FAILED
			fi
			let "ALL_CNT = $ALL_CNT + 1"
		rlPhaseEnd
	done

	rlPhaseStartTest
		rlLog "PASSED : $PASSED_CNT of $ALL_CNT"
		cat PASSED
		rlLog "FAILED : $FAILED_CNT of $ALL_CNT"
		cat FAILED
		if [ $FAILED_CNT -eq 0 ]; then
			rlPass "All testcases passed."
		else
			rlFail "There are some errors."
		fi
	rlPhaseEnd

	rlPhaseStartCleanup
		rlRun "tar c *.LOG *.bin PASSED FAILED | gzip > logs.tar.gz"
		rlFileSubmit "logs.tar.gz"
		rlRun "popd"
		rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
	rlPhaseEnd
rlJournalPrintText
rlJournalEnd
