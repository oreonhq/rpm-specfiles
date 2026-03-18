#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "test concurrent queue"
    rlAssertRpm jctools
    java_home=/usr/lib/jvm/java-21-openjdk/bin
    jar=/usr/share/java/jctools/jctools-core.jar
    rlRun "${java_home}/javac -cp ${jar} -d bin Smoke.java"
    rlRun -s "${java_home}/java -cp ${jar}:bin Smoke"
    rlAssertGrep "Removed 8192" $rlRun_LOG
    rlAssertGrep "SMOKE TEST COMPLETE" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
