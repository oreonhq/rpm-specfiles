# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 42fd4d980ea86426e457b24bdfa835a6f5ad9517ddb01cdb42b99ab9c8dd5dc9
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:        Library providing binary-decimal and decimal-binary routines for IEEE doubles
Name:           double-conversion
Version:        3.4.0
Release:        1%{?dist}

License:        BSD-3-Clause
URL:            https://github.com/google/double-conversion
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires:  cmake

%description
Provides binary-decimal and decimal-binary routines for IEEE doubles.
The library consists of efficient conversion routines that have been
extracted from the V8 JavaScript engine. The code has been re-factored
and improved so that it can be used more easily in other projects.

%package devel
Summary:        %{summary}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      %{name}-static < 3.1.5-10

%description devel
Contains header files for developing applications that use the %{name}
library.

There is extensive documentation in src/double-conversion.h. Other
examples can be found in test/cctest/test-conversions.cc.

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DBUILD_TESTING=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE
%doc README.md AUTHORS Changelog
%{_libdir}/libdouble-conversion.so.3{,.*}

%files devel
%{_libdir}/libdouble-conversion.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/
%{_includedir}/%{name}/

%changelog
%autochangelog
