#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz1158713-ltrace-assigns-wrong-names-to-glibc-PLT-slots
#   Description: bz1158713-ltrace-assigns-wrong-names-to-glibc-PLT-slots
#   Author: Martin Cermak <mcermak@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2015 Red Hat, Inc.
#
#   This program is free software: you can redistribute it and/or
#   modify it under the terms of the GNU General Public License as
#   published by the Free Software Foundation, either version 2 of
#   the License, or (at your option) any later version.
#
#   This program is distributed in the hope that it will be
#   useful, but WITHOUT ANY WARRANTY; without even the implied
#   warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
#   PURPOSE.  See the GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see http://www.gnu.org/licenses/.
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Include Beaker environment
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE="$(rpm -qf $(which ltrace))"

rlJournalStart
    rlPhaseStartSetup
        rlAssertRpm $PACKAGE
        rlAssertRpm $(rpm -qf $(which gcc))
        rlRun "TMPD=$(mktemp -d)"
        rlRun "pushd $TMPD"

        cat > test.c <<EOFA
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <pwd.h>
#include <unistd.h>

int main()
{
    char *s = malloc(1000);

    // trigger a free() call from libc:
    setpwent();
    getpwent();
    endpwent();

    // print maps
    sprintf(s, "grep -F '[heap]' /proc/%d/maps", getpid());
    system (s);

    free(s);
}
EOFA

        cat > test.awk <<EOFB
BEGIN {
    addrindex = 0
}

/libc.*free\(0x[0-9a-f]+\)/ {
    match(\$0,/0x[0-9a-f]+/,m)
    addrs[addrindex++] = strtonum(m[0])
}

/\[heap\]/ {
    sub("-", " ", \$0)
    split(\$0, a, " ")
    limit_min = strtonum("0x"a[1])
    limit_max = strtonum("0x"a[2])
}

END {
    for (i=0; i<addrindex; i++) {
        if (addrs[i] < limit_min) {
            print "ERROR 1 ("addrs[i]"<"limit_min")"
            exit 1
        }
        if (addrs[i] > limit_max) {
            print "ERROR 2 ("addrs[i]">"limit_max")"
            exit 2
        }
    }
}
EOFB

        rlRun "gcc test.c -o test"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "ltrace -e free ./test |& tee log | awk -f test.awk" || \
            rlRun "cat log"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TMPD"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
