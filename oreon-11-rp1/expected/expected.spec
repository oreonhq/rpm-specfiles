# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9a04f4f472fbb5c30bf60402f1ca626c4a76987f867978d0b8a35d7ab3fb8fe7
%global catch2_ver 2.13.10
%global catch2_hash d54a712b7b1d7708bc7a819a8e6e47b2fde9536f487b89ccbca295072a7d9943

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name:           expected
Version:        1.3.1
Release:        1%{?dist}
Summary:        C++11/14/17 std::expected with functional-style extensions
License:        CC0-1.0
URL:            https://github.com/TartanLlama/expected
Source0:        https://github.com/TartanLlama/expected/archive/refs/tags/v%{version}.tar.gz
Source1:        https://github.com/catchorg/Catch2/archive/v%{catch2_ver}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
Single-header C++11/14/17 implementation of std::expected with
functional-style extensions.

%package devel
Summary:        Development files for %{name}
Provides:       expected-devel = %{version}-%{release}
Provides:       cmake(tl-expected) = %{version}
Requires:       libstdc++-devel

%description devel
Header-only development files for %{name}.

%prep
%oreon_sha256
%autosetup -n expected-%{version} -p1
# vendor Catch2 for offline %%check (same hash as catch2 package)
echo "%{catch2_hash}  %{SOURCE1}" | sha256sum -c -
tar -xzf %{SOURCE1} -C %{_builddir}

%build
%cmake -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DEXPECTED_BUILD_TESTS=ON \
  -DEXPECTED_BUILD_PACKAGE=OFF \
  -DFETCHCONTENT_SOURCE_DIR_CATCH2=%{_builddir}/Catch2-%{catch2_ver} \
  -DFETCHCONTENT_FULLY_DISCONNECTED=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license COPYING
%doc README.md
%{_includedir}/tl
%{_datadir}/cmake/tl-expected

%changelog
%autochangelog
