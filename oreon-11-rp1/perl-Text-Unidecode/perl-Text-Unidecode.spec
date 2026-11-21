# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 6c24f14ddc1d20e26161c207b73ca184eed2ef57f08b5fb2ee196e6e2e88b1c6

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Text-Unidecode
Version:        1.30
Release:        1%{?dist}
Summary:        ASCII transliterations of Unicode text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Unidecode
Source0:        https://cpan.metacpan.org/authors/id/S/SB/SBURKE/Text-Unidecode-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  oreon-rpm-macros
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
Provides:       perl(Text::Unidecode)

%description
Plain ASCII transliterations of Unicode text.

%prep
%oreon_sha256
%setup -q -n Text-Unidecode-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc README ChangeLog
%{perl_vendorlib}/Text
%{_mandir}/man3/*

%changelog
%autochangelog
