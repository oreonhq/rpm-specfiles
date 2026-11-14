# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 919f529512961a12e81cd4b4b466a48c3933469e7f9a310c6513cd4fb252ba3c
%global gdk_pixbuf_binary_version 2.10.0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: gdk-pixbuf2
Version: 2.44.8
Release: 1%{?dist}
Summary: Image loading and scaling library
License: LGPL-2.1-or-later
URL: https://gitlab.gnome.org/GNOME/gdk-pixbuf
Source0: https://download.gnome.org/sources/gdk-pixbuf/2.44/gdk-pixbuf-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: python3
BuildRequires: python3-docutils
BuildRequires: shared-mime-info
BuildRequires: pkgconfig(gio-2.0) >= 2.56
BuildRequires: pkgconfig(glib-2.0) >= 2.56
BuildRequires: pkgconfig(gmodule-no-export-2.0) >= 2.56
BuildRequires: pkgconfig(gobject-2.0) >= 2.56
%if %{without bootstrap}
BuildRequires: pkgconfig(gobject-introspection-1.0)
%endif
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libpng)

Requires: shared-mime-info

%description
GdkPixbuf provides image loading, scaling, compositing and animation
support for applications using GLib.

%package devel
Summary: Development files for GdkPixbuf
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig

%description devel
Headers and development files for applications using GdkPixbuf.

%package tests
Summary: Installed test suite for GdkPixbuf
Requires: %{name}%{?_isa} = %{version}-%{release}

%description tests
Installed tests for checking GdkPixbuf on a running system.

%prep
%oreon_sha256
%autosetup -n gdk-pixbuf-%{version}

%build
%meson \
  -Dgif=enabled \
  -Dinstalled_tests=true \
%if %{without bootstrap}
  -Dintrospection=enabled \
%else
  -Dintrospection=disabled \
%endif
  -Djpeg=enabled \
  -Dpng=enabled \
  -Dtests=true
%meson_build

%install
%meson_install
%find_lang gdk-pixbuf
mv %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders \
  %{buildroot}%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits}
touch %{buildroot}%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache

%check
%meson_test

%posttrans
%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits} \
  > %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache || :

%ldconfig_post
%ldconfig_postun

%files -f gdk-pixbuf.lang
%license COPYING
%doc NEWS README.md
%{_bindir}/gdk-pixbuf-csource
%{_bindir}/gdk-pixbuf-pixdata
%{_bindir}/gdk-pixbuf-query-loaders-%{__isa_bits}
%{_bindir}/gdk-pixbuf-thumbnailer
%{_libdir}/libgdk_pixbuf-2.0.so.0*
%dir %{_libdir}/gdk-pixbuf-2.0/
%dir %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/
%dir %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/
%{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders/*.so
%ghost %{_libdir}/gdk-pixbuf-2.0/%{gdk_pixbuf_binary_version}/loaders.cache
%if %{without bootstrap}
%{_libdir}/girepository-1.0/GdkPixbuf-2.0.typelib
%{_libdir}/girepository-1.0/GdkPixdata-2.0.typelib
%endif
%{_datadir}/thumbnailers/gdk-pixbuf-thumbnailer.thumbnailer
%{_mandir}/man1/gdk-pixbuf-*.1*

%files devel
%{_includedir}/gdk-pixbuf-2.0/
%{_libdir}/libgdk_pixbuf-2.0.so
%{_libdir}/pkgconfig/gdk-pixbuf-2.0.pc
%if %{without bootstrap}
%{_datadir}/gir-1.0/GdkPixbuf-2.0.gir
%{_datadir}/gir-1.0/GdkPixdata-2.0.gir
%endif

%files tests
%{_libexecdir}/installed-tests/gdk-pixbuf/
%{_datadir}/installed-tests/gdk-pixbuf/

%changelog
%autochangelog
