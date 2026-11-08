# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 815bfe6792aa11a13a133b86e7f0f45edc5d71eb78f5fb6686c49c7f792b9049

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
BuildRequires: oreon-rpm-macros
# Tests requires network access
%bcond_with test

%global debug_package %{nil}

Name:       toml11
Version:        4.4.0
Release:        1%{?dist}
Summary:    TOML for Modern C++ 

License:    MIT
URL:        https://github.com/ToruNiina/toml11
Source0:        https://github.com/ToruNiina/toml11/archive/v%{version}/toml11-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build

%if %{with test}
BuildRequires: boost-devel
BuildRequires: git-core
BuildRequires:  oreon-rpm-macros
%endif

%global _description %{expand:
toml11 is a C++11 (or later) header-only toml parser/encoder depending only on
C++ standard library.

  * It is compatible to the latest version of TOML v1.0.0.
  * It is one of the most TOML standard compliant libraries, tested with the
    language agnostic test suite for TOML parsers by BurntSushi.
  * It shows highly informative error messages. You can see the error messages
    about invalid files at CircleCI.
  * It has configurable container. You can use any random-access containers
    and key-value maps as backend containers.
  * It optionally preserves comments without any overhead.
  * It has configurable serializer that supports comments, inline tables,
    literal strings and multiline strings.
  * It supports user-defined type conversion from/into toml values.
  * It correctly handles UTF-8 sequences, with or without BOM, both on posix
    and Windows.}

%description %{_description}


%package    devel
Summary:    Development files for %{name}
Provides:   %{name}-static = %{version}-%{release}

%description devel %{_description}

Development files for %{name}.


%prep
%oreon_sha256

%autosetup -p1


%build
%cmake \
    -G Ninja \
%if %{with test}
    -Dtoml11_BUILD_TEST=ON \
%endif
    %{nil}
%cmake_build


%install
%cmake_install


%files devel
%license LICENSE
%doc README.md
%{_includedir}/*.hpp
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/


