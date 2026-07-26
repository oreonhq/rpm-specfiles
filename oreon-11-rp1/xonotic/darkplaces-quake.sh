#!/bin/bash

# Wrapper script for launching Quake with darkplaces

base=~/.darkplaces
pak=$base/id1/pak0.pak
rc=0

if [ ! -f $pak ] ; then
    /usr/share/autodl/AutoDL.py /usr/share/darkplaces/quake.autodlrc
    rc=$?
    if [ $rc -eq 0 -o $rc -eq 2 ] ; then
        cd $base
        tar zxf quakesw-1.0.6.tar.gz && rm -f quakesw-1.0.6.tar.gz
        rc=$?
    fi
fi

[ $rc -eq 0 ] || exit $rc

exec darkplaces-${0/*darkplaces-quake-/} -quake -basedir $base "$@"
