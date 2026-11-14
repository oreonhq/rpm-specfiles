# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d54a712b7b1d7708bc7a819a8e6e47b2fde9536f487b89ccbca295072a7d9943

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name:           catch2
Version:        2.13.10
Release:        1%{?dist}
Summary:        Modern C++ header-only test framework
License:        BSL-1.0
URL:            https://github.com/catchorg/Catch2
Source0:        https://github.com/catchorg/Catch2/archive/v%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
Catch2 is a multi-paradigm automated test framework for C++.

%package devel
Summary:        Development files for %{name}
Provides:       cmake(Catch2) = %{version}
Requires:       libstdc++-devel

%description devel
Headers and CMake config for %{name}.

%prep
%oreon_sha256
%autosetup -n Catch2-%{version} -p1

%build
%cmake -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DCATCH_BUILD_TESTING=ON \
  -DCATCH_INSTALL_DOCS=ON \
  -DCATCH_ENABLE_WERROR=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.txt
%doc docs/Readme.md
%{_includedir}/catch2
%{_datadir}/Catch2
%{_libdir}/cmake/Catch2
%{_datadir}/cmake/Catch2

%changelog
%autochangelog
