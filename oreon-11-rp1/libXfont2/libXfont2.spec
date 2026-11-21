# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8b7b82fdeba48769b69433e8e3fbb984a5f6bf368b0d5f47abeec49de3e58efb

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXfont2
Version: 2.0.7
Release: 1%{?dist}
Summary: X font library
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/lib/libXfont2-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorgproto
BuildRequires: xtrans
BuildRequires: libfontenc-devel
BuildRequires: freetype-devel
BuildRequires: zlib-devel

%description
X font library used by the X server.

%package devel
Summary: Development files for libXfont2
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libfontenc-devel
Requires: freetype-devel
Provides: pkgconfig(xfont2) = %{version}

%description devel
Headers and pkgconfig for libXfont2.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static --enable-freetype
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
%make_build check

%files
%license COPYING
%{_libdir}/libXfont2.so.2*

%files devel
%{_includedir}/X11/fonts/
%{_libdir}/libXfont2.so
%{_libdir}/pkgconfig/xfont2.pc

%changelog
%autochangelog
