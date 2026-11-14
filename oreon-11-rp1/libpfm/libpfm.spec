# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash af518eab2114b0e11dfeacf8dd618b0a1ea04f28cd0b38acad2ec99abff2fd04
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libpfm
Version: 4.14.1
Release: 1%{?dist}
Summary: Performance monitoring library
License: MIT
URL: http://perfmon2.sourceforge.net/
Source0: https://downloads.sourceforge.net/project/perfmon2/libpfm4/libpfm-%{version}.tar.gz
Patch0: libpfm-clang-warnings.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: glibc-devel

%description
libpfm maps hardware performance events to the values the kernel expects.

%package devel
Summary: Development files for libpfm
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Headers and the library link for libpfm.

%prep
%oreon_sha256
%autosetup -n libpfm-%{version} -p1

%build
%make_build -C lib PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y

%install
%make_install -C lib PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y
%make_install -C include PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y
%make_install -C docs PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y
rm -f %{buildroot}%{_libdir}/libpfm.a

%check
%make_build -C tests PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y
./tests/validate

%files
%license COPYING
%{_libdir}/libpfm.so.4*

%files devel
%{_includedir}/perfmon/
%{_libdir}/libpfm.so
%{_mandir}/man3/*
