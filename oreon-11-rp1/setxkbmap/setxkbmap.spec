# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 360193cecc93f906d8383a8fb5c1f3a7eed35e6ced0e118a64ee56ae13c88cac

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: setxkbmap
Version: 1.3.5
Release: 1%{?dist}
Summary: Set the keyboard using the X Keyboard Extension
License: HPND-sell-variant
URL: https://www.x.org
Source0: https://www.x.org/pub/individual/app/setxkbmap-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: meson
BuildRequires: pkgconfig
BuildRequires: pkgconfig(xkbfile)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xrandr)

Requires: xkeyboard-config

%description
setxkbmap sets the keyboard using the X Keyboard Extension.

%prep
%oreon_sha256
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING
%doc README.md
%{_bindir}/setxkbmap
%{_mandir}/man1/setxkbmap.1*

%changelog
%autochangelog
