#!/bin/bash
. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartSetup
        rlRun "tmp=\$(mktemp -d)" 0 "Create tmp directory"
        rlRun "pushd $tmp"
        rlAssertRpm "ibus"
        rlAssertRpm "ibus-table"
        rlAssertRpm "ibus-table-others"
        rlAssertRpm "ibus-table-code"
        rlAssertRpm "ibus-table-cyrillic"
        rlAssertRpm "ibus-table-latin"
        rlAssertRpm "ibus-table-translit"
        rlAssertRpm "ibus-table-tv"
        rlAssertRpm "ibus-table-mathwriter"
        rlAssertRpm "ibus-table-mongol"
    rlPhaseEnd

    rlPhaseStartTest
        # The -s option and & is important, when using the -d option
        # in this test environment the error “Can't connect to IBus.” occurs.
        rlRun -t -l "ibus-daemon -v -r -s &"
        rlRun "sleep 5" 0 "Give ibus-daemon some time to start properly."
        for name in \
            cns11643 \
            emoticon-table \
            latex \
            rusle \
            rustrad \
            yawerty \
            compose \
            hu-old-hungarian-rovas \
            ipa-x-sampa \
            translit-ua \
            translit \
            telex \
            thai \
            viqr \
            vni \
            mathwriter-ibus \
            mongol_bichig
        do
            rlRun -t -l "/usr/libexec/ibus-engine-table --xml 2>/dev/null | grep '<name>table:${name}</name>'" \
            0 "checking whether 'ibus-engine-table --xml' can list table:${name}:"

            rlRun -t -l "ibus list-engine --name-only | grep 'table:${name}$'" \
                0 "checking whether ibus can list table:${name}:"
        done
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $tmp" 0 "Remove tmp directory"
    rlPhaseEnd
rlJournalEnd
