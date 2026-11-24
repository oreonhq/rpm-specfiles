# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8bdf310967f484503fa51714cf97bff0723d9b673e0eecbf92b3f97c060c8ccb
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap


Summary: X Composite Extension library
Name: libXcomposite
Version: 0.4.7
Release: 1%{?dist}
License: MIT AND HPND-sell-variant
URL: http://www.x.org

Source0:        https://www.x.org/pub/individual/lib/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires: make
BuildRequires: xorg-x11-util-macros
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig(compositeproto) >= 0.4
BuildRequires: pkgconfig(xfixes)
BuildRequires: pkgconfig(xext)

%description
X Composite Extension library

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
X.Org X11 libXcomposite development package

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
%doc AUTHORS COPYING README.md ChangeLog
%{_libdir}/libXcomposite.so.1
%{_libdir}/libXcomposite.so.1.0.0

%files devel
%{_includedir}/X11/extensions/Xcomposite.h
%{_libdir}/libXcomposite.so
%{_libdir}/pkgconfig/xcomposite.pc
%{_mandir}/man3/X?omposite*.3*

%changelog
%autochangelog
