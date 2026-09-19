#!/bin/bash

# Wrapper script for launching fheroes2

BASE=$HOME/.local/share/fheroes2
ZIP=$BASE/h2demo.zip
rc=0

if [ ! -f $ZIP ] ; then
    /usr/share/autodl/AutoDL.py /usr/share/fheroes2/fheroes2.autodlrc
    rc=$?
    if [ $rc -eq 0 -o $rc -eq 2 ] ; then
	unzip -n -L -d $BASE -n $ZIP license.txt readme.txt data/campaign.hs data/h2offer.smk data/heroes2.agg data/standard.hs maps/brokena.mp2
        rc=$?
    fi
fi
[ $rc -eq 0 ] || exit $rc

exec fheroes2.bin
