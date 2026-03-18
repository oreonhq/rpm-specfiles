#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "check for presence of antlr command"
    rlAssertRpm antlr-tool
    rlAssertBinaryOrigin antlr antlr-tool
  rlPhaseEnd

  rlPhaseStartTest "display antlr help"
    rlRun -s "antlr --help"
    rlAssertGrep "ANTLR Parser Generator" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
