#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile and run surefire tests"
    rlRun -s "xmvn -V -e -B -o compiler:testCompile surefire:test"
    rlAssertGrep "Running ForkTest" $rlRun_LOG
    rlAssertGrep "Tests run: 1, Failures: 0, Errors: 0, Skipped: 0" $rlRun_LOG
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
