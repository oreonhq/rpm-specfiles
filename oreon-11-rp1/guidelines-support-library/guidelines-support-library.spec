# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 733a87a7eea56db075ee060735ba7616a27c1c55955f264d5473bf9e83294ad0
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

Name: guidelines-support-library
Version: 5.0.1
Release:        %{autorelease}

License: MIT
URL: https://github.com/microsoft/GSL
Summary: Guidelines Support Library
Source0: %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch:   guidelines-support-library-4.2.0-test-c++17.patch

%if 0%{?fedora} && 0%{?fedora} >= 42
ExcludeArch: %{ix86}
%endif

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: gtest-devel
BuildRequires: ninja-build

%description
Header-only %{summary}.

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
BuildArch: noarch

%description devel
The Guidelines Support Library (GSL) contains functions and types that are
suggested for use by the C++ Core Guidelines maintained by the Standard C++
Foundation. This repo contains Microsoft's implementation of GSL.

The entire implementation is provided inline in the headers under the gsl
directory. The implementation generally assumes a platform that implements
C++14 support.

While some types have been broken out into their own headers (e.g. gsl/span),
it is simplest to just include gsl/gsl and gain access to the entire library.

%prep
%oreon_sha256
%autosetup -n GSL-%{version} -p1
sed -e '/-Werror/d' -i tests/CMakeLists.txt

%build
%cmake -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DGSL_INSTALL:BOOL=ON \
    -DGSL_TEST:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%doc README.md CONTRIBUTING.md
%license LICENSE ThirdPartyNotices.txt
%{_datadir}/cmake/Microsoft.GSL/
%{_includedir}/gsl/

%changelog
%autochangelog
