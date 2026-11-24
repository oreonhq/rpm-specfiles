# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 21c692105db15299b5529af81a11a7ad80397f92c122bd7bf1e4a4b0e85654f7
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global forgeurl https://github.com/cpputest/cpputest

Name:           cpputest
Version:        4.0
Release:        %{autorelease}
Summary:        Unit testing and mocking framework for C/C++

License:        LicenseRef-Callaway-BSD
URL:            https://cpputest.github.io/
Source0:        %{forgeurl}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-no-static-ext.patch
Patch1:         %{name}-fix-cmake-dest.patch
Patch2:         %{name}-remove-stdcxx-linking.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
%global _description %{expand:
CppUTest is a C/C++ based unit xUnit test framework for unit testing and for
test-driving your code. It is written in C++ but is used in C and C++ projects
and frequently used in embedded systems but it works for any C/C++ project.

CppUTest’s core design principles are:
- Simple in design and simple in use.
- Portable to old and new platforms.
- Build with Test-driven Development for Test-driven Developers.}

%description    %{_description}

%package        devel
Summary:        Development files for %{name}
Requires:       cmake-filesystem
Requires:       gcc-c++

%description    devel %{_description}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license COPYING
%doc README.md README_CppUTest_for_C.txt
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/cmake/CppUTest
%{_libdir}/pkgconfig/cpputest.pc

%changelog
%autochangelog
