#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k

basedir=$(pwd)

. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartTest
        qs="テスト"
        rlRun "echo $qs | nkf -W -e | nkf -w -E | tee output" 0 "Check nkf functionality"
	rlAssertGrep "$qs" "output"
    rlPhaseEnd
rlJournalEnd
