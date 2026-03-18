#!/bin/bash
# Author: Marian Koncek <mkoncek@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile Smoke.java and run it"
    CLASSPATH+=":$(xmvn-resolve org.apache.ant:ant)"
    CLASSPATH+=":$(xmvn-resolve jakarta.activation:jakarta.activation-api)"
    CLASSPATH+=":$(xmvn-resolve com.sun.istack:istack-commons-runtime)"
    CLASSPATH+=":$(xmvn-resolve com.sun.istack:istack-commons-tools)"
    export CLASSPATH
    rlRun "/usr/lib/jvm/java-21-openjdk/bin/javac Smoke.java"
    rlRun -s "/usr/lib/jvm/java-21-openjdk/bin/java -cp \"${CLASSPATH}:plans\" Smoke"
    rlAssertGrep "com.sun.istack.tools.ProtectedTask" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
