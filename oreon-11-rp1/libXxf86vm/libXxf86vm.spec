# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: MIT

%global source0_hash 96af414c73ce1d5449ad04be7f9f27fa8330f844b6dda843ef22e3e1befb3ee3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXxf86vm
Version: 1.1.6
Release: 1%{?dist}
Summary: XFree86-VidMode X extension library
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/releases/individual/lib/libXxf86vm-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xf86vidmodeproto)
BuildRequires: pkgconfig(xproto)

%description
Library for the XFree86-VidMode X extension.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(xxf86vm) = %{version}

%description devel
Headers and libraries for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

%check
make check

%files
%license COPYING
%{_libdir}/libXxf86vm.so.1
%{_libdir}/libXxf86vm.so.1.*

%files devel
%{_libdir}/libXxf86vm.so
%{_includedir}/X11/extensions/xf86vmode.h
%{_libdir}/pkgconfig/xxf86vm.pc

%changelog
%autochangelog
