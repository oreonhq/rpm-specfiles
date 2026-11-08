# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 529634c40910895a9a1f3c5c1e65da2ca9ed72fb158dfc4bcc89efdf05e39b72

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
Summary: Tracks and displays system calls associated with a running process
Name: strace
Version:        7.3
Release:        1%{?dist}
# The test suite is GPLv2+, the bundled headers are GPLv2 with Linux syscall
# exception, all the rest is LGPLv2.1+.
# BSD-2-Clause:
#   bundled/linux/include/uapi/linux/tee.h
# BSD-3-Clause:
#   bundled/linux/include/uapi/linux/quota.h
# GPL-1.0-or-later WITH Linux-syscall-note:
#   bundled/linux/include/uapi/linux/if_bonding.h
#   bundled/linux/include/uapi/linux/loop.h
# GPL-2.0-or-later WITH Linux-syscall-note:
#   bundled/linux/include/uapi/linux/dm-ioctl.h
#   bundled/linux/include/uapi/linux/hiddev.h
#   bundled/linux/include/uapi/linux/if_alg.h
#   bundled/linux/include/uapi/linux/if_bridge.h
#   bundled/linux/include/uapi/linux/in6.h
#   bundled/linux/include/uapi/linux/in.h
#   bundled/linux/include/uapi/linux/keyctl.h
#   bundled/linux/include/uapi/linux/mptcp.h
#   bundled/linux/include/uapi/linux/ptp_clock.h
#   bundled/linux/include/uapi/linux/tcp.h
#   bundled/linux/include/uapi/mtd/mtd-abi.h
#   bundled/linux/include/uapi/mtd/ubi-user.h
# LGPL-2.0-or-later WITH Linux-syscall-note:
#   bundled/linux/include/uapi/linux/dm-ioctl.h
# LGPL-2.1-or-later WITH Linux-syscall-note:
#   bundled/linux/include/uapi/linux/dqblk_xfs.h
#   bundled/linux/include/uapi/linux/mqueue.h
# (GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB:
#   bundled/linux/include/uapi/linux/tls.h
#   bundled/linux/include/uapi/rdma/ib_user_verbs.h
# (GPL-2.0-only WITH Linux-syscall-note) OR MIT:
#   bundled/linux/include/uapi/linux/io_uring.h
# (GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause:
#   bundled/linux/include/uapi/linux/v4l2-common.h
#   bundled/linux/include/uapi/linux/v4l2-controls.h
#   bundled/linux/include/uapi/linux/videodev2.h
# GPL-2.0-only WITH Linux-syscall-note:
#   bundled/linux/include/uapi/asm-generic/hugetlb_encode.h (no explicit license in the file)
#   bundled/linux/include/uapi/linux/mount.h (no explicit license in the file)
#   bundled/linux/include/uapi/linux/netfilter/nfnetlink_osf.h (no explicit license in the file)
#   bundled/linux/include/uapi/linux/version.h (no explicit license in the file)
#   bundled/linux/include/uapi/asm/hugetlb_encode.h (no explicit license in the file)
#   the rest of bundled/linux
# ISC:
#   bundled/linux/include/uapi/linux/nfc.h
# X11:
#   build-aux/install-sh (dist only)
# LGPL-2.1-or-later:
#   build-aux/copyright-year-gen
#   build-aux/file-date-gen
#   m4/ax_code_coverage.m4
#   m4/mpers.m4
#   m4/st_demangle.m4
#   m4/st_esyscmd_s.m4
#   m4/st_libdw.m4
#   m4/st_libunwind.m4
#   m4/st_save_restore_var.m4
#   m4/st_selinux.m4
#   m4/st_stacktrace.m4
#   m4/st_warn_cflags.m4
# GPL-2.0-or-later:
#   build-aux/ar-lib (dist only)
#   build-aux/compile (dist only)
#   build-aux/depcomp (dist only)
#   build-aux/missing (dist only)
#   build-aux/test-driver (dist only)
# GPL-3.0-or-later:
#   build-aux/config.guess (dist only)
#   build-aux/config.sub (dist only)
#   build-aux/git-version-gen
# FSFAP:
#   README-configure
#   m4/ax_prog_cc_for_build.m4
#   m4/ax_valgrind_check.m4
# FSFUL:
#   configure (dist only)
# FSFULLR:
#   m4/warnings.m4
# FSFULLRWD:
#   aclocal.m4 (dist only)
#   Makefile.in (dist only)
#   bundled/Makefile.in (dist only)
#   src/Makefile.in (dist only)
#   tests/Makefile.in (dist only)
#   tests-m32/Makefile.in (dist only)
#   tests-mx32/Makefile.in (dist only)
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-3.0-or-later AND BSD-2-Clause AND BSD-3-Clause AND (GPL-1.0-or-later WITH Linux-syscall-note) AND (GPL-2.0-or-later WITH Linux-syscall-note) AND (GPL-2.0-only WITH Linux-syscall-note) AND (LGPL-2.0-or-later WITH Linux-syscall-note) AND (LGPL-2.1-or-later WITH Linux-syscall-note) AND ((GPL-2.0-only WITH Linux-syscall-note) OR Linux-OpenIB) AND ((GPL-2.0-only WITH Linux-syscall-note) OR MIT) AND ((GPL-2.0-or-later WITH Linux-syscall-note) OR BSD-3-Clause) AND ISC AND X11 AND FSFAP AND FSFUL AND FSFULLR AND FSFULLRWD
# Some distros require Group tag to be present,
# some require Group tag to be absent,
# some do not care about Group tag at all,
# and we have to cater for all of them.
URL: https://strace.io
Source0:        https://strace.io/files/%{version}/strace-%{version}.tar.xz
BuildRequires: xz
BuildRequires: gcc gzip make

# Install Bluetooth headers for AF_BLUETOOTH sockets decoding.
BuildRequires: pkgconfig(bluez)
BuildRequires:  oreon-rpm-macros

# Install elfutils-devel or libdw-devel to enable strace -k option.
# Install binutils-devel to enable symbol demangling.
%define buildrequires_stacktrace BuildRequires: elfutils-devel binutils-devel
%define buildrequires_selinux BuildRequires: libselinux-devel
%{?buildrequires_stacktrace}
%{?buildrequires_selinux}

# rhbz#2461721
Recommends: yama-ptrace-enable

# OBS compatibility
%{?!buildroot:BuildRoot: %_tmppath/buildroot-%name-%version-%release}
%define maybe_use_defattr %{nil}

# Fallback definitions for make_build/make_install macros
%{?!__make:       %global __make %_bindir/make}
%{?!__install:    %global __install %_bindir/install}
%{?!make_build:   %global make_build %__make %{?_smp_mflags}}
%{?!make_install: %global make_install %__make install DESTDIR="%{?buildroot}" INSTALL="%__install -p"}

%description
The strace program intercepts and records the system calls called and
received by a running process.  Strace can print a record of each
system call, its arguments and its return value.  Strace is useful for
diagnosing problems and debugging, as well as for instructional
purposes.

Install strace if you need a tool to track the system calls made and
received by a process.

%prep
%oreon_sha256

%setup -q
echo -n %version-%release > .tarball-version
echo -n 2026 > .year
echo -n 2026-06-25 > doc/.strace.1.in.date
echo -n 2025-07-02 > doc/.strace-log-merge.1.in.date

%build
echo 'BEGIN OF BUILD ENVIRONMENT INFORMATION'
uname -a |head -1
libc="$(ldd /bin/sh |sed -n 's|^[^/]*\(/[^ ]*/libc\.so[^ ]*\).*|\1|p' |head -1)"
$libc |head -1
file -L /bin/sh
gcc --version |head -1
ld --version |head -1
kver="$(printf '%%s\n%%s\n' '#include <linux/version.h>' 'LINUX_VERSION_CODE' | gcc -E -P -)"
printf 'kernel-headers %%s.%%s.%%s\n' $((kver/65536)) $((kver/256%%256)) $((kver%%256))
echo 'END OF BUILD ENVIRONMENT INFORMATION'

CFLAGS_FOR_BUILD="$RPM_OPT_FLAGS"; export CFLAGS_FOR_BUILD
%configure --enable-mpers=check --enable-bundled=yes
%make_build

%install
%make_install

# some say uncompressed changelog files are too big
for f in ChangeLog ChangeLog-CVS; do
	gzip -9n < "$f" > "$f".gz &
done
wait

%check
width=$(echo __LONG_WIDTH__ |%__cc -E -P -)
skip_32bit=0
skip_32bit=1

if [ "${width}" != 32 ] || [ "${skip_32bit}" != 1 ]; then
	%{buildroot}%{_bindir}/strace -V
	%make_build -k check VERBOSE=1 CFLAGS="${CFLAGS} -Wno-error=stringop-overread -Wno-error=stringop-overflow -Wno-error=format-overflow"
	echo 'BEGIN OF TEST SUITE INFORMATION'
	tail -n 99999 -- tests*/test-suite.log tests*/ksysent.gen.log
	find tests* -type f -name '*.log' -print0 |
		xargs -r0 grep -H '^KERNEL BUG:' -- ||:
	echo 'END OF TEST SUITE INFORMATION'
fi

%files
%maybe_use_defattr
%doc CREDITS ChangeLog.gz ChangeLog-CVS.gz COPYING NEWS README
%{_bindir}/strace
%{_bindir}/strace-log-merge
%{_mandir}/man1/*

