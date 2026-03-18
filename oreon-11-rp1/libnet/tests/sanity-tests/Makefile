# SPDX-License-Identifier: LGPL-2.1+
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#   Makefile of /CoreOS/libnet
#   Description: Sanity
#   Author: Susant Sahani<susant@redhat.com>
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
export TEST=/CoreOS/libnet
export TESTVERSION=1.0

INCLUDES =
OBJS =  test-libnet.c
CFLAG = -Wall -g3
CC = gcc
LIBS = -lnet -lcmocka -lpcap -lpthread

test-libnet:${OBJ}
	${CC} ${CFLAGS} ${INCLUDES} -o $@ ${OBJS} ${LIBS}

run: test-libnet
	./runtest.sh
clean:
	-rm -f *~ test-libnet

.c.o:
	${CC} ${CFLAGS} ${INCLUDES} -c $<

CC = gcc

include /usr/share/rhts/lib/rhts-make.include
$(METADATA): Makefile
        @echo "Owner:           Susant Sahani<susant@redhat.com>" > $(METADATA)
        @echo "Name:            $(TEST)" >> $(METADATA)
        @echo "TestVersion:     $(TESTVERSION)" >> $(METADATA)
        @echo "Path:            $(TEST_DIR)" >> $(METADATA)
        @echo "Description:     Test libnet sanity" >> $(METADATA)
        @echo "Type:            Sanity" >> $(METADATA)
        @echo "TestTime:        5m" >> $(METADATA)
        @echo "RunFor:          libnet" >> $(METADATA)
        @echo "Requires:        libnet libnet-devel" >> $(METADATA)
        @echo "Priority:        Normal" >> $(METADATA)
        @echo "License:         GPLv2" >> $(METADATA)
        @echo "Confidential:    no" >> $(METADATA)
        @echo "Destructive:     no" >> $(METADATA)
        @echo "Releases:        -Fedora 29" >> $(METADATA)
	rhts-lint $(METADATA)
