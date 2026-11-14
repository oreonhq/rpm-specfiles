# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 75decbcea8d7b354cf36adc9675e53c4790ee3de56a14bd87b42c8e8aad2ecf5

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: imake
Version: 1.0.10
Release: 1%{?dist}
Summary: C preprocessor interface to the make utility
License: MIT
URL: https://www.x.org/
Source0: https://www.x.org/pub/individual/util/imake-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: pkgconfig(xproto)
BuildRequires: xorg-x11-util-macros

%description
imake is a C preprocessor interface to the make utility.

%prep
%oreon_sha256
%autosetup

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING
%doc ChangeLog README*
%{_bindir}/imake
%{_bindir}/xmkmf
%{_bindir}/makeg
%{_mandir}/man1/imake.1*
%{_mandir}/man1/xmkmf.1*
%{_mandir}/man1/makeg.1*

%changelog
%autochangelog
