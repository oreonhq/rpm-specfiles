# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 2a5bfd926c4fe5f77e6137da2c31ac2545282ae5fec6e9af0fdd403555a90ff4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Unicode-EastAsianWidth
Version:        12.0
Release:        2%{?dist}
Summary:        East Asian Width properties for Perl
License:        CC0-1.0
URL:            https://metacpan.org/release/Unicode-EastAsianWidth
Source0:        https://cpan.metacpan.org/authors/id/A/AU/AUDREYT/Unicode-EastAsianWidth-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test)
Provides:       perl(Unicode::EastAsianWidth)

%description
East Asian Width Unicode properties.

%prep
%oreon_sha256
%setup -q -n Unicode-EastAsianWidth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc README Changes
%{perl_vendorlib}/Unicode
%{_mandir}/man3/*

%changelog
%autochangelog
