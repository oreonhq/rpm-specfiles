#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/pthread-program-assertion-failure
#   Description: pthread-program-assertion-failure
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
        rlRun "TMP=\$(mktemp -d)"
        rlRun "pushd $TMP"
        cat > test.c <<EOF
#include <pthread.h>
#include <stdio.h>

extern void print (char *);

#define PRINT_LOOP 10

void *
th_main (void *arg)
{
  int i;
  for (i=0; i<PRINT_LOOP; i++)
    printf (arg);
  return NULL;
}

int
main ()
{
  pthread_t thread1;
  pthread_t thread2;
  pthread_t thread3;
  pthread_create (&thread1, NULL, th_main, "aaa");
  pthread_create (&thread2, NULL, th_main, "bbb");
  pthread_create (&thread3, NULL, th_main, "ccc");
  pthread_join (thread1, NULL);
  pthread_join (thread2, NULL);
  pthread_join (thread3, NULL);
  return 0;
}
EOF
        rlRun "gcc -lpthread test.c"
    rlPhaseEnd

    rlPhaseStartTest
        rlRun "ltrace -L ./a.out"
    rlPhaseEnd

    rlPhaseStartCleanup
        rlRun "popd"
        rlRun "rm -r $TMP"
    rlPhaseEnd
rlJournalPrintText
rlJournalEnd
