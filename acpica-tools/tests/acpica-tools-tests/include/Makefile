# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Makefile of /CoreOS/acpica-tools/acpica-tools-tests/include
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Copyright (c) 2014 Red Hat, Inc.
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

AUTHOR=Mike Gahagan <mgahagan@redhat.com>
DESCRIPTION=This virtual test case provides a common set of functions for numerous test cases.
PACKAGE=acpica-tools

export TEST=/CoreOS/acpica-tools/acpica-tools-tests/include
export TESTVERSION=1.0

FILES=$(METADATA) Makefile PURPOSE *.sh 

.PHONY: all install download clean

run: $(FILES) build

build: $(BUILT_FILES)
	chmod a+x runtest.sh

clean:
	rm -f *~ $(BUILT_FILES) *.rpm

include /usr/share/rhts/lib/rhts-make.include

$(METADATA): Makefile
	@echo "Owner:        $(AUTHOR)"         > $(METADATA)
	@echo "Name:         $(TEST)"           >> $(METADATA)
	@echo "TestVersion:  $(TESTVERSION)"    >> $(METADATA)
	@echo "Path:         $(TEST_DIR)"       >> $(METADATA)
	@echo "Description:  $(DESCRIPTION)"    >> $(METADATA)
	@echo "Type:         Library"           >> $(METADATA)
	@echo "TestTime:     5m"                >> $(METADATA)
	@echo "Priority:     High"              >> $(METADATA)
	@echo "License:      GPLv2"             >> $(METADATA)
	@echo "Confidential: no"                >> $(METADATA)
	@echo "Destructive:  no"                >> $(METADATA)
	@echo "RunFor:       $(PACKAGE)"        >> $(METADATA)
	@echo "Requires:     $(PACKAGE)"        >> $(METADATA)
	@echo "Requires:     @developer-tools"  >> $(METADATA)
	@echo "Requires:     gcc"               >> $(METADATA)
	@echo "Requires:     rpm-build"         >> $(METADATA)
	@echo "Requires:     wget"              >> $(METADATA)
	rhts-lint $(METADATA)
