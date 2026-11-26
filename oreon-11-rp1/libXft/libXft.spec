# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 60a25b78945ed6932635b3bb1899a517d31df7456e69867ffba27f89ff3976f5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: libXft
Version: 2.3.9
Release: 1%{?dist}
Summary: X FreeType library
License: HPND-sell-variant
URL: https://www.x.org
Source0: https://xorg.freedesktop.org/archive/individual/lib/libXft-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: gcc
BuildRequires: pkgconfig
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrender)
BuildRequires: xorg-x11-util-macros

%description
libXft is the client-side font rendering library, using FreeType, libX11,
and the X Render extension to display anti-aliased text.

%package devel
Summary: Development files for libXft
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: fontconfig-devel
Requires: freetype-devel
Requires: libXrender-devel
Requires: pkgconfig
Provides: pkgconfig(xft) = %{version}

%description devel
Headers and development files for applications using libXft.

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
%doc README.md
%{_libdir}/libXft.so.2
%{_libdir}/libXft.so.2.*

%files devel
%{_includedir}/X11/Xft/
%{_libdir}/libXft.so
%{_libdir}/pkgconfig/xft.pc
%{_mandir}/man3/Xft*.3*

%changelog
%autochangelog
