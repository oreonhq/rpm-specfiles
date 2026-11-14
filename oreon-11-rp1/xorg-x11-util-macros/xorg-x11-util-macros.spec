# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9ac269eba24f672d7d7b3574e4be5f333d13f04a7712303b1821b2a51ac82e8e

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: xorg-x11-util-macros
Version: 1.20.2
Release: 1%{?dist}
Summary: X.Org X11 Autotools macros
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/pub/individual/util/util-macros-%{version}.tar.xz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: make

Provides: pkgconfig(xorg-macros) = %{version}
Provides: /usr/share/aclocal/xorg-macros.m4

%description
Autotools macros used by X.Org packages.

%prep
%oreon_sha256
%autosetup -n util-macros-%{version}

%build
%configure
%make_build

%install
%make_install

%check
test -f %{buildroot}%{_datadir}/pkgconfig/xorg-macros.pc

%files
%license COPYING
%doc ChangeLog README*
%{_datadir}/aclocal/*.m4
%{_datadir}/pkgconfig/xorg-macros.pc
%{_datadir}/util-macros/
%{_mandir}/man1/*

%changelog
%autochangelog
