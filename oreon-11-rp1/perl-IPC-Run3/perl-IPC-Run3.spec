# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 9d048ae7b9ae63871bae976ba01e081d887392d904e5d48b04e22d35ed22011a
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-IPC-Run3
Version:        0.049
Release:        %{autorelease}
Summary:        Run a subprocess in batch mode
License:        GPL-1.0-or-later OR Artistic-1.0-Perl OR BSD-2-Clause
URL:            https://metacpan.org/release/IPC-Run3
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/IPC-Run3-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: oreon-rpm-macros
BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.31
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)

BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Test::Pod)

Patch0:         0001-test-and-fix-for-RT-52317-Calling-run3-garbles-STDIN.patch

%description
This module allows you to run a subprocess and redirect stdin, stdout,
and/or stderr to files and perl data structures. It aims to satisfy 99% of
the need for using system, qx, and open3 with a simple, extremely Perlish
API and none of the bloat and rarely used features of IPC::Run.

%prep
%oreon_sha256
%setup -q -n IPC-Run3-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test RELEASE_TESTING=1

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
