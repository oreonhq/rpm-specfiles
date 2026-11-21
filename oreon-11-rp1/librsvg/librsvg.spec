# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash c982b8157a054b803493bf994d31e50105eb948dd8da6ab9734e8d392712a3
%global source1_hash 196b66ecc06ac758c0963bf3b8c689ba47bdceacd60dcb2587b1374b6da64102
%global gdk_pixbuf_binary_version 2.10.0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: librsvg
Version: 2.62.4
Release: 1%{?dist}
Summary: SVG rendering library
License: LGPL-2.1-or-later
URL: https://wiki.gnome.org/Projects/LibRsvg
Source0: https://download.gnome.org/sources/librsvg/2.62/librsvg-%{version}.tar.xz
Source1: librsvg-%{version}-vendor.tar.xz

BuildRequires: oreon-rpm-macros >= 1-14
BuildRequires: cargo
BuildRequires: cargo-c
BuildRequires: gcc
BuildRequires: gi-docgen
BuildRequires: gobject-introspection-devel
BuildRequires: meson
BuildRequires: pkgconf
BuildRequires: python3
BuildRequires: python3-docutils
BuildRequires: rust
BuildRequires: vala
BuildRequires: pkgconfig(cairo) >= 1.18.0
BuildRequires: pkgconfig(cairo-gobject) >= 1.18.0
BuildRequires: pkgconfig(cairo-png) >= 1.18.0
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(gdk-pixbuf-2.0) >= 2.20
BuildRequires: pkgconfig(gio-2.0) >= 2.50.0
BuildRequires: pkgconfig(glib-2.0) >= 2.50.0
BuildRequires: pkgconfig(gmodule-2.0) >= 2.50.0
BuildRequires: pkgconfig(gobject-2.0) >= 2.50.0
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(harfbuzz) >= 2.0.0
BuildRequires: pkgconfig(libxml-2.0) >= 2.9.0
BuildRequires: pkgconfig(pango) >= 1.50.0
BuildRequires: pkgconfig(pangocairo) >= 1.50.0
BuildRequires: pkgconfig(pangoft2) >= 1.50.0
BuildRequires: pkgconfig(vapigen)

Requires: gdk-pixbuf2%{?_isa}
Requires(posttrans): gdk-pixbuf2

%description
librsvg renders SVG documents onto Cairo surfaces.

%package devel
Summary: Development files for librsvg
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(cairo)
Requires: pkgconfig(cairo-gobject)
Requires: pkgconfig(gdk-pixbuf-2.0)
Requires: pkgconfig(gio-2.0)
Requires: pkgconfig(glib-2.0)
Requires: pkgconfig(pangocairo)
Provides: pkgconfig(librsvg-2.0) = %{version}

%description devel
Headers, the pkg-config file and the introspection data for librsvg.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup
tar -xf %{SOURCE1}

%build
%oreon_cargo_prep vendor
%meson \
  -Ddocs=enabled \
  -Dintrospection=enabled \
  -Dpixbuf=enabled \
  -Dpixbuf-loader=enabled \
  -Drsvg-convert=enabled \
  -Dtests=true \
  -Dvala=enabled
%meson_build

%install
%meson_install

%check
%meson_test

%posttrans
%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits} \
  > %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache || :

%ldconfig_post
%ldconfig_postun

%files
%license COPYING.LIB
%doc NEWS README.md
%{_bindir}/rsvg-convert
%{_libdir}/librsvg-2.so.2*
%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/libpixbufloader_svg.so
%{_datadir}/thumbnailers/librsvg.thumbnailer
%{_mandir}/man1/rsvg-convert.1*

%files devel
%{_includedir}/librsvg-2.0/
%{_libdir}/librsvg-2.so
%{_libdir}/pkgconfig/librsvg-2.0.pc
%{_libdir}/girepository-1.0/Rsvg-2.0.typelib
%{_datadir}/gir-1.0/Rsvg-2.0.gir
%{_datadir}/vala/vapi/librsvg-2.0.vapi
%{_datadir}/vala/vapi/librsvg-2.0.deps
%{_datadir}/doc/Rsvg-2.0/

%changelog
%autochangelog
