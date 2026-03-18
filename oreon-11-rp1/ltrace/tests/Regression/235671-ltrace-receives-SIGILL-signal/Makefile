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


TOPLEVEL_NAMESPACE=/tools
PACKAGE_NAME=ltrace
RELATIVE_PATH=Regression/235671-ltrace-receives-SIGILL-signal

export TEST=$(TOPLEVEL_NAMESPACE)/$(PACKAGE_NAME)/$(RELATIVE_PATH)
export TESTVERSION=1.0

BUILT_FILES=

FILES=$(METADATA) runtest.sh Makefile PURPOSE

.PHONY: all install download clean

run: $(FILES) build
	./runtest.sh

build: $(BUILT_FILES)
	chmod a+x ./runtest.sh 

clean:
	rm -f *~ $(BUILT_FILES)


include /usr/share/rhts/lib/rhts-make.include


$(METADATA): Makefile
	@touch $(METADATA)
	@echo "Owner:        Michal Nowak <mnowak@redhat.com>" > $(METADATA)
	@echo "Name:         $(TEST)" >> $(METADATA)
	@echo "Path:         $(TEST_DIR)"       >> $(METADATA)
	@echo "TestVersion:  $(TESTVERSION)"    >> $(METADATA)
	@echo "Description:  ltrace receives SIGILL signal and terminates" >> $(METADATA)
	@echo "Bug:          235671" >> $(METADATA)
	@echo "Type:         Regression" >> $(METADATA)
	@echo "TestTime:     5m" >> $(METADATA)
	@echo "RunFor:       $(PACKAGE_NAME)" >> $(METADATA)
	@echo "Requires:     $(PACKAGE_NAME)" >> $(METADATA)
	@echo "License:      GPLv3+" >> $(METADATA)

	rhts-lint $(METADATA)

