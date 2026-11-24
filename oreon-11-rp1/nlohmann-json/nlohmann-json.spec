# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4b92eb0c06d10683f7447ce9406cb97cd4b453be18d7279320f7b2f025c10187
%global json_testdata_version 3.1.0
%global source1_hash 884b1e21f38cfd6a62c159f1b7e0a8f5168ae5daaa384ed4dc0c0fa6660f21bd

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
Source1:        https://github.com/nlohmann/json_test_data/archive/refs/tags/v%{json_testdata_version}.tar.gz

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
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -n json-%{version} -a 1 -p1

%build
%cmake -G Ninja \
  -DCMAKE_BUILD_TYPE=RelWithDebInfo \
  -DJSON_BuildTests=ON \
  -DJSON_MultipleHeaders=ON \
  -DJSON_TestDataDirectory=%{_builddir}/json-%{version}/json_test_data-%{json_testdata_version}
%cmake_build

%install
%cmake_install

%check
%ctest -LE "not_reproducible|git_required"

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
