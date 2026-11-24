# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 4f1a66e746cbe54ff3c2fbada5843df4fbbbe7481d80be003e8d11161935ab74
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:    libasyncns
Version: 0.8
Release: 1%{?dist}
Summary: Asynchronous Name Service Library
License: LGPL-2.1-or-later
URL:     http://0pointer.de/lennart/projects/libasyncns/
Source0: %{url}/%{name}-%{version}.tar.gz
Patch0:  pkg-config-multiarch.patch
Patch1:  equality_in_assert.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires:  make
%description
A small and lightweight library that implements easy to use asynchronous
wrappers around the libc NSS functions getaddrinfo(), res_query() and related.

%package devel
Summary: Development Files for libasyncns Client Development
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development Files for libasyncns Client Development

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%{make_build}

%install
%{make_install}
find %{buildroot} \( -name *.a -o -name *.la \) -exec rm {} \;
rm -rf %{buildroot}%{_datadir}/doc/libasyncns/

%files
%doc README
%license LICENSE
%{_libdir}/libasyncns.so.*

%files devel
%{_includedir}/asyncns.h
%{_libdir}/libasyncns.so
%{_libdir}/pkgconfig/libasyncns.pc

%changelog
%autochangelog
