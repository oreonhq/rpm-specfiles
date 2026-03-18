#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartSetup
        rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
        rlRun "pushd $tmp"
        rlAssertRpm "ibus"
        rlAssertRpm "ibus-table"
        rlAssertRpm "ibus-table-chinese"
        rlAssertRpm "ibus-table-chinese-array"
        rlAssertRpm "ibus-table-chinese-cangjie"
        rlAssertRpm "ibus-table-chinese-cantonese"
        rlAssertRpm "ibus-table-chinese-cantonyale"
        rlAssertRpm "ibus-table-chinese-easy"
        rlAssertRpm "ibus-table-chinese-erbi"
        rlAssertRpm "ibus-table-chinese-quick"
        rlAssertRpm "ibus-table-chinese-scj"
        rlAssertRpm "ibus-table-chinese-stroke5"
        rlAssertRpm "ibus-table-chinese-wu"
        rlAssertRpm "ibus-table-chinese-wubi-haifeng"
        rlAssertRpm "ibus-table-chinese-wubi-jidian"
        rlAssertRpm "ibus-table-chinese-yong"
    rlPhaseEnd

    rlPhaseStartTest
        # The -s option and & is important, when using the -d option
        # in this test environment the error “Can't connect to IBus.” occurs.
        rlRun -t -l "ibus-daemon -v -r -s &"
        rlRun "sleep 5" 0 "Give ibus-daemon some time to start properly."
        for name in \
            array30-big \
            array30 \
            cangjie-big \
            cangjie3 \
            cangjie5 \
            cantonese \
            cantonhk \
            cantonyale \
            easy-big \
            erbi-qs \
            erbi \
            jyutping \
            quick-classic \
            quick3 \
            quick5 \
            scj6 \
            stroke5 \
            wu \
            wubi-haifeng86 \
            wubi-jidian86 \
            yong
        do
            rlRun -t -l "/usr/libexec/ibus-engine-table --xml 2>/dev/null | grep '<name>table:${name}</name>'" \
            0 "checking whether 'ibus-engine-table --xml' can list table:${name}:"

            rlRun -t -l "ibus list-engine --name-only | grep 'table:${name}$'" \
                0 "checking whether ibus can list table:${name}:"
        done
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "ibus exit" 0 "Exit ibus"
        rlRun "popd"
        rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
