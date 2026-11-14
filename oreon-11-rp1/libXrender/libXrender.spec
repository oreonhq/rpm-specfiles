# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3fe88c609df6782e1e7af2e4de36b2563d70cd70ff7dcb1cda561ad64912bb64

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXrender
Version: 0.9.13
Release: 1%{?dist}
Summary: X.Org X11 libXrender runtime library
License: HPND-sell-variant
URL: https://www.x.org

Source0: https://xorg.freedesktop.org/archive/individual/lib/libXrender-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(renderproto)
BuildRequires: xorg-x11-util-macros

%description
X.Org X11 libXrender runtime library.

%package devel
Summary: X.Org X11 libXrender development package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: libX11-devel
Requires: xorg-x11-proto-devel
Requires: pkgconfig
Provides: pkgconfig(xrender) = %{version}

%description devel
X.Org X11 libXrender development package.

%prep
%oreon_sha256

%autosetup -p1

%build
%configure --disable-static
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
%{_libdir}/libXrender.so.1
%{_libdir}/libXrender.so.1.3.0

%files devel
%doc doc/libXrender.txt
%{_includedir}/X11/extensions/Xrender.h
%{_libdir}/libXrender.so
%{_libdir}/pkgconfig/xrender.pc

%changelog
%autochangelog
