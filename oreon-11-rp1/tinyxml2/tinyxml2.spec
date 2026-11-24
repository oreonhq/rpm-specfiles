# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5556deb5081fb246ee92afae73efd943c889cef0cafea92b0b82422d6a18f289
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global so_version 11

Name:           tinyxml2
Version:        11.0.0
Release:        1%{?dist}
Summary:        Simple, small and efficient C++ XML parser
License:        Zlib
URL:            https://github.com/leethomason/tinyxml2
Source0:        %{url}/archive/%{version}/tinyxml2-%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  cmake

%description
TinyXML-2 is a simple, small, efficient, C++ XML parser that can be easily
integrated into other programs. It uses a Document Object Model (DOM), meaning
the XML data is parsed into a C++ objects that can be browsed and manipulated,
and then written to disk or another output stream.

%package devel
Summary:        Development files for tinyxml2
Requires:       tinyxml2%{?_isa} = %{version}-%{release}

%description devel
This package contains the libraries and header files that are needed
for writing applications with the tinyxml2 library.

%prep
%oreon_sha256
%autosetup -p1
rm -rf docs/

%build
%cmake \
  -Dtinyxml2_BUILD_TESTING:BOOL=ON \
  -Dtinyxml2_INSTALL_PKGCONFIG:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.txt
%doc readme.md
%{_libdir}/libtinyxml2.so.%{so_version}{,.*}

%files devel
%{_includedir}/tinyxml2.h
%{_libdir}/libtinyxml2.so
%{_libdir}/pkgconfig/tinyxml2.pc
%{_libdir}/cmake/tinyxml2/

%changelog
%autochangelog
