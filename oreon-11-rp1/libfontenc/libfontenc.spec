# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7b02c3d405236e0d86806b1de9d6868fe60c313628b38350b032914aa4fd14c6

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libfontenc
Version: 1.1.8
Release: 1%{?dist}
Summary: X font encoding library
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/lib/libfontenc-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorgproto
BuildRequires: zlib-devel

%description
Font encoding library used by the X font code.

%package devel
Summary: Development files for libfontenc
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: zlib-devel
Provides: pkgconfig(fontenc) = %{version}

%description devel
Headers and pkgconfig for libfontenc.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
%make_build check

%files
%license COPYING
%{_libdir}/libfontenc.so.1*

%files devel
%{_includedir}/X11/fonts/fontenc.h
%{_libdir}/libfontenc.so
%{_libdir}/pkgconfig/fontenc.pc

%changelog
%autochangelog
