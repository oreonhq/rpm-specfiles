# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d689e2adb7ef7b439f6469b51cda8a7daefc83243854c2a3b8f84d0f029d67ee
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Summary:    X property display utility
Name:       xprop
Version:    1.2.8
Release:    1%{?dist}
License:    MIT
URL:        https://www.x.org
Source0:        https://www.x.org/pub/individual/app/%{name}-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires:  clang
BuildRequires:  make
BuildRequires:  gettext-devel
BuildRequires:  libtool

BuildRequires:  pkgconfig(x11)

Obsoletes: xorg-x11-utils < 7.5-39

%description
The xprop utility is for displaying window and font properties in an X server.

%prep
%oreon_sha256
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%doc README.md
%license COPYING
%{_bindir}/xprop
%{_mandir}/man1/xprop.1*

%changelog
%autochangelog
