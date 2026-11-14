# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d075209d18728b1ca5d0bb864aa047a262a1fde206da8a677d6af75b2ee1ae98

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: pixman
Version: 0.46.2
Release: 1%{?dist}
Summary: Pixel manipulation library
License: MIT
URL: https://gitlab.freedesktop.org/pixman/pixman
Source0: https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson

%description
Pixman is a pixel manipulation library for X and Cairo.

%package devel
Summary: Pixel manipulation library development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: pkgconfig(pixman-1) = %{version}

%description devel
Pixel manipulation library for X and Cairo development package.

%prep
%oreon_sha256

%autosetup -p1

%build
%meson --auto-features=auto
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc

%changelog
%autochangelog
