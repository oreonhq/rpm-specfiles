# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 68469818a77da196900ee5150bd1bcec832f6333e25945661d15e60c0ba00b28

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:    lksctp-tools
Summary: User-space access to Linux Kernel SCTP
Version: 1.0.21
Release: 1%{?dist}
License: GPL-2.0-or-later AND LGPL-2.0-only AND MIT
URL:     https://github.com/sctp/lksctp-tools/wiki

Source0: https://github.com/sctp/lksctp-tools/archive/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: binutils
BuildRequires: gcc
BuildRequires: libtool
BuildRequires: make

%description
This is the lksctp-tools package for Linux Kernel SCTP (Stream Control
Transmission Protocol) Reference Implementation.

This package is intended to supplement the Linux Kernel SCTP Reference
Implementation now available in the Linux kernel source tree in
versions 2.5.36 and following.  For more information on LKSCTP see the
package documentation README file, section titled "LKSCTP - Linux
Kernel SCTP."

This package contains the base run-time library and command-line tools.

%package devel
Summary: Development files for lksctp-tools
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for lksctp-tools which include man pages, header files,
static libraries, symlinks to dynamic libraries and some tutorial source code.

%package doc
Summary: Documents pertaining to SCTP
Requires: %{name}%{?_isa} = %{version}-%{release}

%description doc
Documents pertaining to LKSCTP & SCTP in general (IETF RFC's & Internet
Drafts).

%prep
%oreon_sha256

%setup -q -n %{name}-%{name}-%{version}

%build
[ ! -x ./configure ] && sh bootstrap
%configure --disable-static
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build

%install
rm -f doc/rfc2960.txt doc/states.txt
%make_install

find $RPM_BUILD_ROOT -type f -name "*.la" -delete

%check
nm -D --defined-only %{buildroot}%{_libdir}/libsctp.so.1 | grep -q ' T sctp_bindx$'
nm -D --defined-only %{buildroot}%{_libdir}/libsctp.so.1 | grep -q ' T sctp_sendmsg$'
nm -D --defined-only %{buildroot}%{_libdir}/libsctp.so.1 | grep -q ' T sctp_peeloff$'
test -x %{buildroot}%{_bindir}/checksctp

%files
%doc AUTHORS ChangeLog COPYING* README
%{_bindir}/*
%{_libdir}/libsctp.so.1*
%dir %{_libdir}/lksctp-tools/
%{_libdir}/lksctp-tools/libwithsctp.so.1*
%{_mandir}/man7/*

%files devel
%{_includedir}/*
%{_libdir}/libsctp.so
%{_libdir}/pkgconfig/libsctp.pc
%{_libdir}/lksctp-tools/libwithsctp.so
%{_datadir}/lksctp-tools/
%{_mandir}/man3/*

%files doc
%doc doc/*.txt

%changelog
%autochangelog
