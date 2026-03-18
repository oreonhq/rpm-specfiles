# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Makefile of /CoreOS/acpica-tools/dump-tables
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Author, maintainer and description of the test
AUTHOR=Mike Gahagan <mgahagan@redhat.com>
DESCRIPTION=Uses the utilities in acpica-tools to dump the ACPI tables on a system and upload to Beaker.
PACKAGE=acpica-tools

# The name of the test.
export TEST=/CoreOS/acpica-tools/dump-tables

# Version of the test. Used with make tag.
export TESTVERSION=2.0


# data files, .c files, scripts anything needed to either compile the test and/or run it.
FILES=$(METADATA) runtest.sh PURPOSE Makefile

run: $(FILES) build
	./runtest.sh

build: $(BUILT_FILES) $(FILES)
	chmod a+x ./runtest.sh

clean:
	rm -f *~ *.rpm
	rm -f $(METADATA)
	rm -rf /mnt/testarea/dump-tables

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
	@echo "TestTime:     12m"               >> $(METADATA)
	@echo "RunFor:       $(PACKAGE)"        >> $(METADATA)
	@echo "Architectures:   aarch64 i386 x86_64 ppc64 ppc64le"    >> $(METADATA)
	@echo "Type:         Functional"        >> $(METADATA)
	@echo "Requires:     $(PACKAGE)"        >> $(METADATA)
	rhts-lint $(METADATA)
#	The include package takes care of all the dependencies
#	Add any other dependencies there (/kernel/filesystems/xfs/include)
