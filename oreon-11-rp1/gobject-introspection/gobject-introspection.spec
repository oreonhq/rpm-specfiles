# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 920d1a3fcedeadc32acff95c2e203b319039dd4b4a08dd1a2dfd283d19c0b9ae
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global glib2_version 2.80.0
%global gi_series %(echo %{version} | cut -d. -f1-2)

Name: gobject-introspection
Version: 1.86.0
Release: 2%{?dist}
Summary: Introspection system for GObject-based libraries
License: GPL-2.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later AND BSD-2-Clause
URL: https://wiki.gnome.org/Projects/GObjectIntrospection
Source0: https://download.gnome.org/sources/%{name}/%{gi_series}/%{name}-%{version}.tar.xz

Patch0: workaround.patch

BuildRequires: oreon-rpm-macros
BuildRequires: bison
BuildRequires: flex
BuildRequires: gcc
BuildRequires: gettext
%if %{without bootstrap}
BuildRequires: gtk-doc
%endif
BuildRequires: meson
BuildRequires: python3-devel
BuildRequires: python3-mako
BuildRequires: python3-markdown
BuildRequires: python3-setuptools
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(gio-2.0) >= %{glib2_version}
BuildRequires: pkgconfig(libffi)

Requires: glib2%{?_isa} >= %{glib2_version}

%description
GObject Introspection can scan C header and source files in order to
generate introspection "typelib" files. It also provides an API to examine
typelib files, useful for creating language bindings among other
things.

%package devel
Summary: Libraries and headers for gobject-introspection
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libtool
Requires: python3-mako
Requires: python3-markdown
Requires: (python(abi) = %{python3_version} if python3)
Requires: (python3-setuptools if python3 >= 3.12)
Provides: pkgconfig(gobject-introspection-1.0) = %{version}
Provides: pkgconfig(gobject-introspection-no-export-1.0) = %{version}
Provides: /usr/bin/g-ir-scanner
Provides: /usr/bin/g-ir-compiler

%description devel
Libraries and headers for gobject-introspection.

%prep
%oreon_sha256
%autosetup -p1
mv giscanner/ast.py giscanner/gio_ast.py

%build
%meson -Ddoctool=enabled \
%if %{with bootstrap}
  -Dgtk_doc=false \
%else
  -Dgtk_doc=true \
%endif
  -Dpython=%{__python3}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc NEWS README.rst
%license COPYING COPYING.GPL COPYING.LGPL
%{_libdir}/libgirepository-1.0.so.1*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/*.typelib

%files devel
%{_libdir}/libgirepository-1.0.so
%{_libdir}/gobject-introspection/
%{_libdir}/pkgconfig/gobject-introspection-1.0.pc
%{_libdir}/pkgconfig/gobject-introspection-no-export-1.0.pc
%{_includedir}/gobject-introspection-1.0/
%{_bindir}/g-ir-*
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/*.gir
%{_datadir}/gir-1.0/gir-1.2.rnc
%{_datadir}/gobject-introspection-1.0/
%{_datadir}/aclocal/introspection.m4
%if %{without bootstrap}
%dir %{_datadir}/gtk-doc
%dir %{_datadir}/gtk-doc/html
%{_datadir}/gtk-doc/html/gi/
%endif
%{_mandir}/man1/g-ir-compiler.1*
%{_mandir}/man1/g-ir-doc-tool.1*
%{_mandir}/man1/g-ir-generate.1*
%{_mandir}/man1/g-ir-scanner.1*

%changelog
%autochangelog
