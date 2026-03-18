#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  PATH=/usr/lib/jvm/java-21-openjdk/bin:${PATH}

  rlPhaseStartTest "check for presence of modello command"
    rlAssertRpm modello
    rlAssertBinaryOrigin modello modello
  rlPhaseEnd

  rlPhaseStartTest "display modello usage"
    rlRun -s "modello" 1
    rlAssertGrep "Usage: modello" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "generate STAX reader"
    rlRun "modello smoke.mdo java test-src 1.0.0 foo 8"
    rlRun "javac -d test-bin test-src/smoke/*"
    rlAssertExists test-bin/smoke/SomeBean.class
    rlRun "modello smoke.mdo stax-reader test-src 1.0.0 foo 8"
    rlRun "javac -d test-bin -cp test-bin test-src/smoke/io/stax/*"
    rlAssertExists test-bin/smoke/io/stax/SmokeStaxReader.class
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
