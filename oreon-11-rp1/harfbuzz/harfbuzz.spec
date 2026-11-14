# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0fc7c565443a5f4be7da65ac5ee5bd737d9b158dc908708b7689a0a5796b0c8d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: harfbuzz
Version: 15.1.0
Release: 1%{?dist}
Summary: Text shaping library
License: MIT
URL: https://github.com/harfbuzz/harfbuzz
Source0: https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
%if %{without bootstrap}
BuildRequires: gtk-doc
BuildRequires: help2man
%endif
BuildRequires: meson
BuildRequires: python3
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
%if %{without bootstrap}
BuildRequires: pkgconfig(gobject-introspection-1.0)
%endif
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)

%description
HarfBuzz is a text shaping library that converts Unicode text into
positioned glyphs for display.

%package devel
Summary: Development files for HarfBuzz
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers and development files for applications using HarfBuzz.

%package tools
Summary: Utilities for inspecting and shaping fonts
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Command-line tools for shaping, subsetting and inspecting fonts.

%prep
%oreon_sha256
%autosetup

%build
%meson \
%if %{without bootstrap}
  -Ddocs=enabled \
  -Dintrospection=enabled \
  -Dtests=enabled
%else
  -Ddocs=disabled \
  -Dintrospection=disabled \
  -Dtests=disabled
%endif
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_scriptlets

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_libdir}/libharfbuzz*.so.0*
%if %{without bootstrap}
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib
%endif

%files devel
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz*.so
%{_libdir}/pkgconfig/harfbuzz*.pc
%{_libdir}/cmake/harfbuzz/
%if %{without bootstrap}
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir
%{_datadir}/gtk-doc/html/harfbuzz/
%endif

%files tools
%{_bindir}/hb-*
%if %{without bootstrap}
%{_mandir}/man1/hb-*.1*
%endif

%changelog
%autochangelog
