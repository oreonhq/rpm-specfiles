# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 357bcab8877dc9943f355d3a72daba1b053238ba955f50fa81586afb65090219
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           pugixml
Version:        1.16
Release:        1%{?dist}
Summary:        A light-weight C++ XML processing library
License:        MIT
URL:            https://pugixml.org/
VCS:            git:https://github.com/zeux/%{name}.git

Source0:        https://github.com/zeux/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc-c++
BuildRequires:  cmake
%description
pugixml is a light-weight C++ XML processing library.
It features:
- DOM-like interface with rich traversal/modification capabilities
- Extremely fast non-validating XML parser which constructs the DOM tree from
  an XML file/buffer
- XPath 1.0 implementation for complex data-driven tree queries
- Full Unicode support with Unicode interface variants and automatic encoding
  conversions

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for package %{name}

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}

%prep
%oreon_sha256
%autosetup -p1

%build
%cmake -DPUGIXML_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%doc readme.txt
%license LICENSE.md
%{_libdir}/libpugixml.so.1*

%files devel
%{_libdir}/libpugixml.so
%{_libdir}/cmake/pugixml/
%{_libdir}/pkgconfig/pugixml.pc
%{_includedir}/*.hpp

%files doc
%doc docs/*

%changelog
%autochangelog
