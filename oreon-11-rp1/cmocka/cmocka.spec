# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 39f92f366bdf3f1a02af4da75b4a5c52df6c9f7e736c7d65de13283f9f0ef416
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global _lto_cflags %{nil}

Name: cmocka
Version: 2.0.2
Release: 1%{?dist}
Summary: Unit testing framework for C
License: Apache-2.0
URL: https://cmocka.org/
Source0: https://cmocka.org/files/2.0/cmocka-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make

%description
cmocka is a unit testing framework for C with support for mock objects.

%package devel
Summary: Development files for cmocka
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(cmocka) = %{version}

%description devel
Headers and the library link for cmocka.

%prep
%oreon_sha256
%autosetup -n cmocka-%{version}

%build
%cmake -DUNIT_TESTING=ON
%cmake_build

%install
%cmake_install
rm -f %{buildroot}%{_libdir}/libcmocka.a
%oreon_filelist_devel

%check
%ctest

%files -f %{_builddir}/%{name}.files
%license COPYING

%files devel -f %{_builddir}/%{name}-devel.files
