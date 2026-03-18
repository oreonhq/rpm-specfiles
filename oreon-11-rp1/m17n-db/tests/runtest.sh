#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

NAME=m17n-db

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm ${NAME}
        rlAssertRpm ${NAME}-devel
        rlAssertRpm glibc-locale-source
        rlShowPackageVersion ${NAME}
        rlRun -t -l "VERSION=$(rpm -q ${NAME} --queryformat='%{version}')" 0 "Get VERSION"
        FEDORA_VERSION=$(rlGetDistroRelease)
        rlLog "FEDORA_VERSION=${DISTRO_RELEASE}"
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
        rlRun "set -o pipefail"
        rlRun -t -l "./bootstrap.sh"
        rlRun -t -l "./configure --prefix=/usr"
        rlRun -t -l "make check"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun -t -l "INSTALLED_VERSION=$(m17n-db --version)" \
              0 "Get installed version"
        rlAssertEquals "versions should be equal" "${VERSION}" "${INSTALLED_VERSION}"
        rlGetTestState
        rlLog "Number of failed asserts so far: ${ECODE}"
        rlRun -t -l "DIRECTORY=$(m17n-db)" \
              0 "Get m17n directory"
        rlAssertEquals "m17n directory should be /usr/share/m17n" "${DIRECTORY}" "/usr/share/m17n"
        rlGetTestState
        rlLog "Number of failed asserts so far: ${ECODE}"
        for mim_file in $(ls /usr/share/m17n/*.mim)
        do
            rlAssertGrep "(input-method" ${mim_file}
            rlGetTestState
            rlLog "Number of failed asserts so far: ${ECODE}"
        done
        rlGetTestState
        rlLog "Total number of failed asserts: ${ECODE}"
        rlRun "popd" 0
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
