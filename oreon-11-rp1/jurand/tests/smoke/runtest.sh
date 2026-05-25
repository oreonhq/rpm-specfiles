#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartSetup
    rlAssertRpm jurand
    rlAssertRpm java-21-openjdk-devel
    export JAVA_HOME=/usr/lib/jvm/java-21-openjdk
    rlRun "wget https://src.fedoraproject.org/lookaside/pkgs/guava/guava-31.1.tar.gz/sha512/660b486d82d526ce722130f2968ea8ab9eb53f5915f80e53ef135a7bfcb6ced9b2f2a50ebdb8b316cc48a4f2553fa067a1d6fc0bc4498774a9f1990a535651b8/guava-31.1.tar.gz"
    rlAssertExists guava-31.1.tar.gz
    rlRun "tar xf guava-31.1.tar.gz"
    rlAssertExists guava-31.1
  rlPhaseEnd

  rlPhaseStartTest
    rlRun "jurand -i -a guava-31.1/guava/src\
      -p org[.]checkerframework[.]\
      -p com[.]google[.]common[.]annotations[.]\
      -p com[.]google[.]errorprone[.]annotations[.]\
      -p com[.]google[.]j2objc[.]annotations[.]\
      -p javax[.]annotation[.]\
    "
    rlRun -s "find guava-31.1/guava/src guava-31.1/futures/failureaccess/src -name \*.java | sort"
    rlRun -s "${JAVA_HOME}/bin/javac -d . @$rlRun_LOG"
    rlAssertNotGrep error: $rlRun_LOG
    rlAssertExists com/google/common/base/Strings.class
  rlPhaseEnd

  rlPhaseStartCleanup
    rlRun "rm -rf guava-31.1.tar.gz guava-31.1/ com/"
  rlPhaseEnd
rlJournalEnd
rlJournalPrintText
