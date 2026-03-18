#!/bin/bash
# vim: dict+=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
. /usr/share/beakerlib/beakerlib.sh || exit 1

FAILED=0
for dir in annotations annotationsDerived; do
    for xml in /usr/share/unicode/cldr/common/$dir/*.xml; do
        echo xmllint --noout --valid --postvalid $xml
        xmllint --noout --valid --postvalid $xml
        if test $? -ne 0 ; then
            FAILED=1
            break
        fi
    done
    if test $FAILED -ne 0 ; then
        break
    fi
done

rlJournalStart
    rlPhaseStartTest
        rlAssertEquals "lint result" $FAILED 0
    rlPhaseEnd
rlJournalEnd
