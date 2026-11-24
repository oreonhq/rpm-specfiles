# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 7d34910958e1c1f8d193d828fea1b7da192297280a35437af0692f003ba03755
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global tarball libXv

Summary: X.Org X11 libXv runtime library
Name:    libXv
Version: 1.0.13
Release: 1%{?dist}
License: SMLNJ AND HPND-sell-variant
URL: http://www.x.org

Source0:        https://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.xz

Requires: libX11 >= 1.5.99.902

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: gcc
BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(videoproto)
BuildRequires: pkgconfig(xext)
BuildRequires: libX11-devel >= 1.5.99.902

%description
X.Org X11 libXv runtime library

%package devel
Summary: X.Org X11 libXv development package
Requires: %{name} = %{version}-%{release}

%description devel
X.Org X11 libXv development package

%prep
%oreon_sha256
%setup -q

%build
autoreconf -v --install --force
%configure --disable-static
make %{?_smp_mflags}

%install

rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%ldconfig_post
%ldconfig_postun

%files
%doc AUTHORS COPYING
%{_libdir}/libXv.so.1
%{_libdir}/libXv.so.1.0.0

%files devel
%doc man/xv-library-v2.2.txt
%{_includedir}/X11/extensions/Xvlib.h
%{_libdir}/libXv.so
%{_libdir}/pkgconfig/xv.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
