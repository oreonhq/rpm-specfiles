#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/scap-security-guide/Sanity/smoke-test
#   Description: Test calls upstream test suite.
#   Author: Marek Haicman <mhaicman@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2018 Red Hat, Inc. All rights reserved.
#
#   This copyrighted material is made available to anyone wishing
#   to use, modify, copy, or redistribute it subject to the terms
#   and conditions of the GNU General Public License version 2.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE. See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public
#   License along with this program; if not, write to the Free
#   Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
#   Boston, MA 02110-1301, USA.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="scap-security-guide"

rlJournalStart

    rlPhaseStartSetup
        rlImport ControlFlow/Cleanup rpm/snapshot || rlDie "Failed to import libraries"
        rlAssertRpm "$PACKAGE"

        RpmSnapshotCreate
        CleanupRegister "RpmSnapshotRevert"
        rlRun "TmpDir=\$(mktemp -d)" 0
        CleanupRegister "rlRun 'rm -r $TmpDir' 0 'Removing tmp directory'"
        rlRun "pushd $TmpDir"
        CleanupRegister "rlRun 'popd'"

        rlFetchSrcForInstalled $PACKAGE
        rlRun "dnf builddep -y $PACKAGE*"
        SITE_PACKAGES=$(python3 -c 'import sysconfig; print(sysconfig.get_paths()["purelib"])')
        rlRun "pip3 install --target=$SITE_PACKAGES ruamel.yaml yamlpath prometheus-client"
        CleanupRegister "rlRun 'pip3 uninstall -y ruamel.yaml yamlpath prometheus-client'"
        TOPDIR=`rpm --eval %_topdir`
        rlRun "rm -rf ${TOPDIR}/BUILD/${PACKAGE}*" 0-255
        rlRun "rpm -ihv `ls *.rpm`" 0 "Install $PACKAGE source RPM"
    rlPhaseEnd

    rlPhaseStartSetup "Prepare upstream test suite (%prep and %build stages from the spec file)"
        rlRun "rpmbuild -v -bc ${TOPDIR}/SPECS/${PACKAGE}.spec"
        CleanupRegister "rlRun 'rm -rf ${TOPDIR}/BUILD/${PACKAGE}*'"
        CleanupRegister "rlRun 'rm -rf ${TOPDIR}/SPECS/${PACKAGE}*'"
        CleanupRegister "rlRun 'rm -rf ${TOPDIR}/SOURCES/*'"
    rlPhaseEnd

    rlPhaseStartTest "Run upstream test suite"
        BUILD_DIR_PATH="$(find $TOPDIR -name build | grep scap-security-guide)"
        rlRun -s "cmake --build $BUILD_DIR_PATH --target test -- ARGS='--output-on-failure'"
        rv=$?

        # if we got error, submit file with result of particular test for easier debugging
        if [ $rv -ne 0 ]; then
            FILE="${BUILD_DIR_PATH}/Testing/Temporary/LastTest.log"
            rlBundleLogs test_outputs $(readlink -f $FILE)
        fi
    rlPhaseEnd

    rlPhaseStartCleanup
        CleanupDo
    rlPhaseEnd

rlJournalPrintText
rlJournalEnd
