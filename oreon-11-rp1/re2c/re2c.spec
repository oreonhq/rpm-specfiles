# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 0ac299ad359e3f512b06a99397d025cfff81d3be34464ded0656f8a96676c029

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: re2c
Version: 3.1
Release: 1%{?dist}
Summary: Lexer generator for C, C++ and Go
License: LicenseRef-Oreon-Public-Domain
URL: https://re2c.org/
Source0: https://github.com/skvadrik/re2c/releases/download/%{version}/re2c-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: make

%description
re2c is a free and open-source lexer generator for C, C++ and Go.

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
%license LICENSE
%doc CHANGELOG README.md
%{_bindir}/re2c
%{_bindir}/re2go
%{_bindir}/re2rust
%{_mandir}/man1/re2c.1*
%{_mandir}/man1/re2go.1*
%{_mandir}/man1/re2rust.1*
%{_datadir}/re2c/

%changelog
%autochangelog
