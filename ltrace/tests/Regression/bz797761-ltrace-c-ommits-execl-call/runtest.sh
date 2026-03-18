#!/bin/bash
# vim: dict=/usr/share/beakerlib/dictionary.vim cpt=.,w,b,u,t,i,k
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   runtest.sh of /tools/ltrace/Regression/bz797761-ltrace-c-ommits-execl-call
#   Description: The test tries to ltrace an app which uses execl calls.
#   Author: Michael Petlan <mpetlan@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2013 Red Hat, Inc. All rights reserved.
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

PACKAGE="ltrace"

create_reproducer()
{
cat <<EOF > reproducer.c
#include <stdio.h>
#include <unistd.h>
int main ()
{
  execl("/bin/ls","ls",0);
  return 0;
}
EOF
}

rlJournalStart
	rlPhaseStartSetup
		rlAssertRpm $PACKAGE
		rlRun "TmpDir=\$(mktemp -d)" 0 "Creating tmp directory"
		rlRun "pushd $TmpDir"
		create_reproducer
		rlRun "gcc -o reproducer reproducer.c"
	rlPhaseEnd

	rlPhaseStartTest
		# The main purpose of this section is to check if the file ltrace-c.log contains the 'exec' substring.
		rlRun "ltrace ./reproducer 2>&1 >/dev/null | tee ltrace.log"
		rlRun "ltrace -c ./reproducer 2>&1 >/dev/null | tee ltrace-c.log"
		rlAssertGrep "exec" ltrace.log
		rlAssertGrep "exec" ltrace-c.log
	rlPhaseEnd

	rlPhaseStartCleanup
		rlRun "popd"
		rlRun "rm -r $TmpDir" 0 "Removing tmp directory"
	rlPhaseEnd
rlJournalPrintText
rlJournalEnd
