# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash a49b08d56813789e5f03289a3f949459eafe9e40a1a9fc066c42c90009a322cf

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-libintl-perl
Version:        1.37
Release:        2%{?dist}
Summary:        Perl interface to gettext
License:        GPL-3.0-or-later
URL:            https://metacpan.org/release/libintl-perl
Source0:        https://cpan.metacpan.org/authors/id/G/GU/GUIDO/libintl-perl-%{version}.tar.gz
BuildRequires:  oreon-rpm-macros
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(version)
BuildRequires:  perl(Test)
Provides:       perl(Locale::Messages)
Provides:       perl(Locale::TextDomain)
Provides:       perl(Locale::gettext_pp)
Provides:       perl(Locale::Recode)
Requires:       perl(File::Spec)
Requires:       perl(version)

%description
High level Perl interface to Uniforum message translation, including
Locale::Messages.

%prep
%oreon_sha256
%setup -q -n libintl-perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license COPYING
%doc README Changes
%{perl_vendorlib}/Locale
%{perl_vendorarch}/auto
%{_mandir}/man3/*

%changelog
%autochangelog
