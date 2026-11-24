# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 15d7b28da8ac71d8bc8c9287c2045fd174267bc740bec10cfda332dc1204e0e0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global tarball mtdev

Name:           mtdev
Version:        1.1.6
Release:        1%{?dist}
Summary:        Multitouch Protocol Translation Library
License:        MIT
URL:            http://bitmath.org/code/mtdev/
Source0:        mtdev-%{version}.tar.bz2
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make

%description
%{name} is a stand-alone library which transforms all variants of kernel MT
events to the slotted type B protocol. The events put into mtdev may be from
any MT device, specifically type A without contact tracking, type A with
contact tracking, or type B with contact tracking.

%package devel
Summary:        Multitouch Protocol Translation Library Development Package
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description devel
Multitouch protocol translation library development package.

%prep
%oreon_sha256
%setup -q

%build
autoreconf --force -v --install
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%ldconfig_scriptlets

%files
%doc COPYING README
%{_libdir}/libmtdev.so.*

%files devel
%{_includedir}/mtdev.h
%{_includedir}/mtdev-plumbing.h
%{_includedir}/mtdev-mapping.h
%{_libdir}/libmtdev.so
%{_libdir}/pkgconfig/mtdev.pc
%{_bindir}/mtdev-test

%changelog
%autochangelog
