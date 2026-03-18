#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "check for presence of cup command"
    rlAssertRpm java_cup
    rlAssertBinaryOrigin cup java_cup
  rlPhaseEnd

  rlPhaseStartTest "display cup version"
    rlRun -s "cup -version" 1
    rlAssertGrep "CUP v0" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "generate parser for empty grammar"
    java_home=/usr/lib/jvm/java-21-openjdk/bin
    jar=/usr/share/java/java_cup-runtime.jar
    rlRun -s "cup empty.cup"
    rlAssertGrep "0 errors and 0 warnings" $rlRun_LOG
    rlAssertGrep "2 terminals, 1 non-terminal, and 2 productions declared" $rlRun_LOG
    rlAssertGrep "Code written to" $rlRun_LOG
    rlRun "javac -cp ${jar} parser.java sym.java"
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
