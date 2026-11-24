# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash b4ba7d95297f26341fcdd2595532eaf88026a251630985a3ab2e0443f4ee8d13
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary: Windows MetaFile Library
Name: libwmf
Version: 0.2.17
Release: 1%{?dist}
License: LGPL-2.1-or-later AND GPL-2.0-or-later AND GPL-1.0-or-later
Source0:        https://github.com/caolanm/libwmf/archive/v%{version}.tar.gz
URL: https://github.com/caolanm/libwmf

Provides: bundled(gd) = 2.0.0

Requires: urw-fonts
Requires: %{name}-lite = %{version}-%{release}

Requires: gdk-pixbuf2%{?_isa} >= 2.31.5-2.fc24

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: freetype-devel
BuildRequires: gdk-pixbuf2-devel
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: libpng-devel
BuildRequires: libjpeg-devel
BuildRequires: libXt-devel
BuildRequires: libX11-devel
BuildRequires: dos2unix
BuildRequires: make
%description
A library for reading and converting Windows MetaFile vector graphics (WMF).

%package lite
Summary: Windows Metafile parser library

%description lite
A library for parsing Windows MetaFile vector graphics (WMF).

%package devel
Summary: Support files necessary to compile applications with libwmf
Requires: libwmf = %{version}-%{release}
Requires: freetype-devel, libX11-devel, libxml2-devel, libjpeg-devel, libpng-devel

%description devel
Libraries, headers, and support files necessary to compile applications 
using libwmf.

%prep
%oreon_sha256
%setup -q
f=README ; iconv -f iso-8859-2 -t utf-8 $f > $f.utf8 ; mv $f.utf8 $f

%build
autoreconf -i -f -Ipatches
%configure --with-libxml2 --disable-static --disable-dependency-tracking --with-gsfontdir=/usr/share/fonts/urw-base35
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

rm -rf $RPM_BUILD_ROOT%{_includedir}/libwmf/gd
find doc -name "Makefile*" -exec rm {} \;

rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*afm
rm -rf $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/*t1
sed -i $RPM_BUILD_ROOT%{_datadir}/libwmf/fonts/fontmap -e 's#libwmf/fonts#fonts/urw-base35#g'

%ldconfig_scriptlets
%ldconfig_scriptlets lite

%files
%{_libdir}/libwmf-0.2.so.7*
%{_libdir}/gdk-pixbuf-2.0/*/loaders/*.so
%{_bindir}/wmf2svg
%{_bindir}/wmf2gd
%{_bindir}/wmf2eps
%{_bindir}/wmf2fig
%{_bindir}/wmf2x
%{_bindir}/libwmf-fontmap
%{_datadir}/libwmf/

%files lite
%doc AUTHORS README
%license COPYING
%{_libdir}/libwmflite-0.2.so.7*

%files devel
%doc doc/*.html
%doc doc/*.png
%doc doc/*.gif
%doc doc/html
%doc doc/caolan
%{_libdir}/libwmf*.so
%{_libdir}/pkgconfig/libwmf.pc
%{_includedir}/libwmf/
%{_bindir}/libwmf-config

%changelog
%autochangelog
