#!/bin/bash
# Author: Marian Koncek <mkoncek@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile Smoke.java and run it"
    CLASSPATH+=":$(xmvn-resolve jakarta.activation:jakarta.activation-api)"
    export CLASSPATH
    rlRun "/usr/lib/jvm/java-21-openjdk/bin/javac Smoke.java"
    rlRun -s "/usr/lib/jvm/java-21-openjdk/bin/java -cp \"${CLASSPATH}:plans\" Smoke"
    rlAssertGrep "jakarta.activation.MimeType" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
