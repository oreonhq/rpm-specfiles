# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: BSD-3-Clause

%global source0_hash e27a71b6023288d7a5658b99f65d5a9f2c9aea9813092a913a8070a784ea999e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libipt
Version: 2.2.1
Release: 1%{?dist}
Summary: Intel Processor Trace decoder library
License: BSD-3-Clause
URL: https://github.com/intel/libipt
Source0: https://github.com/intel/libipt/archive/refs/tags/v%{version}.tar.gz#/libipt-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make

%description
libipt is a library for decoding Intel Processor Trace.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: libipt-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libipt) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DPTUNIT=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md
%{_libdir}/libipt.so.*

%files devel
%{_libdir}/libipt.so
%{_includedir}/intel-pt.h
%{_libdir}/pkgconfig/libipt.pc
%{_libdir}/cmake/libipt/

%changelog
%autochangelog
