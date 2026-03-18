# SPDX-License-Identifier: GPL-2.0-or-later
VERSION	:=	2.4
$(info "Version: $(VERSION)")

CC	:=	gcc
ifeq ($(CFLAGS),)
CFLAGS	:= 	-O3 -g -Wall -D_GNU_SOURCE \
		-fstack-protector-all -fcf-protection \
		-fstack-clash-protection
endif
CFLAGS  +=	-fPIC -fplugin=annobin
LDFLAGS +=	-Wl,-z,now -Wl,-z,relro -pie

FILES	:=	slub_cpu_partial_off 	\
		rhel-rt.rules 		\
		kernel-is-rt 		\
		realtime-setup.sysconfig 	\
		realtime-setup.systemd 	\
		realtime.conf 		\
		realtime-entsk.service 	\
		realtime-setup.service	\
		realtime-setup.spec

EXT 	:=	bz2
TARBALL	:=	realtime-setup-v$(VERSION).tar.$(EXT)

all:  realtime-entsk

realtime-entsk: enable-netsocket-tstamp-static-key.c
	$(CC) $(CFLAGS) -c enable-netsocket-tstamp-static-key.c
	$(CC) $(LDFLAGS) -o realtime-entsk enable-netsocket-tstamp-static-key.o

clean:
	rm -f *~ *.tar.$(EXT)
	rm -rf rpm
	rm -f realtime-entsk *.o

tarball:
	rm -f *.tar.$(EXT)
	git archive --format=tar --prefix=realtime-setup-v$(VERSION)/ HEAD | \
		bzip2 >realtime-setup-v$(VERSION).tar.$(EXT)

install:
	install -m 755 -D slub_cpu_partial_off $(DEST)/usr/bin/slub_cpu_partial_off
	install -m 644 -D rhel-rt.rules $(DEST)/etc/udev/rules.d/99-rhel-rt.rules
	install -m 755 -D kernel-is-rt $(DEST)/usr/sbin/kernel-is-rt
	install -m 644 -D realtime-setup.sysconfig $(DEST)/etc/sysconfig/realtime-setup
	install -m 755 -D realtime-setup.systemd $(DEST)/usr/bin/realtime-setup
	install -m 644 -D realtime.conf $(DEST)/etc/security/limits.d/realtime.conf
	install -m 644 -D realtime-entsk.service $(DEST)/usr/lib/systemd/system/realtime-entsk.service
	install -m 755 -D -s realtime-entsk $(DEST)/usr/sbin/realtime-entsk
	install -m 644 -D realtime-setup.service $(DEST)/usr/lib/systemd/system/realtime-setup.service
