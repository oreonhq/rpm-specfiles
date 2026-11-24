# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 74b6a2c2b4573a400cafb6ecbf60c98df300cd3d0041296b913d02b2cbbb2676
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

%bcond optional_tests 0

Name:    pybind11
Version: 3.0.4
Release:        %{autorelease}
Summary: Seamless operability between C++11 and Python
License: BSD-3-Clause
URL:	 https://github.com/pybind/pybind11
Source0: https://github.com/pybind/pybind11/archive/v%{version}/%{name}-%{version}.tar.gz

Patch1:  pybind11-2.13.6-Use_usr_prefix.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires: python3-devel

BuildRequires: cmake

%if %{with optional_tests}
BuildRequires: python3dist(scipy)
BuildRequires: python3dist(numpy)
BuildRequires: boost-devel
%endif

BuildRequires: cmake(Eigen3)
BuildRequires: cmake(Catch2)

%global base_description \
pybind11 is a lightweight header-only library that exposes C++ types \
in Python and vice versa, mainly to create Python bindings of existing \
C++ code.

%description
%{base_description}

%package devel
Summary:  Development headers for pybind11
Provides: %{name}-static = %{version}-%{release}

%description devel
%{base_description}

This package contains the development headers for pybind11.

%package -n     python3-%{name}
Summary:        %{summary}

Requires: %{name}-devel%{?_isa} = %{version}-%{release}

%description -n python3-%{name}
%{base_description}

This package contains the Python 3 files.

%prep
%oreon_sha256
%autosetup -p1

%generate_buildrequires
%pyproject_buildrequires -g test

%build
%cmake \
  -DCMAKE_BUILD_TYPE:STRING=Release \
  -DUSE_PYTHON_INCLUDE_DIR=FALSE
%cmake_build
%{pyproject_wheel %{shrink:
  -C cmake.build-type=Release
  -C cmake.define.PYBIND11_INSTALL=OFF
  -C cmake.define.PYBIND11_TEST=OFF
}}

%install
%cmake_install
%pyproject_install
%pyproject_save_files -l pybind11

%check
%cmake_build --target check

%files devel
%license LICENSE
%doc README.rst
%{_includedir}/pybind11/
%{_datadir}/cmake/pybind11/
%{_bindir}/pybind11-config
%{_datadir}/pkgconfig/%{name}.pc

%files -n python3-%{name} -f %{pyproject_files}

%changelog
%autochangelog
