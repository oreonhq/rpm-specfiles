# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2d7d9f6084ab9ce6c534ce71a3dd5144b6e474f3c97616459a88f73f44a64bff

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: iso-codes
Version: 4.20.1
Release: 1%{?dist}
Summary: ISO code lists and translations
License: LGPL-2.1-or-later
URL: https://salsa.debian.org/iso-codes-team/iso-codes
Source0: https://salsa.debian.org/iso-codes-team/iso-codes/-/archive/v%{version}/iso-codes-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: gettext
BuildRequires: make
BuildRequires: python3

%description
This package provides the ISO-639 language, ISO-3166 country and other
ISO code lists with translations.

%prep
%oreon_sha256
%autosetup -n iso-codes-v%{version}

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE COPYING
%doc ChangeLog README.md
%{_datadir}/iso-codes/
%{_datadir}/xml/iso-codes/
%{_datadir}/locale/*/LC_MESSAGES/*
%{_datadir}/pkgconfig/iso-codes.pc

%changelog
%autochangelog
