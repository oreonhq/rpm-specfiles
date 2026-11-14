# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 342385b6ca3b7c73455d7c80a13b7dbe4489e00bc3bd4c5bd6ed4dce421e374a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: pango
Version: 1.58.2
Release: 1%{?dist}
Summary: System for layout and rendering of international text
License: LGPL-2.1-or-later
URL: https://www.pango.org/
Source0: https://download.gnome.org/sources/pango/1.58/pango-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: python3
BuildRequires: pkgconfig(cairo) >= 1.18.0
BuildRequires: pkgconfig(fontconfig) >= 2.17.0
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fribidi) >= 1.0.6
BuildRequires: pkgconfig(gio-2.0) >= 2.88
BuildRequires: pkgconfig(glib-2.0) >= 2.88
BuildRequires: pkgconfig(gobject-2.0) >= 2.88
%if %{without bootstrap}
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.83.2
%endif
BuildRequires: pkgconfig(harfbuzz) >= 11.0.0

%description
Pango is a library for laying out and rendering international text. It
supports complex scripts through HarfBuzz and multiple rendering backends.

%package devel
Summary: Development files for Pango
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers and development files for applications using Pango.

%package tools
Summary: Utilities for inspecting Pango text layout
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tools
Command-line utilities for inspecting fonts and Pango text layout.

%prep
%oreon_sha256
%autosetup

%build
%meson \
  -Dcairo=enabled \
  -Dfontconfig=enabled \
  -Dfreetype=enabled \
%if %{without bootstrap}
  -Dintrospection=enabled
%else
  -Dintrospection=disabled
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
%{_libdir}/libpango*.so.0*
%if %{without bootstrap}
%{_libdir}/girepository-1.0/Pango*.typelib
%endif

%files devel
%{_includedir}/pango-1.0/
%{_libdir}/libpango*.so
%{_libdir}/pkgconfig/pango*.pc
%if %{without bootstrap}
%{_datadir}/gir-1.0/Pango*.gir
%endif

%files tools
%{_bindir}/pango-*

%changelog
%autochangelog
