# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash d1008fb78dcae1323ddab664bcb352a61f022b1b131bd8018548e021d975ec7a

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: less
Version: 710
Release: 3%{?dist}
Summary: A text file browser similar to more
License: GPL-3.0-or-later OR BSD-2-Clause
URL: https://www.greenwoodsoftware.com/less/
Source0: https://ftp.gnu.org/gnu/less/less-%{version}.tar.gz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: glibc-gconv-extra
BuildRequires: glibc-langpack-en
BuildRequires: make
BuildRequires: ncurses-devel
BuildRequires: pcre2-devel
BuildRequires: perl-interpreter >= 4:5.44.0-4

%description
The less utility is a text file browser that resembles more.

%prep
%oreon_sha256
%autosetup -n less-%{version}

%build
%configure --with-regex=pcre2
%make_build

%install
%make_install

%check
%make_build check

%files
%license COPYING LICENSE
%doc NEWS README
%{_bindir}/less
%{_libexecdir}/lessecho
%{_libexecdir}/less-osc8-open
%{_mandir}/man1/less.1*
%{_mandir}/man1/lessecho.1*
%{_mandir}/man5/lesskey.5*

%changelog
%autochangelog
