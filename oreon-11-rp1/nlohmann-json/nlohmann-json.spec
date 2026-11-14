# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 42f6e95cad6ec532fd372391373363b62a14af6d771056dbfc86160e6dfff7aa

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%global debug_package %{nil}

Name:           nlohmann-json
Version:        3.12.0
Release:        1%{?dist}
Summary:        JSON for Modern C++
License:        MIT
URL:            https://github.com/nlohmann/json
Source0:        https://github.com/nlohmann/json/releases/download/v%{version}/json.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  ninja-build

%description
JSON for Modern C++ is a header-only library that implements a JSON parser
and serializer for C++11 and later.

%package devel
Summary:        Development files for %{name}
Provides:       json-devel = %{version}-%{release}
Provides:       cmake(nlohmann_json) = %{version}
Provides:       pkgconfig(nlohmann_json) = %{version}
Requires:       libstdc++-devel

%description devel
Header-only development files for %{name}.

%prep
%oreon_sha256
%autosetup -n json -p1

%build
%cmake -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DJSON_BuildTests=ON \
  -DJSON_MultipleHeaders=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files devel
%license LICENSE.MIT
%doc README.md
%{_includedir}/nlohmann
%{_datadir}/cmake/nlohmann_json
%{_libdir}/cmake/nlohmann_json
%{_datadir}/pkgconfig/nlohmann_json.pc
%{_libdir}/pkgconfig/nlohmann_json.pc

%changelog
%autochangelog
