# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Makefile of /CoreOS/acpica-tools/acpica-tools-tests/aslts
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Author, maintainer and description of the test
AUTHOR=Mike Gahagan <mgahagan@redhat.com>
DESCRIPTION=ACPICA ASL grammar validation Test Suite (ASLTS)
PACKAGE=acpica-tools

# The name of the test.
export TEST=/CoreOS/acpica-tools/acpica-tools-tests/aslts

# Version of the test. Used with make tag.
export TESTVERSION=1.0


# data files, .c files, scripts anything needed to either compile the test and/or run it.
FILES=$(METADATA) runtest.sh PURPOSE Makefile

run: $(FILES) build
	./runtest.sh

build: $(BUILT_FILES) $(FILES)
	chmod a+x ./runtest.sh

clean:
	rm -f *~ *.rpm
	rm -f $(METADATA)

# Include Common Makefile
include /usr/share/rhts/lib/rhts-make.include

# Generate the testinfo.desc here:
$(METADATA): Makefile
	@touch $(METADATA)
	@echo "Owner:        $(AUTHOR)"     > $(METADATA)
	@echo "Name:         $(TEST)"           >> $(METADATA)
	@echo "Path:         $(TEST_DIR)"       >> $(METADATA)
	@echo "License:      GPLv2"             >> $(METADATA)
	@echo "TestVersion:  $(TESTVERSION)"    >> $(METADATA)
	@echo "Description:  $(DESCRIPTION)"    >> $(METADATA)
	@echo "TestTime:     30m"               >> $(METADATA)
	@echo "RunFor:       $(PACKAGE)"        >> $(METADATA)
	@echo "Architectures:   aarch64 i386 x86_64 ppc64 ppc64le"    >> $(METADATA)
	@echo "Type:         Regression"        >> $(METADATA)
	@echo "RhtsRequires: test(/CoreOS/acpica-tools/acpica-tools-tests/include)" >> $(METADATA)
	@echo "Requires:     $(PACKAGE)"        >> $(METADATA)
	@echo "Requires:     @developer-tools"  >> $(METADATA)
	@echo "Requires:     gcc"               >> $(METADATA)
	@echo "Requires:     rpm-build"         >> $(METADATA)
	@echo "Requires:     wget"              >> $(METADATA)
	rhts-lint $(METADATA)
#	The include package takes care of all the dependencies
#	Add any other dependencies there (/kernel/filesystems/xfs/include)
