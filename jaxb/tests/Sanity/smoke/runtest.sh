#!/bin/bash
# Author: Marian Koncek <mkoncek@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "compile Smoke.java and run it"
    CLASSPATH+=":$(xmvn-resolve jakarta.activation:jakarta.activation-api)"
    CLASSPATH+=":$(xmvn-resolve jakarta.xml.bind:jakarta.xml.bind-api)"
    CLASSPATH+=":$(xmvn-resolve com.sun.istack:istack-commons-runtime)"
    CLASSPATH+=":$(xmvn-resolve org.glassfish.jaxb:jaxb-runtime)"
    CLASSPATH+=":$(xmvn-resolve org.glassfish.jaxb:jaxb-core)"
    export CLASSPATH
    rlRun "/usr/lib/jvm/java-25-openjdk/bin/javac Smoke.java"
    rlRun "/usr/lib/jvm/java-25-openjdk/bin/java -cp \"${CLASSPATH}:plans\" Smoke"
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
