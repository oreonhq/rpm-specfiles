# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash ecae8008e2cc9ade2f2c1bb9d5e6d4fb73e7c433866a056bd82980741571a022

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libjpeg-turbo
Version: 3.1.4.1
Release: 1%{?dist}
Summary: SIMD-accelerated JPEG image codec
License: IJG AND BSD-3-Clause AND Zlib
URL: https://github.com/libjpeg-turbo/libjpeg-turbo
Source0: https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/%{version}/libjpeg-turbo-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: cmake
BuildRequires: nasm
BuildRequires: make

Provides: libjpeg = 6b-47%{?dist}
Provides: libjpeg%{?_isa} = 6b-47%{?dist}
Provides: pkgconfig(libjpeg) = %{version}

%description
libjpeg-turbo is a JPEG image codec that uses SIMD instructions.

%package devel
Summary: Development files for libjpeg-turbo
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: libjpeg-devel = 6b-47%{?dist}
Provides: pkgconfig(libjpeg) = %{version}
Provides: pkgconfig(libturbojpeg) = %{version}

%description devel
Headers and libraries for libjpeg-turbo.

%package utils
Summary: Utilities for manipulating JPEG images
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
Command line tools for JPEG images.

%prep
%oreon_sha256
%autosetup -n libjpeg-turbo-%{version}

%build
%cmake -DWITH_JPEG8=1
%cmake_build

%install
%cmake_install

%check
%ctest

%files
%license LICENSE.md README.ijg
%doc README.md
%{_libdir}/libjpeg.so.*
%{_libdir}/libturbojpeg.so.*

%files devel
%{_includedir}/*.h
%{_libdir}/libjpeg.so
%{_libdir}/libturbojpeg.so
%{_libdir}/pkgconfig/libjpeg.pc
%{_libdir}/pkgconfig/libturbojpeg.pc
%{_libdir}/cmake/libjpeg-turbo/

%files utils
%{_bindir}/cjpeg
%{_bindir}/djpeg
%{_bindir}/jpegtran
%{_bindir}/rdjpgcom
%{_bindir}/wrjpgcom
%{_bindir}/tjbench
%{_mandir}/man1/*

%changelog
%autochangelog
