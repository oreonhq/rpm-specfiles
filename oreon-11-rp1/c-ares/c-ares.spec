# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 9364b70a12eb59a06830fb488d9357f90100dff0d98b23ea3593a183d43e6f2f

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: c-ares
Version: 1.34.9
Release: 1%{?dist}
Summary: Library for asynchronous DNS requests
License: MIT
URL: https://c-ares.org/
Source0: https://github.com/c-ares/c-ares/releases/download/v%{version}/c-ares-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make

%description
c-ares is a C library for asynchronous DNS requests.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: c-ares-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libcares) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DCARES_SHARED=ON -DCARES_STATIC=OFF -DCARES_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md
%doc README.md
%{_libdir}/libcares.so.*

%files devel
%{_libdir}/libcares.so
%{_includedir}/ares*.h
%{_libdir}/pkgconfig/libcares.pc
%{_libdir}/cmake/c-ares/

%changelog
%autochangelog
