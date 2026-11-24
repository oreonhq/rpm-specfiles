# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 61266ab1afc9d73dbc60a8b2af73e99d2fdff47d99544d085760e4fa667b5dd1
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           libgudev
Version:        238
Release:        1%{?dist}
Summary:        GObject-based wrapper library for libudev

License:        LGPL-2.1-or-later
URL:            https://wiki.gnome.org/Projects/libgudev
Source0:        https://download.gnome.org/sources/libgudev/%{version}/libgudev-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  pkgconfig
BuildRequires:  libudev-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
%if %{without bootstrap}
BuildRequires:  umockdev-devel
BuildRequires:  glibc-langpack-fr
%endif

Provides:       libgudev1 = %{version}-%{release}
Obsoletes:      libgudev1 < 230

%description
This library makes it much simpler to use libudev from programs
already using GObject. It also makes it possible to easily use libudev
from other programming languages, such as Javascript, because of
GObject introspection support.

%package devel
Summary:   Header files for %{name}
Requires:  %{name}%{?_isa} = %{version}-%{release}

Provides:       libgudev1-devel = %{version}-%{release}
Obsoletes:      libgudev1-devel < 230

%description devel
This package is necessary to build programs using %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%if %{without bootstrap}
%meson -Dgtk_doc=true -Dtests=enabled -Dvapi=disabled
%else
%meson -Dgtk_doc=true -Dtests=disabled -Dvapi=disabled
%endif
%meson_build

%install
%meson_install

%if %{without bootstrap}
%check
%meson_test
%endif

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS
%{_libdir}/libgudev-1.0.so.*
%{_libdir}/girepository-1.0/GUdev-1.0.typelib

%files devel
%{_libdir}/libgudev-1.0.so
%dir %{_includedir}/gudev-1.0
%dir %{_includedir}/gudev-1.0/gudev
%{_includedir}/gudev-1.0/gudev/*.h
%{_datadir}/gir-1.0/GUdev-1.0.gir
%dir %{_datadir}/gtk-doc/html/gudev
%{_datadir}/gtk-doc/html/gudev/*
%{_libdir}/pkgconfig/gudev-1.0*

%changelog
%autochangelog
