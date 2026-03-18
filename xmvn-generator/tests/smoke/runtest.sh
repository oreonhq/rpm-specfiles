#!/bin/bash
# Author: Mikolaj Izdebski <mizdebsk@redhat.com>
. /usr/share/beakerlib/beakerlib.sh

rlJournalStart

  rlPhaseStartSetup
    rlAssertRpm xmvn-generator
  rlPhaseEnd

  rlPhaseStartTest
    rlRun -s "rpmbuild -D '%_topdir %{lua:print(posix.getcwd())}' -D '%_sourcedir %{_topdir}' -D '%_builddir %{_topdir}/build' -D '%_srcrpmdir %{_topdir}' -D '%_rpmdir %{_topdir}' -ba testpkg.spec"
    rlAssertGrep "^INSTALL DONE$" $rlRun_LOG
    rpm=noarch/testpkg-1.2.3-1.fc22.noarch.rpm
    rlAssertExists $rpm
    rlRun -s "rpm -qp $rpm --provides"
    rlAssertGrep "^jpms(foo.module)$" $rlRun_LOG
    rlRun "rpm2cpio $rpm | cpio -id"
    rlAssertExists usr/share/java/sub/some.jar
    rlRun "jar xf usr/share/java/sub/some.jar"
    rlAssertExists file.txt
    rlAssertExists META-INF/MANIFEST.MF
    rlAssertGrep "^Automatic-Module-Name: foo.module" META-INF/MANIFEST.MF
    rlAssertGrep "^Rpm-Name: testpkg" META-INF/MANIFEST.MF
    rlAssertGrep "^Rpm-Epoch: 42" META-INF/MANIFEST.MF
    rlAssertGrep "^Rpm-Version: 1.2.3" META-INF/MANIFEST.MF
    rlAssertGrep "^Rpm-Release: 1.fc22" META-INF/MANIFEST.MF
  rlPhaseEnd

rlJournalEnd
rlJournalPrintText
