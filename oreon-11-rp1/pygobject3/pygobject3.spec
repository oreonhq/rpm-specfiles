# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 45068697de3ffe46840ca369705f23118b34db4f7deb63f6eff079a6734ddcca
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: pygobject3
Version: 3.58.0
Release: 1%{?dist}
Summary: Python bindings for GObject
License: LGPL-2.1-or-later
URL: https://pygobject.gnome.org/
Source0: https://download.gnome.org/sources/pygobject/3.58/pygobject-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: meson
BuildRequires: gcc
BuildRequires: python3-devel
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(girepository-2.0)
BuildRequires: pkgconfig(libffi)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(py3cairo)
BuildRequires: gobject-introspection-devel
BuildRequires: python3-pytest

%description
Python access to GObject libraries.

%package -n python3-gobject
Summary: Python bindings for GObject
Requires: python3
Requires: glib2%{?_isa}

%description -n python3-gobject
The gi module for Python.

%package -n python3-gobject-devel
Summary: Development files for PyGObject
Requires: python3-gobject%{?_isa} = %{version}-%{release}
Requires: pkgconfig(gobject-2.0)

%description -n python3-gobject-devel
Headers and pkgconfig for PyGObject.

%prep
%oreon_sha256
%autosetup -n pygobject-%{version}

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n python3-gobject
%license COPYING
%{python3_sitearch}/gi/
%{python3_sitearch}/PyGObject-*.dist-info/

%files -n python3-gobject-devel
%{_includedir}/pygobject-3.0/
%{_libdir}/pkgconfig/pygobject-3.0.pc
