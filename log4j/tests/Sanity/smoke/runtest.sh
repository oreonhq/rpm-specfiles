#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "hello world"
    rlAssertRpm log4j
    java_home=/usr/lib/jvm/java-21-openjdk/bin
    jar=/usr/share/java/jctools/jctools-core.jar
    rlRun "${java_home}/javac -cp /usr/share/java/log4j/log4j-api.jar -d out Smoke.java"
    rlRun -s "${java_home}/java -cp /usr/share/java/log4j/log4j-api.jar:/usr/share/java/log4j/log4j-core.jar:out Smoke 2>&1"
    rlAssertGrep "ERROR Smoke - Hello from Log4J" $rlRun_LOG
    rlAssertGrep "SMOKE TEST COMPLETE" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
