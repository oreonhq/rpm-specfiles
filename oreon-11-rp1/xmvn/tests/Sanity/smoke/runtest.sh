#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartTest "check for presence of XMvn commands"
    rlAssertRpm xmvn
    rlAssertRpm xmvn-minimal
    rlAssertRpm xmvn-tools
    rlAssertBinaryOrigin xmvn xmvn-minimal
    rlAssertBinaryOrigin xmvn-install xmvn-tools
    rlAssertBinaryOrigin xmvn-resolve xmvn-tools
    rlAssertBinaryOrigin xmvn-subst xmvn-tools
  rlPhaseEnd

  rlPhaseStartTest "display xmvn version"
    rlRun -s "xmvn --version"
    rlAssertGrep "^Apache Maven " $rlRun_LOG
    rlAssertGrep "^Maven home: " $rlRun_LOG
    rlAssertGrep "^Java version:" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn help"
    rlRun -s "xmvn --help"
    rlAssertGrep "Comma-delimited list of" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-install help"
    rlRun -s "xmvn-install --help"
    rlAssertGrep "^xmvn-install: Install artifacts" $rlRun_LOG
    rlAssertGrep "^Usage: xmvn-install" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-resolve help"
    rlRun -s "xmvn-resolve --help"
    rlAssertGrep "^xmvn-resolve: Resolve artifacts from system repository" $rlRun_LOG
    rlAssertGrep "^Usage: xmvn-resolve" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-subst help"
    rlRun -s "xmvn-subst --help"
    rlAssertGrep "^xmvn-subst: Substitute artifact files with symbolic links" $rlRun_LOG
    rlAssertGrep "^Usage: xmvn-subst" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "resolve local artifact"
    rlRun "rm -rf $HOME/.m2/repository/junit/junit/4.12/"
    rlAssertNotExists $HOME/.m2/repository/junit/junit/4.12/junit-4.12.jar
    rlRun -s "xmvn -Dxmvn.debug=1 -B dependency:get -Dartifact=junit:junit:4.12"
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
    rlAssertGrep "Resolving junit:junit:jar:4.12 with transitive dependencies" $rlRun_LOG
    rlAssertGrep "Trying to resolve artifact junit:junit:jar:4.12" $rlRun_LOG
    rlAssertGrep "Artifact junit:junit:jar:4.12 was resolved to /usr/share/java/" $rlRun_LOG
    rlAssertNotExists $HOME/.m2/repository/junit/junit/4.12/junit-4.12.jar
  rlPhaseEnd

  rlPhaseStartTest "download remote artifact"
    rlRun "rm -rf $HOME/.m2/repository/turbine/turbine/2.1/"
    rlAssertNotExists $HOME/.m2/repository/turbine/turbine/2.1/turbine-2.1.jar
    rlRun -s "xmvn -Dxmvn.debug=1 -B dependency:get -Dartifact=turbine:turbine:2.1"
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
    rlAssertGrep "Resolving turbine:turbine:jar:2.1 with transitive dependencies" $rlRun_LOG
    rlAssertGrep "Trying to resolve artifact turbine:turbine:jar:2.1" $rlRun_LOG
    rlAssertGrep "Failed to resolve artifact: turbine:turbine:jar:2.1" $rlRun_LOG
    rlAssertExists $HOME/.m2/repository/turbine/turbine/2.1/turbine-2.1.jar
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
