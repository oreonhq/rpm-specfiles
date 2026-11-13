# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d18b97764c755528c1051d376e33545d0eb60c6ebf85680436813fa5b04cc3d1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libpfm
Version: 4.13.0
Release: 1%{?dist}
Summary: Performance monitoring library
License: MIT
URL: http://perfmon2.sourceforge.net/
Source0: https://downloads.sourceforge.net/project/perfmon2/libpfm4/libpfm-%{version}.tar.gz
Patch0: libpfm-unused-n.patch

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
%make_build PREFIX=%{_prefix} LIBDIR=%{_libdir} CONFIG_PFMLIB_NOPYTHON=y

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
