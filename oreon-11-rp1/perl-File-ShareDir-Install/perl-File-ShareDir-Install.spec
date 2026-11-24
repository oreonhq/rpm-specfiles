# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 8f9533b198f2d4a9a5288cbc7d224f7679ad05a7a8573745599789428bc5aea0

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: perl-File-ShareDir-Install
Version: 0.14
Release: 1%{?dist}
Summary: Install shared files
License: GPL-1.0-or-later OR Artistic-1.0-Perl
URL: https://metacpan.org/release/File-ShareDir-Install
Source0: https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-ShareDir-Install-%{version}.tar.gz
BuildArch: noarch

BuildRequires: oreon-rpm-macros
BuildRequires: make
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(File::Spec)
BuildRequires: perl(IO::Dir)
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
BuildRequires: perl(File::Path)
BuildRequires: perl(Test::More)

%description
File::ShareDir::Install installs files from a distribution into a shared directory.

%prep
%oreon_sha256
%autosetup -n File-ShareDir-Install-%{version}

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
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
