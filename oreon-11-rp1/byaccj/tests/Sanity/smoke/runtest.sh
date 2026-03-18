#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "check for presence of byaccj command"
    rlAssertRpm byaccj
    rlAssertBinaryOrigin byaccj byaccj
  rlPhaseEnd

  rlPhaseStartTest "display byaccj usage"
    rlRun -s "byaccj" 1
    rlAssertGrep "^usage:" $rlRun_LOG
    rlAssertGrep "Jclass=className" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "generate, compile and run a simple parser"
    rlRun -s "byaccj -J calc.y"
    rlAssertExists "Parser.java"
    rlAssertExists "ParserVal.java"
    rlRun -s "javac *.java"
    rlAssertExists "Parser.class"
    rlAssertExists "ParserVal.class"
    rlRun -s "java -cp . Parser '(42+10)/8*5'"
    rlAssertGrep "^RESULT is: 30" $rlRun_LOG
    rlRun -s "java -cp . Parser 'boom'" 1
    rlAssertGrep "syntax error" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
