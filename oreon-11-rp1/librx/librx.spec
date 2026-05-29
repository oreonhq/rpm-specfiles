%global source0_hash 5bbbb99777fa998837ee19ed3b144e183c331d45cc19df90ec8810a4e66981c1

Summary: POSIX regexp functions
Name: librx
Version: 1.5
Release: 53%{?dist}
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL: http://www.gnu.org/software/rx/rx.html
# Originally downloaded from ftp://ftp.gnu.org/gnu/rx/rx-1.5.tar.bz2
# The FSF no longer offers this code.
Source0: rx-%{version}.tar.bz2
Patch0: rx-1.5-shared.patch
Patch1: rx-1.5-texinfo.patch
Patch2: librx-1.5-libdir64.patch
Patch3: rx-1.5-libtoolmode.patch
BuildRequires: texinfo, libtool
BuildRequires: make

%description
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

%package devel
Summary: POSIX regexp functions, developers library
Requires: %{name} = %{version}-%{release}

%description devel
Rx is, among other things, an implementation of the interface
specified by POSIX for programming with regular expressions.  Some
other implementations are GNU regex.c and Henry Spencer's regex
library.

This package contains files needed for development with librx.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n rx-%{version}
%patch -P0 -p1
%patch -P1 -p1 -b .texipatch
%ifarch x86_64 s390x ia64 %{power64} alpha sparc64 aarch64 %{mips64} riscv64
%patch -P2 -p1 -b .64bit
%endif
%patch -P3 -p1 -b .libtoolmode

%build
# The package has many C99 compatibility issues.  It relies on
# implicit function declarations.  It may not work on 64-bit
# architectures because some pointers are truncated to 32 bits.
%global build_type_safety_c 0
%set_build_flags
CC="$CC -std=gnu89"
%configure
make %{?_smp_mflags}
make doc/rx.info

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_infodir}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}
make install DESTDIR=${RPM_BUILD_ROOT}
install -m 644 doc/rx.info ${RPM_BUILD_ROOT}%{_infodir}
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.la
rm -rf ${RPM_BUILD_ROOT}%{_libdir}/librx.a
chmod -x ${RPM_BUILD_ROOT}%{_includedir}/rxposix.h

%ldconfig_scriptlets

%files
%{_libdir}/*.so.*

%files devel
%doc ANNOUNCE BUILDING COOKOFF rx/ChangeLog
%{_includedir}/*
%{_infodir}/*
%{_libdir}/*.so

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5-53
- Import
