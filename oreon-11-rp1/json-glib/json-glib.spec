# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: LGPL-2.1-or-later

%global source0_hash 55c5c141a564245b8f8fbe7698663c87a45a7333c2a2c56f06f811ab73b212dd

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: json-glib
Version: 1.10.8
Release: 1%{?dist}
Summary: Library for JavaScript Object Notation format
License: LGPL-2.1-or-later
URL: https://wiki.gnome.org/Projects/JsonGlib
Source0: https://download.gnome.org/sources/json-glib/1.10/json-glib-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: gtk-doc

%description
JSON-GLib is a library for serializing and deserializing JSON using GLib
data types.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: pkgconfig(json-glib-1.0) = %{version}

%description devel
Headers and pkgconfig for %{name}.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc NEWS README.md
%{_libdir}/libjson-glib-1.0.so.*
%{_libdir}/girepository-1.0/Json-1.0.typelib
%{_datadir}/gir-1.0/Json-1.0.gir

%files devel
%{_libdir}/libjson-glib-1.0.so
%{_includedir}/json-glib-1.0/
%{_libdir}/pkgconfig/json-glib-1.0.pc

%changelog
%autochangelog
