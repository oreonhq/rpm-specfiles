# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9acfe68419c4d06a45c550321b3212762d92f41465062ca4ea19e632ee5d216e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%global _lto_cflags -flto -ffat-lto-objects
%bcond bootstrap 0
%oreon_bootstrap

Name: libxslt
Version: 1.1.45
Release: 1%{?dist}
Summary: Library for transforming XML with XSLT
License: MIT
URL: https://gitlab.gnome.org/GNOME/libxslt
Source0: https://download.gnome.org/sources/libxslt/1.1/libxslt-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(libxml-2.0)

%description
libxslt applies XSLT stylesheets to XML documents. xsltproc is the command line tool.

%package devel
Summary: Development files for libxslt
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libxml2-devel%{?_isa}

%description devel
Headers and pkgconfig files for libxslt.

%package doc
Summary: API docs for libxslt
BuildArch: noarch

%description doc
gtk-doc HTML for libxslt and libexslt.

%prep
%oreon_sha256
%autosetup -n libxslt-%{version}

%build
%configure --disable-static --without-python
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la
find %{buildroot} -name '*.a' -delete

%check
%make_build check

%files
%license Copyright
%{_bindir}/xsltproc
%{_libdir}/libxslt.so.1*
%{_libdir}/libexslt.so.0*
%{_mandir}/man1/xsltproc.1*

%files devel
%{_bindir}/xslt-config
%{_includedir}/libxslt/
%{_includedir}/libexslt/
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%{_libdir}/cmake/libxslt/
%{_libdir}/xsltConf.sh
%{_mandir}/man3/*

%files doc
%{_datadir}/gtk-doc/html/libxslt/
%{_datadir}/gtk-doc/html/libexslt/
%{_docdir}/libxslt/

%changelog
%autochangelog
