%global source0_hash 9a4a1494549a2db27bc4c5a16743a5c88ebc18e13c73019c56f399ae0310baf2
%global debug_package %{nil}
Name:           pybind11-json
Version:        0.2.15
Release:        1%{?dist}
Summary:        Using nlohmann::json with pybind11
License:        BSD-3-Clause
URL:            https://github.com/pybind/pybind11_json
Source0:        https://github.com/pybind/pybind11_json/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  gtest-devel
BuildRequires:  json-devel
BuildRequires:  make
BuildRequires:  pybind11-devel
BuildRequires:  python3-devel
# /oreon:deps
%description
pybind11_json is an nlohmann::json to pybind11 bridge, it allows you to
automatically convert nlohmann::json to py::object and the other way around.
Simply include the header, and the automatic conversion will be enabled.

%package devel
Summary:        %{summary}
BuildArch:      noarch
Requires:       json-devel
Requires:       pybind11-devel
Provides:       %{name}-static = %{version}-%{release}
%description devel
pybind11_json is an nlohmann::json to pybind11 bridge, it allows you to
automatically convert nlohmann::json to py::object and the other way around.
Simply include the header, and the automatic conversion will be enabled.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir pybind11_json-%{version}
%oreon_prep
%build

%cmake \
  -DBUILD_TESTS=ON
%cmake_build
%install
%cmake_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%cmake_build -t tests
%files -f %{oreon_filedir}/main.list
%files -n pybind11-json-devel -f %{oreon_filedir}/pybind11-json-devel.list

%changelog

%autochangelog
