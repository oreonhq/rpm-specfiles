# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash e69a696068ccffd2b435539d583665981b6c6abed596a72832bffbe3e13e1f49

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}

Name:           xtl
Version:        0.8.1
Release:        1%{?dist}
License:        BSD-3-Clause
Summary:        QuantStack tools library
URL:            https://github.com/QuantStack/xtl
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  binutils
BuildRequires:  cmake
BuildRequires:  doctest-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinx_rtd_theme

%description
Basic tools (containers, algorithms) used by other QuantStack packages.

%package devel
Summary:        %{summary}
Provides:       xtl-static = %{version}-%{release}
Requires:       cmake-filesystem

%description devel
Development files for %{name} library.

%package doc
Summary:        %{summary}

%description doc
Documentation files for %{name} library.

%prep
%oreon_sha256

%autosetup -p1

%build
%cmake -DBUILD_TESTS=ON
%cmake_build

pushd docs
make html SPHINXBUILD=sphinx-build-3
rm build/html/.buildinfo
popd

%install
%cmake_install

%check
%cmake_build --target xtest

%files devel
%doc README.md
%license LICENSE
%{_includedir}/xtl/
%{_datadir}/cmake/xtl/
%{_datadir}/pkgconfig/xtl.pc

%files doc
%doc docs/build/html

%changelog
%autochangelog
