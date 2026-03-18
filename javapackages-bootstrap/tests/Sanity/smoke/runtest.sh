#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  PATH="/usr/libexec/javapackages-bootstrap:$PATH"

  rlPhaseStartTest "check for presence of libexec binaries"
    rlAssertRpm javapackages-bootstrap
    rlAssertBinaryOrigin mvn javapackages-bootstrap
    rlAssertBinaryOrigin xmvn javapackages-bootstrap
    rlAssertBinaryOrigin xmvn-install javapackages-bootstrap
    rlAssertBinaryOrigin xmvn-resolve javapackages-bootstrap
    rlAssertBinaryOrigin xmvn-subst javapackages-bootstrap
    rlAssertBinaryOrigin ant javapackages-bootstrap
    rlAssertBinaryOrigin cup javapackages-bootstrap
    rlAssertBinaryOrigin jflex javapackages-bootstrap
  rlPhaseEnd

  rlPhaseStartTest "display mvn version"
    rlRun -s "mvn --version"
    rlAssertGrep "Red Hat XMvn" $rlRun_LOG
    rlAssertGrep "XMvn home: /usr/share/javapackages-bootstrap" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn version"
    rlRun -s "xmvn --version"
    rlAssertGrep "Red Hat XMvn" $rlRun_LOG
    rlAssertGrep "XMvn home: /usr/share/javapackages-bootstrap" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-install help"
    rlRun -s "xmvn-install --help"
    rlAssertGrep "Usage: xmvn-install" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-resolve help"
    rlRun -s "xmvn-resolve --help"
    rlAssertGrep "Usage: xmvn-resolve" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display xmvn-subst help"
    rlRun -s "xmvn-subst --help"
    rlAssertGrep "Usage: xmvn-subst" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display ant version"
    rlRun -s "ant -version"
    rlAssertGrep "Apache Ant(TM) version" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display cup version"
    rlRun -s "cup -version" 1
    rlAssertGrep "CUP v" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "display jflex version"
    rlRun -s "jflex --version"
    rlAssertGrep "This is JFlex" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
