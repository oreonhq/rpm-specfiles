#!/bin/bash
# Author: Marian Koncek <mkoncek@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile Smoke.java and run it"
    CLASSPATH+=":$(xmvn-resolve com.sun.xml.fastinfoset:FastInfoset)"
    export CLASSPATH
    rlRun "/usr/lib/jvm/java-21-openjdk/bin/javac Smoke.java"
    rlRun -s "/usr/lib/jvm/java-21-openjdk/bin/java -cp \"${CLASSPATH}:plans\" Smoke"
    rlAssertGrep "com.sun.xml.fastinfoset.stax.StAXDocumentParser" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
