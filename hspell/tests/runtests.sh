#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

NAME=convmv

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm ${NAME}
        rlShowPackageVersion ${NAME}
        rlRun -t -l "VERSION=$(rpm -q ${NAME} --queryformat='%{version}')" 0 "Get VERSION"
        rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
        rlRun "pushd $tmp"
        rlFetchSrcForInstalled "${NAME}"
        rlRun "rpm --define '_topdir $tmp' -i *src.rpm"
        rlRun -t -l "mkdir BUILD" 0 "Creating BUILD directory"
        rlRun -t -l "rpmbuild --noclean --nodeps --define '_topdir $tmp' -bp $tmp/SPECS/*spec"
        if [ -d BUILD/${NAME}-${VERSION}-build ]; then
            rlRun -t -l "pushd BUILD/${NAME}-${VERSION}-build/${NAME}-${VERSION}"
        else
            rlRun -t -l "pushd BUILD/${NAME}-${VERSION}"
        fi
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "set -o pipefail"
        rlRun "echo "Default installation does not have aspell binary so remove its execution""
        rlRun "sed -i 's/he.rws hunspell/hunspell/g' Makefile.in"
        rlRun "./configure"
        rlRun "sed -i '82,84d' test/test1"
        rlRun "make V=1 test"
        rlRun "retval=$?"
        rlRun "echo $retval"
        rlRun "popd" 0
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd

