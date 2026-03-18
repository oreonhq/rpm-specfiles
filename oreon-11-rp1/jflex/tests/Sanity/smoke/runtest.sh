#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartSetup
    basedir=$PWD
    rlRun "pushd \$(mktemp -d)"
  rlPhaseEnd

  rlPhaseStartTest "check for presence of jflex command"
    rlAssertRpm jflex
    rlAssertBinaryOrigin jflex jflex
  rlPhaseEnd

  rlPhaseStartTest "display jflex version"
    rlRun -s "jflex --version"
    rlAssertGrep "This is JFlex" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "compile and run simple lexer"
    rlRun "cp ${basedir}/SimpleLexer.flex ."
    rlRun "cp ${basedir}/Main.java ."
    rlRun "jflex SimpleLexer.flex"
    rlRun "javac -d out SimpleLexer.java"
    rlRun "javac -d out Main.java"
    rlRun -s "java -cp out Main '6x9 1337+42'"
    rlAssertGrep "^<6><9><1337><42>$" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
