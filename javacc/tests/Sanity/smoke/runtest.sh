#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "check for presence of javacc commands"
    rlAssertRpm javacc
    rlAssertBinaryOrigin javacc javacc
    rlAssertBinaryOrigin javacc.sh javacc
    rlAssertBinaryOrigin jjtree javacc
    rlAssertBinaryOrigin jjdoc javacc
  rlPhaseEnd

  rlPhaseStartTest "display javacc version"
    rlRun -s "javacc" 1
    rlAssertGrep "^Java Compiler Compiler Version" $rlRun_LOG
    rlAssertGrep "Parser Generator" $rlRun_LOG
    rlRun -s "javacc.sh" 1
    rlAssertGrep "^Java Compiler Compiler Version" $rlRun_LOG
    rlAssertGrep "Parser Generator" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display jjtree version"
    rlRun -s "jjtree" 1
    rlAssertGrep "^Java Compiler Compiler Version" $rlRun_LOG
    rlAssertGrep "Tree Builder" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display jjdoc version"
    rlRun -s "jjdoc" 1
    rlAssertGrep "^Java Compiler Compiler Version" $rlRun_LOG
    rlAssertGrep "Documentation Generator" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "generate, compile and run a simple parser"
    rlRun -s "javacc smoke.jj"
    rlAssertExists "Smoke.java"
    rlRun -s "javac *.java"
    rlRun -s "java -cp . Smoke '{}'"
    rlAssertNotGrep "." $rlRun_LOG
    rlRun -s "java -cp . Smoke '{{}'" 1
    rlAssertGrep "ParseException" $rlRun_LOG
    rlAssertGrep "EOF" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
