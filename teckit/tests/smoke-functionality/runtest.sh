#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /CoreOS/teckit/smoke-functionality
#   Description: tests basic functionality
#   Author: Than Ngo <than@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2019 Red Hat, Inc.
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

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="teckit"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
        rlRun "cp -r * $TmpDir"
        rlRun "pushd $TmpDir"
    rlPhaseEnd

    rlPhaseStartTest "test man pages"
        for m in sfconv teckit_compile txtconv ; do
           rlRun "man $m >& /dev/null"
        done
    rlPhaseEnd

    rlPhaseStartTest "compiling Greek mapping (uncompressed)"
        rlRun "teckit_compile SILGreek2004-04-27.map -z -o SILGreek.uncompressed.tec"
        rlAssertNotDiffer SILGreek2004-04-27.uncompressed.tec.orig SILGreek.uncompressed.tec
    rlPhaseEnd

    rlPhaseStartTest "compiling Greek mapping (compressed)"
        rlRun "teckit_compile SILGreek2004-04-27.map -o SILGreek.tec"
    rlPhaseEnd

    rlPhaseStartTest "converting plain-text file to unicode"
        rlRun "txtconv -t SILGreek.tec -i mrk.txt -o mrk.utf8.txt -nfc"
    rlPhaseEnd

    rlPhaseStartTest "converting back to legacy encoding"
        rlRun "txtconv -t SILGreek.tec -r -i mrk.utf8.txt -o mrk.bytes.txt"
        rlAssertNotDiffer mrk.txt mrk.bytes.txt
    rlPhaseEnd

    rlPhaseStartTest "converting unicode to utf16 and nfd"
        rlRun "txtconv -i mrk.utf8.txt -o mrk.utf16be.txt -of utf16be -nfd"
    rlPhaseEnd

    rlPhaseStartTest "converting back to utf8 and nfc"
        rlRun "txtconv -i mrk.utf16be.txt -o mrk.utf8b.txt -of utf8 -nfc"
        rlAssertNotDiffer mrk.utf8.txt mrk.utf8b.txt
    rlPhaseEnd

    rlPhaseStartTest "compiling ISO-8859-1 mapping for sfconv test"
        rlRun "teckit_compile ISO-8859-1.map -o ISO-8859-1.tec"
    rlPhaseEnd

    rlPhaseStartTest "converting standard format file to unicode"
        rlRun "sfconv -8u -c GNT-map.xml -i Mrk-GNT.sf -o mrk.sf.utf8.txt -utf8 -bom"
    rlPhaseEnd

    rlPhaseStartTest "converting back to legacy encodings"
        rlRun "sfconv -u8 -c GNT-map.xml -i mrk.sf.utf8.txt -o mrk.sf.legacy.txt"
    rlPhaseEnd

    rlPhaseStartTest "converting back to legacy encodings"
        rlRun "sfconv -u8 -c GNT-map.xml -i mrk.sf.utf8.txt -o mrk.sf.legacy.txt"
        rlAssertNotDiffer mrk.sf.legacy.txt.orig mrk.sf.legacy.txt
    rlPhaseEnd

    rlPhaseStartCleanup 
        rlRun "popd"
        rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
    rlPhaseEnd
    rlJournalPrintText
rlJournalEnd
