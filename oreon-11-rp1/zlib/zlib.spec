# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bb329a0a2cd0274d05519d61c667c062e06990d72e125ee2dfa8de64f0119d16
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name: zlib
Version: 1.3.2
Release: 1%{?dist}
Summary: zlib, a general purpose data compression library
License: Zlib
URL: https://zlib.net/
Source0: https://github.com/madler/zlib/releases/download/v%{version}/zlib-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-devel
BuildRequires: make

%description
zlib 1.3.2 is a general purpose data compression library. All the code is thread safe (though see the FAQ for caveats). The data format used by the zlib library is described by RFCs (Request for Comments) 1950 to 1952 at https://datatracker.ietf.org/doc/html/rfc1950 (zlib format), rfc1951 (deflate format) and rfc1952 (gzip format).

Obsoletes: zlib-ng-compat < 3
Provides: zlib-ng-compat = 2.3.3

%package devel
Summary: zlib, a general purpose data compression library
Requires: zlib%{?_isa} = %{version}-%{release}
Provides: pkgconfig(zlib)
Obsoletes: zlib-ng-compat-devel < 3
Provides: zlib-ng-compat-devel = 2.3.3

%description devel
zlib 1.3.2 is a general purpose data compression library. All the code is thread safe (though see the FAQ for caveats). The data format used by the zlib library is described by RFCs (Request for Comments) 1950 to 1952 at https://datatracker.ietf.org/doc/html/rfc1950 (zlib format), rfc1951 (deflate format) and rfc1952 (gzip format).

%prep
%oreon_sha256
%autosetup -p1

%build
./configure --prefix=%{_prefix} --libdir=%{_libdir} --shared
make -s %{?_smp_mflags}

%install
make -s install DESTDIR=%{buildroot}
rm -f %{buildroot}%{_libdir}/*.a

%files
%license LICENSE
%{_libdir}/libz.so.1
%{_libdir}/libz.so.1.*
%{_mandir}/man3/zlib.3*

%files devel
%{_includedir}/zlib.h
%{_includedir}/zconf.h
%{_libdir}/libz.so
%{_libdir}/pkgconfig/zlib.pc
