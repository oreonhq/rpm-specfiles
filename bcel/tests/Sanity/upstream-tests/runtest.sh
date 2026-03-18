#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartSetup
    rlAssertRpm bcel
    rlRun "pushd \$(mktemp -d)"
  rlPhaseEnd

  rlPhaseStartTest "prepare test sources"
    rlFetchSrcForInstalled bcel
    srpm=$(echo bcel-*.src.rpm)
    rlAssertExists ${srpm}
    rlRun "rpm2cpio ${srpm} | cpio -id"
    tarball=$(echo bcel-*.tar.gz)
    rlAssertExists ${tarball}
    rlRun "tar xf ${tarball}"
    basedir=$(echo bcel-*-src)
    rlAssertExists ${basedir}/
    jar=$(find-jar bcel)
    rlAssertExists ${jar}
    rlRun "mkdir ${basedir}/target"
    rlRun "ln -s ${jar} ${basedir}/target/classes"
  rlPhaseEnd

  mvn="mvn -V -B -f ${basedir}"

  rlPhaseStartTest "compile test sources"
    rlRun -s "${mvn} compiler:testCompile"
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "generate test resources"
    rlRun -s "${mvn} resources:testResources"
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
  rlPhaseEnd

  rlPhaseStartTest "run tests"
    rlRun -s "${mvn} surefire:test -Dsurefire.excludes=JdkGenericDumpTestCase,ConstantPoolModuleToStringTestCase,ConstantPoolModuleAccessTestCase,BCELifierTestCase"
    rlAssertGrep "BUILD SUCCESS" $rlRun_LOG
    rlAssertGrep "Failures: 0, Errors: 0" $rlRun_LOG
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
