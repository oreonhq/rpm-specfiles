# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b3d50e7a73fbf4642ceef30131c93414901d69eee41c2a5302db650b03e2c792
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           xsimd
Version:        14.3.0
Release:        %{autorelease}
Summary:        C++ wrappers for SIMD intrinsic
License:        BSD-3-Clause
URL:            https://xsimd.readthedocs.io/
%global github  https://github.com/xtensor-stack/xsimd
Source0:        %{github}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
BuildRequires:  doctest-devel

%global debug_package %{nil}

%global _description \
SIMD (Single Instruction, Multiple Data) is a feature of microprocessors that \
has been available for many years. SIMD instructions perform a single operation \
on a batch of values at once, and thus provide a way to significantly \
accelerate code execution. However, these instructions differ between \
microprocessor vendors and compilers. \
 \
xsimd provides a unified means for using these features for library authors. \
Namely, it enables manipulation of batches of numbers with the same arithmetic \
operators as for single values. It also provides accelerated implementation \
of common mathematical functions operating on batches. \

%description %_description

%package devel
Summary:        %{summary}
Provides:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
BuildArch:      noarch

%description devel %_description

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ifnarch ppc64le s390x
%cmake_build -- xtest
%endif

%files devel
%doc README.md
%license LICENSE
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_datadir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
