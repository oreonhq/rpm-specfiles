# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global byaccdate 20260126
%global source0_hash b618c5fb44c2f5f048843db90f7d1b24f78f47b07913c8c7ba8c942d3eb24b00

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: byacc
Version: 2.0.%{byaccdate}
Release: 1%{?dist}
Summary: Berkeley Yacc LALR parser generator
License: LicenseRef-Oreon-Public-Domain
URL: https://invisible-island.net/byacc/byacc.html
Source0: https://invisible-island.net/archives/byacc/byacc-%{byaccdate}.tgz

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: make

Provides: /usr/bin/yacc
Conflicts: bison < 1:2.0

%description
Berkeley Yacc is an LALR(1) parser generator.

%prep
%oreon_sha256
%autosetup -n byacc-%{byaccdate}

%build
%configure
%make_build

%install
%make_install

%check
%make_build check

%files
%license LICENSE
%doc ACKNOWLEDGEMENTS CHANGES NEW_FEATURES NOTES README*
%{_bindir}/yacc
%{_bindir}/byacc
%{_mandir}/man1/yacc.1*
%{_mandir}/man1/byacc.1*

%changelog
%autochangelog
