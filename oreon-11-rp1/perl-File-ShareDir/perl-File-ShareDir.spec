# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 3bb2a20ba35df958dc0a4f2306fc05d903d8b8c4de3c8beefce17739d281c958

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: perl-File-ShareDir
Version: 1.118
Release: 1%{?dist}
Summary: Locate per-dist and per-module shared files
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/File-ShareDir
Source0: https://cpan.metacpan.org/authors/id/R/RE/REHSACK/File-ShareDir-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Carp)
BuildRequires: perl(Class::Inspector)
BuildRequires: perl(File::ShareDir::Install)
BuildRequires: perl(File::Spec)
BuildRequires: perl(File::Path)
BuildRequires: perl(Test::More)

Requires: perl(Class::Inspector)

%description
File::ShareDir finds the shared data directory for a Perl distribution or module.

%prep
%oreon_sha256
%autosetup -n File-ShareDir-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
