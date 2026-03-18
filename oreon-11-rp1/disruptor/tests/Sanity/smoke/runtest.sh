#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "log events"
    rlAssertRpm disruptor
    java_home=/usr/lib/jvm/java-21-openjdk/bin
    jar=/usr/share/java/disruptor.jar
    rlRun "${java_home}/javac -cp ${jar} -d bin Smoke.java"
    rlRun -s "${java_home}/java -cp ${jar}:bin Smoke"
    rlAssertGrep "Event: LongEvent" $rlRun_LOG
    rlAssertGrep "SMOKE TEST COMPLETE" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
