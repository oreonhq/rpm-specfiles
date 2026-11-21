# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4b92eb0c06d10683f7447ce9406cb97cd4b453be18d7279320f7b2f025c10187

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
Source0:        https://github.com/nlohmann/json/archive/refs/tags/v%{version}.tar.gz

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
%autosetup -n json-%{version} -p1

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
