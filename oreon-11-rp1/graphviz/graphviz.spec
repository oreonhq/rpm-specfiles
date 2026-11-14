# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash afc7c28dd43d3639910f58820bdce7d89655aa9ac0a4961ac67ffcf77e6a9ac3

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: graphviz
Version: 15.1.1
Release: 2%{?dist}
Summary: Graph Visualization Tools
License: EPL-1.0
URL: https://www.graphviz.org/
Source0: https://gitlab.com/api/v4/projects/graphviz%2Fgraphviz/packages/generic/graphviz-releases/%{version}/graphviz-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make
BuildRequires: automake
BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(zlib)
%if %{without bootstrap}
BuildRequires: pkgconfig(libgd)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: swig
BuildRequires: python3-devel
%endif
BuildRequires: bison
BuildRequires: flex

%description
A collection of tools for manipulating graph structures and generating
graph layouts.

%package devel
Summary: Development files for graphviz
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: graphviz-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(libgvc) = %{version}

%description devel
Headers and libraries for graphviz.

%prep
%oreon_sha256
%autosetup

%build
./autogen.sh
%if %{with bootstrap}
%configure --disable-static --without-gdk-pixbuf --without-gtk --without-pangocairo --without-gdk --disable-python3
%else
%configure --disable-static --enable-python3
%endif
%make_build

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%check
%make_build check

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md
%{_bindir}/*
%{_libdir}/libcdt.so.*
%{_libdir}/libcgraph.so.*
%{_libdir}/libgvc.so.*
%{_libdir}/libgvpr.so.*
%{_libdir}/liblab_gamut.so.*
%{_libdir}/libpathplan.so.*
%{_libdir}/libxdot.so.*
%{_libdir}/graphviz/
%{_datadir}/graphviz/
%{_mandir}/man1/*
%{_mandir}/man7/*

%files devel
%{_includedir}/graphviz/
%{_libdir}/libcdt.so
%{_libdir}/libcgraph.so
%{_libdir}/libgvc.so
%{_libdir}/libgvpr.so
%{_libdir}/liblab_gamut.so
%{_libdir}/libpathplan.so
%{_libdir}/libxdot.so
%{_libdir}/pkgconfig/*.pc

%changelog
%autochangelog
