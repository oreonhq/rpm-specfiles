# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 117c192ae3b7c37c0156dedaa88038e0599a6b264666c3c6c2553154b500fe23

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%undefine __cmake_in_source_build

Name:           xtensor
Version:        0.27.1
Release:        1%{?dist}
Summary:        C++ tensors with broadcasting and lazy computing
License:        BSD-3-Clause
URL:            https://xtensor.readthedocs.io/

%global github  https://github.com/QuantStack/xtensor
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  xtl-devel
BuildRequires:  doctest-devel

%global debug_package %{nil}

%global _description %{expand:
xtensor is a C++ library meant for numerical analysis with multi-dimensional
array expressions.

xtensor provides:
- an extensible expression system enabling lazy broadcasting.
- an API following the idioms of the C++ standard library.
- tools to manipulate array expressions and build upon xtensor.}

%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
Requires:       xtl-devel

%description devel %_description

%prep
%oreon_sha256

%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install
rm %{buildroot}%{_prefix}/etc/xeus-cpp/tags.d/xtensor.json
rm %{buildroot}%{_datadir}/xeus-cpp/tagfiles/xtensor.tag

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}.hpp
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
