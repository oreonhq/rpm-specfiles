# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6c643c7035cdacf67afd68f25d01b90ef889d546c9fcd7c0adf7c2cf91e3a32d

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXext
Version: 1.3.7
Release: 1%{?dist}
Summary: X.Org X11 libXext runtime library
License: MIT AND X11
URL: https://www.x.org

Source0: https://xorg.freedesktop.org/archive/individual/lib/libXext-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xproto)
BuildRequires: pkgconfig(xextproto)
BuildRequires: xorg-x11-util-macros

%description
X.Org X11 libXext runtime library.

%package devel
Summary: X.Org X11 libXext development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel
Requires: xorg-x11-proto-devel
Requires: pkgconfig
Provides: pkgconfig(xext) = %{version}

%description devel
X.Org X11 libXext development package.

%prep
%oreon_sha256

%autosetup -p1

%build
%configure --disable-static --disable-specs
%make_build

%install
%make_install INSTALL="install -p"

rm -f %{buildroot}%{_libdir}/*.la
rm -rf %{buildroot}%{_docdir}

%check
make check

%ldconfig_post
%ldconfig_postun

%files
%license COPYING
%doc AUTHORS ChangeLog README.md
%{_libdir}/libXext.so.6
%{_libdir}/libXext.so.6.4.0

%files devel
%{_includedir}/X11/extensions/*.h
%{_libdir}/libXext.so
%{_libdir}/pkgconfig/xext.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
