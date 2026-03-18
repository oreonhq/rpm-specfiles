TOPLEVEL_NAMESPACE=/CoreOS
PACKAGE_NAME=opal-prd
RELATIVE_PATH=smoke-functionality

export TEST=$(TOPLEVEL_NAMESPACE)/$(PACKAGE_NAME)/$(RELATIVE_PATH)
export TESTVERSION=1.0

BUILT_FILES=
FILES=$(METADATA) runtest.sh Makefile

.PHONY: all install download clean

run: $(FILES) build
	./runtest.sh

build: $(BUILT_FILES)
	chmod a+x ./runtest.sh

clean:
	rm -f *~ $(BUILT_FILES)

# You may need to add other taregts e.g. to build executables from source code
# Add them here:


# Include Common Makefile
include /usr/share/rhts/lib/rhts-make.include

# Generate the testinfo.desc here:
$(METADATA): Makefile
	@touch $(METADATA)
	@echo "Owner:        Than Ngo <than@redhat.com>" > $(METADATA)
	@echo "Name:         $(TEST)" >> $(METADATA)
	@echo "Path:         $(TEST_DIR)"       >> $(METADATA)
	@echo "TestVersion:  $(TESTVERSION)"    >> $(METADATA)
	@echo "Description:  Basic sanity and function tests">> $(METADATA)
	@echo "Type:         Sanity and function" >> $(METADATA) 
	@echo "TestTime:     5m" >> $(METADATA)
	@echo "RunFor:       $(PACKAGE_NAME)" >> $(METADATA)  # add any other packages for which your test ought to run here
	@echo "Requires:     $(PACKAGE_NAME)" >> $(METADATA)  # add any other requirements for the script to run here
	@echo "Requires:     opal-prd" >> $(METADATA)
	@echo "Requires:     opal-utils" >> $(METADATA)
	@echo "License:      ASL 2.0" >> $(METADATA) 
