# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d4ebd26061d5a5d05355f52289c3f595d744aac8d70c547a012b2be96bc2f014

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

Name: doctest
Version: 2.5.1
Release: 3%{?dist}
Summary: Feature-rich header-only C++ testing framework
# logo is CC-BY-4.0
# doctest/doctest.h and doctest/parts/doctest_fwd.h include BSL-1.0
# scripts/*.cmake are BSD-3-Clause
License: MIT AND CC-BY-4.0 AND BSL-1.0 AND BSD-3-Clause
URL: https://github.com/doctest/%{name}
Source0: %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: doctest-2.5.1-debugger-sigtrap.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc-c++
BuildRequires: cmake

%description
A fast (both in compile times and runtime) C++ testing framework, with the
ability to write tests directly along production source (or in their own
source, if you prefer).

%package devel
Summary: Development files for %{name}
Provides: %{name}-static = %{?epoch:%{epoch}:}%{version}-%{release}
Provides: %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: libstdc++-devel%{?_isa}

%description devel
%{summary}.

%prep
%oreon_sha256

%autosetup -p1

%build
export CXXFLAGS="${CXXFLAGS} -Wno-lifetime-safety-intra-tu-suggestions -Wno-lifetime-safety"
%cmake \
  -DCMAKE_BUILD_TYPE=Release \
  -DDOCTEST_WITH_TESTS:BOOL=ON \
  -DCMAKE_DISABLE_FIND_PACKAGE_MPI:BOOL=ON \
  %{nil}
%cmake_build

%install
%cmake_install

%check
%ctest --output-on-failure --timeout 120

%files devel
%doc README.md CHANGELOG.md CONTRIBUTING.md
%license LICENSE.txt
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
