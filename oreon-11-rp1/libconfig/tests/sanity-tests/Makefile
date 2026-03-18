# SPDX-License-Identifier: LGPL-2.1+
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Makefile of /CoreOS/libconfig
#   Description: Test if libconfig working ok
#   Author: Susant Sahani<susant@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
export TEST=/CoreOS/libconfig
export TESTVERSION=1.0

OBJS =  test-libconfig.c
CFLAG = -Wall -g3
CC = gcc
LIBS = -lconfig -lcmocka

test-libconfig:${OBJ}
	${CC} ${CFLAGS} ${INCLUDES} -o $@ ${OBJS} ${LIBS}

run: test-libconfig
	./runtest.sh
clean:
	-rm -f *~ test-libconfig

.c.o:
	${CC} ${CFLAGS} ${INCLUDES} -c $<

CC = gcc

include /usr/share/rhts/lib/rhts-make.include
$(METADATA): Makefile
        @echo "Owner:           Susant Sahani<susant@redhat.com>" > $(METADATA)
        @echo "Name:            $(TEST)" >> $(METADATA)
        @echo "TestVersion:     $(TESTVERSION)" >> $(METADATA)
        @echo "Path:            $(TEST_DIR)" >> $(METADATA)
        @echo "Description:     Test libconfig works ok" >> $(METADATA)
        @echo "Type:            Sanity" >> $(METADATA)
        @echo "TestTime:        5m" >> $(METADATA)
        @echo "RunFor:          libconfig" >> $(METADATA)
        @echo "Requires:        libconfig libconfig-devel" >> $(METADATA)
        @echo "Priority:        Normal" >> $(METADATA)
        @echo "License:         GPLv2" >> $(METADATA)
        @echo "Confidential:    no" >> $(METADATA)
        @echo "Destructive:     no" >> $(METADATA)
        @echo "Releases:        -Fedora 29" >> $(METADATA)
	rhts-lint $(METADATA)
