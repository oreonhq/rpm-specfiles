# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5385bc1b8c2f20f3b91d258bf8ccc8cf62023935df2d2676b5b67049f31a049c

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           qrencode
Version:        4.1.1
Release:        1%{?dist}
Summary:        QR Code encoding library
License:        LGPL-2.1-or-later
URL:            https://github.com/fukuchi/libqrencode
Source0:        https://github.com/fukuchi/libqrencode/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  oreon-rpm-macros
BuildRequires:  cmake
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  libpng-devel

%description
Libqrencode encodes data in a QR Code symbol.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       pkgconfig(libqrencode) = %{version}

%description devel
Headers and the pkg-config file for libqrencode.

%prep
%oreon_sha256
%autosetup -n libqrencode-%{version} -p1

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DWITH_TOOLS=ON \
  -DWITH_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets

%files
%license COPYING
%{_bindir}/qrencode
%{_libdir}/libqrencode.so.4*
%{_mandir}/man1/qrencode.1*

%files devel
%{_includedir}/qrencode.h
%{_libdir}/libqrencode.so
%{_libdir}/pkgconfig/libqrencode.pc

%changelog
%autochangelog
