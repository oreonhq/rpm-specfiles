# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a9b63eea997abb9ee6a8b4fbb515831c841f471af845a09de443b28003874bec

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libxkbfile
Version: 1.1.3
Release: 2%{?dist}
Summary: XKB file library
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/lib/libxkbfile-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorgproto
BuildRequires: libX11-devel

%description
Library for reading and writing XKB description files.

%package devel
Summary: Development files for libxkbfile
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel
Provides: pkgconfig(xkbfile) = %{version}

%description devel
Headers and pkgconfig for libxkbfile.

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
%{_libdir}/libxkbfile.so.1*

%files devel
%{_includedir}/X11/extensions/XKB*.h
%{_includedir}/X11/extensions/XKM.h
%{_includedir}/X11/extensions/XKMformat.h
%{_libdir}/libxkbfile.so
%{_libdir}/pkgconfig/xkbfile.pc

%changelog
%autochangelog
