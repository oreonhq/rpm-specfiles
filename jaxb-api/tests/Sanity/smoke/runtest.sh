#!/bin/bash
# Author: Marian Koncek <mkoncek@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile Smoke.java and run it"
    CLASSPATH+=":$(xmvn-resolve jakarta.xml.bind:jakarta.xml.bind-api)"
    export CLASSPATH
    rlRun "/usr/lib/jvm/java-25-openjdk/bin/javac Smoke.java"
    rlRun -s "/usr/lib/jvm/java-25-openjdk/bin/java -cp \"${CLASSPATH}:plans\" Smoke"
    rlAssertGrep "jakarta.xml.bind.Unmarshaller" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
