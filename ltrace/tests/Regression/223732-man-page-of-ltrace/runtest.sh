#!/bin/bash

# Copyright (c) 2008 Red Hat, Inc. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Author: Michal Nowak <mnowak@redhat.com>

# source the test script helpers
. /usr/bin/rhts_environment.sh
. /usr/share/beakerlib/beakerlib.sh || exit 1

PACKAGE=ltrace

rlJournalStart
	rlPhaseStartSetup "Gathering information"
		rlShowPackageVersion $PACKAGE
		rlShowRunningKernel
	rlPhaseEnd

	rlPhaseStartTest "Running tar inside ltrace"
		man ltrace > trace.man
		rlAssertNotGrep "Only ELF32 binaries are supported" trace.man
	rlPhaseEnd

	rlPhaseStartCleanup "Doing clean-up"
		rm -f trace.man
	rlPhaseEnd
	rlJournalPrintText
rlJournalEnd
