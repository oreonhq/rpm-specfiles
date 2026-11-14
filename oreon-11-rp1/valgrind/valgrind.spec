# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9f7a18d128f05d3a80fea53e6953f34aad7200a425ceaee46099a8a798a7dd9c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global toolchain gcc
%global _lto_cflags %{nil}
%undefine _include_minidebuginfo

Summary: Dynamic analysis tools to detect memory or thread bugs and profile
Name: valgrind
Version: 3.28.0
Release: 1%{?dist}
Epoch: 1
License: GPL-3.0-or-later AND bzip2-1.0.6 AND (GPL-3.0-or-later AND LGPL-2.0-or-later) AND (GPL-3.0-or-later AND ISC) AND (GPL-3.0-or-later AND Unlicense) AND (GPL-3.0-or-later AND Zlib) AND (GPL-3.0-or-later WITH GCC-exception-2.0) AND (LGPL-2.0-or-later WITH GCC-exception-2.0) AND (GPL-3.0-or-later AND BSD-3-Clause) AND (GPL-3.0-or-later AND (MIT OR NCSA)) AND CMU-Mach AND (GPL-3.0-or-later AND X11 AND BSD-3-Clause) AND X11 AND (GPL-2.0-or-later WITH Autoconf-exception-generic) AND (GPL-3.0-or-later WITH Autoconf-exception-generic-3.0) AND FSFULLR AND FSFAP AND FSFUL AND FSFULLRWD
URL: https://www.valgrind.org/
Source0: https://sourceware.org/pub/valgrind/valgrind-%{version}.tar.bz2
Source1: valgrind-%{version}.tar.bz2.asc
# Mark Wielaard release key
Source2: gpgkey-28FF4B30A88D5523A7E2CBA20376A15C6FFC11CD.gpg

Patch1: valgrind-3.9.0-cachegrind-improvements.patch
Patch2: valgrind-3.9.0-ldso-supp.patch
Patch3: valgrind-3.26.0-some-stack-protector.patch
Patch4: valgrind-3.26.0-some-Wl-z-now.patch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: glibc-devel
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gdb
BuildRequires: gnupg2
BuildRequires: procps-ng
BuildRequires: perl-generators
BuildRequires: perl(Getopt::Long)
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: docbook-dtds
BuildRequires: elfutils-debuginfod
BuildRequires: elfutils-debuginfod-client
BuildRequires: python3-devel

Recommends: valgrind-docs = %{epoch}:%{version}-%{release}
Recommends: valgrind-scripts = %{epoch}:%{version}-%{release}
Recommends: valgrind-gdb = %{epoch}:%{version}-%{release}
Recommends: elfutils-debuginfod-client

ExclusiveArch: %{ix86} x86_64 ppc ppc64 ppc64le s390x armv7hl aarch64 riscv64

%ifarch %{ix86}
%define valarch x86
%define only_arch --enable-only32bit
%endif
%ifarch x86_64
%define valarch amd64
%define only_arch --enable-only64bit
%endif
%ifarch ppc
%define valarch ppc32
%define only_arch --enable-only32bit
%endif
%ifarch ppc64
%define valarch ppc64be
%define only_arch --enable-only64bit
%endif
%ifarch ppc64le
%define valarch ppc64le
%define only_arch --enable-only64bit
%endif
%ifarch s390x
%define valarch s390x
%define only_arch --enable-only64bit
%endif
%ifarch armv7hl
%define valarch arm
%define only_arch --enable-only32bit
%endif
%ifarch aarch64
%define valarch arm64
%define only_arch --enable-only64bit
%endif
%ifarch riscv64
%define valarch riscv64
%define only_arch --enable-only64bit
%endif

%description
Valgrind is an instrumentation framework for building dynamic analysis
tools. There are Valgrind tools that can automatically detect many
memory management and threading bugs, and profile your programs in
detail. You can also use Valgrind to build new tools. The Valgrind
distribution currently includes six production-quality tools: a memory
error detector (memcheck, the default tool), two thread error
detectors (helgrind and drd), a cache and branch-prediction profiler
(cachegrind), a call-graph generating cache and branch-prediction
profiler (callgrind), and a heap profiler (massif).

%package devel
Summary: Development files for valgrind aware programs
License: bzip2-1.0.6
Recommends: valgrind = %{epoch}:%{version}-%{release}
Provides: pkgconfig(valgrind) = %{version}

%description devel
Header files and libraries for development of valgrind aware programs.

%package docs
Summary: Documentation for valgrind tools, scripts and gdb integration
License: GFDL-1.2-or-later
BuildArch: noarch

%description docs
Documentation in html and pdf, plus man pages for valgrind tools and scripts.

%package scripts
Summary: Scripts for post-processing valgrind tool output
License: GPL-3.0-or-later AND (GPL-3.0-or-later OR MPL-2.0)
Recommends: valgrind-gdb = %{epoch}:%{version}-%{release}

%description scripts
Perl and Python scripts for post-processing valgrind tool output.

%package gdb
Summary: Tools for integrating valgrind and gdb
License: GPL-3.0-or-later
Requires: valgrind = %{epoch}:%{version}-%{release}
Recommends: gdb

%description gdb
Tools and support files for integrating valgrind and gdb.

%package tools-devel
Summary: Development files for building valgrind tools
Requires: valgrind-devel = %{epoch}:%{version}-%{release}
Provides: valgrind-static = %{epoch}:%{version}-%{release}

%description tools-devel
Header files and libraries for development of valgrind tools.

%prep
%oreon_sha256
%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1

%build
./autogen.sh

%define mpiccpath /bin/false

%undefine _strict_symbol_defs_build

%ifarch ppc64
CFLAGS="`echo " %{optflags} " | sed 's/ -fstack-protector\([-a-z]*\) / / g;s/ -O2 / /g;s/ -fexceptions / /g;'`"
%else
CFLAGS="`echo " %{optflags} " | sed 's/ -fstack-protector\([-a-z]*\) / / g;s/ -O2 / /g;'`"
%endif
export CFLAGS

LDFLAGS="`echo " %{build_ldflags} " | sed 's/ -Wl,-z,now / / g;'`"
export LDFLAGS

%configure \
  --with-mpicc=%{mpiccpath} \
  %{only_arch} \
  GDB=%{_bindir}/gdb \
  --with-gdbscripts-dir=%{_datadir}/gdb/auto-load \
  --enable-lto

%make_build

%install
%make_install
mkdir docs/installed
mv %{buildroot}%{_datadir}/doc/valgrind/* docs/installed/
rm -f docs/installed/*.ps

%ifarch %{ix86} x86_64
for i in HAVE_PTHREAD_CREATE_GLIBC_2_0 HAVE_PTRACE_GETREGS HAVE_AS_AMD64_FXSAVE64; do
  sed -i -e 's,^\(#define '$i' 1\|/\* #undef '$i' \*/\)$,#ifdef __x86_64__\n# define '$i' 1\n#endif,' \
    %{buildroot}%{_includedir}/valgrind/config.h
done
%endif

chmod 644 %{buildroot}%{_libexecdir}/valgrind/vgpreload*-%{valarch}-*so

%check
LD_SHOW_AUXV=1 /bin/true
./vg-in-place --error-exitcode=1 /bin/true --help
%make_build CFLAGS="" CXXFLAGS="" LDFLAGS="" check
export PYTHONCOERCECLOCALE=0
make regtest

%files
%license COPYING
%{_bindir}/valgrind
%dir %{_libexecdir}/valgrind
%{_libexecdir}/valgrind/default.supp
%{_libexecdir}/valgrind/*-*-linux
%attr(0755,root,root) %{_libexecdir}/valgrind/vgpreload_*-%{valarch}-linux.so

%files docs
%license COPYING.DOCS
%doc NEWS README_*
%doc docs/installed/html docs/installed/*.pdf
%{_mandir}/man1/*

%files scripts
%license COPYING
%{_bindir}/callgrind_annotate
%{_bindir}/callgrind_control
%{_bindir}/cg_annotate
%{_bindir}/cg_diff
%{_bindir}/cg_merge
%{_bindir}/ms_print
%{_libexecdir}/valgrind/dh_view.css
%{_libexecdir}/valgrind/dh_view.html
%{_libexecdir}/valgrind/dh_view.js

%files gdb
%license COPYING
%{_bindir}/valgrind-di-server
%{_bindir}/valgrind-listener
%{_bindir}/vgdb
%{_bindir}/vgstack
%{_libexecdir}/valgrind/*.xml
%{_datadir}/gdb/auto-load/valgrind-monitor.py
%{_datadir}/gdb/auto-load/valgrind-monitor-def.py

%files devel
%dir %{_includedir}/valgrind
%{_includedir}/valgrind/valgrind.h
%{_includedir}/valgrind/cachegrind.h
%{_includedir}/valgrind/callgrind.h
%{_includedir}/valgrind/drd.h
%{_includedir}/valgrind/helgrind.h
%{_includedir}/valgrind/memcheck.h
%{_includedir}/valgrind/dhat.h
%{_libdir}/pkgconfig/valgrind.pc

%files tools-devel
%license COPYING
%{_includedir}/valgrind/config.h
%{_includedir}/valgrind/libvex*h
%{_includedir}/valgrind/pub_tool_*h
%{_includedir}/valgrind/vki
%dir %{_libdir}/valgrind
%{_libdir}/valgrind/*.a

%changelog
%autochangelog
