# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash efd299ff27cde40a45efc7dbb97ebe40a0c461921cb462f1d62611642bb4ee86
%global source1_hash fa1543d3bffae062f4c0f049e71361b5154579c4aa2baaf40699f469ba2079be
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: liburing
Version: 2.15
Release: 1%{?dist}
Summary: Linux-native io_uring I/O access library
License: (GPL-2.0-only WITH Linux-syscall-note OR MIT) AND (LGPL-2.0-or-later OR MIT)
Source0:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz
Source1:        https://brick.kernel.dk/snaps/%{name}-%{version}.tar.gz.asc
URL: https://git.kernel.dk/cgit/liburing/
BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make

%description
Provides native async IO for the Linux kernel, in a fast and efficient
manner, for both buffered and O_DIRECT.

%package devel
Summary: Development files for Linux-native io_uring I/O access library
Requires: %{name}%{_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
This package provides header files to include and libraries to link with
for the Linux-native io_uring.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup -p1

%build
%set_build_flags
./configure --prefix=%{_prefix} --libdir=/%{_libdir} --libdevdir=/%{_libdir} --mandir=%{_mandir} --includedir=%{_includedir} --use-libc

%make_build

%install
%make_install

%files
%{_libdir}/liburing.so.*
%{_libdir}/liburing-ffi.so.*
%license COPYING

%files devel
%{_includedir}/liburing/
%{_includedir}/liburing.h
%{_libdir}/liburing.so
%{_libdir}/liburing-ffi.so
%exclude %{_libdir}/liburing.a
%exclude %{_libdir}/liburing-ffi.a
%{_libdir}/pkgconfig/*
%{_mandir}/man2/*
%{_mandir}/man3/*
%{_mandir}/man7/*

%changelog
%autochangelog
