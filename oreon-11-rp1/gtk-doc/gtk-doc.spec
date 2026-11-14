# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0e517a5f97069831181be177516bde8aa8b3922398f2bdb09e265d22aecadbc5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global debug_package %{nil}
%define major_minor %(echo %{version} | cut -d. -f1-2)

Name:           gtk-doc
Version:        1.36.1
Release:        2%{?dist}
Summary:        API documentation generation tool for GTK+ and GNOME
License:        GPL-2.0-or-later AND GFDL-1.1-no-invariants-or-later
URL:            https://gitlab.gnome.org/GNOME/gtk-doc/
Source0:        http://download.gnome.org/sources/%{name}/%{major_minor}/%{name}-%{version}.tar.xz

BuildRequires:  oreon-rpm-macros
BuildRequires:  /usr/bin/xsltproc
%bcond_with pdf_docs
%if %{with pdf_docs}
BuildRequires:  dblatex
BuildRequires:  python3-parameterized
%endif
BuildRequires:  docbook-style-xsl
BuildRequires:  docbook-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-lxml
BuildRequires:  python3-pygments
BuildRequires:  yelp-tools

Requires:       /usr/bin/xsltproc
Requires:       cmake-filesystem
Requires:       docbook-style-xsl
Requires:       docbook-utils
Requires:       python3-lxml
Requires:       python3-pygments
Provides:       pkgconfig(gtk-doc) = %{version}

%description
gtk-doc is a tool for generating API reference documentation.
It is used for generating the documentation for GTK+, GLib
and GNOME.

%prep
%oreon_sha256
%autosetup -p1
mv doc/README doc/README.docs

%build
%meson -Dtests=true
%meson_build

%install
%meson_install
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/gtk-doc/

%check
%meson_test

%files
%license COPYING COPYING-DOCS
%doc README.md doc/* examples
%{_bindir}/*
%{_datadir}/aclocal/gtk-doc.m4
%{_datadir}/gtk-doc/
%{_datadir}/pkgconfig/gtk-doc.pc
%{_datadir}/help/*/gtk-doc-manual/
%{_libdir}/cmake/GtkDoc/

%changelog
%autochangelog
