# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0a288114e5f44e31987042c79aecff1ffad53a8154b8ec971c24a69a80f81f77

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xkbcomp
Version: 1.4.7
Release: 1%{?dist}
Summary: XKB keymap compiler
License: MIT
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/app/xkbcomp-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig
BuildRequires: xorg-x11-util-macros
BuildRequires: xorgproto
BuildRequires: libxkbfile-devel
BuildRequires: libX11-devel

Requires: xkeyboard-config

%description
Compiles XKB keymaps into the form the X server loads.

%prep
%oreon_sha256
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%{_bindir}/xkbcomp
%{_libdir}/pkgconfig/xkbcomp.pc
%{_mandir}/man1/xkbcomp.1*

%changelog
%autochangelog
