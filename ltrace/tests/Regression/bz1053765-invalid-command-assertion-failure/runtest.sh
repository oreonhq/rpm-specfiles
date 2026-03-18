#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz1053765-invalid-command-assertion-failure
#   Description: The test tries to ltrace a non-existing app, ltrace should handle that.
#   Author: Michael Petlan <mpetlan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2014 Red Hat, Inc. All rights reserved.
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

PACKAGE="$(rpm -qf $(which ltrace))"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
    rlPhaseEnd

    rlPhaseStartTest
    	rlRun "{ ltrace blahblahblah0123546213208412321 2> err.log > out.log; } 2> superr.log" 1 "Running ltrace with a non-existing binary."
    	rlAssertNotGrep "Aborted" superr.log
    	rlAssertNotGrep "destroy" err.log
    	rlAssertNotGrep "Assertion" err.log
    	rlAssertNotGrep "assertion" err.log
    	rlAssertNotGrep "relocs" err.log
    	rlAssertNotGrep "failed" err.log
    	echo "==== stderr ===="
    	cat err.log
    	echo "==== stdout ===="
    	cat out.log
    	echo "==== external stderr ===="
    	cat superr.log
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "rm err.log out.log superr.log"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
