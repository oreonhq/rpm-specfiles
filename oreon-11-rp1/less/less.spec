# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bc5ca2e99bf8bc6145054e8a487e716bc45275126980e46d3da638329d5e3072

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: less
Version: 710
Release: 1%{?dist}
Summary: A text file browser similar to more
License: GPL-3.0-or-later OR BSD-2-Clause
URL: https://www.greenwoodsoftware.com/less/
Source0: https://github.com/gwsw/less/archive/refs/tags/v%{version}.tar.gz#/less-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: autoconf
BuildRequires: automake

%description
The less utility is a text file browser that resembles more.

%prep
%oreon_sha256
%autosetup -n less-%{version}

%build
./autogen.sh
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING LICENSE
%doc NEWS README
%{_bindir}/less
%{_bindir}/lessecho
%{_bindir}/lesskey
%{_mandir}/man1/less.1*
%{_mandir}/man1/lessecho.1*
%{_mandir}/man1/lesskey.1*

%changelog
%autochangelog
