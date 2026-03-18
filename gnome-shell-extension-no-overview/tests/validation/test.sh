#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k

# gjs or js115 in mozjs115-devel provides very simple validations.

. /usr/share/beakerlib/beakerlib.sh || exit 1

rlJournalStart
    rlPhaseStartSetup
        rlRun -t "sed -e 's|resource:.*/main.js|./main.js|' /usr/share/gnome-shell/extensions/no-overview@fthx/extension.js > extension.js"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun -t "json-glib-validate /usr/share/gnome-shell/extensions/no-overview@fthx/metadata.json"
        rlRun -t "gjs -m test.js"
    rlPhaseEnd
rlJournalEnd
