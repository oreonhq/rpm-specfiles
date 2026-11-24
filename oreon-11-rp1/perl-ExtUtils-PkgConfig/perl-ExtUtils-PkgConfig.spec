# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bbeaced995d7d8d10cfc51a3a5a66da41ceb2bc04fedcab50e10e6300e801c6e
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-ExtUtils-PkgConfig
Version:        1.16
Release:        1%{?dist}
Summary:        Simplistic interface to pkg-config
License:        LGPL-2.0-or-later
URL:            https://metacpan.org/release/ExtUtils-PkgConfig
Source0:        https://cpan.metacpan.org/modules/by-module/ExtUtils/ExtUtils-PkgConfig-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(English)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  pkgconfig
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       pkgconfig

%description
The pkg-config program retrieves information about installed libraries,
usually for the purposes of compiling against and linking to them.

ExtUtils::PkgConfig is a very simplistic interface to this utility,
intended for use in the Makefile.PL of perl extensions that bind
libraries that pkg-config knows. It is really just boilerplate code
that you would've written yourself.

%prep
%oreon_sha256
%setup -q -n ExtUtils-PkgConfig-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/ExtUtils/
%{_mandir}/man3/ExtUtils::PkgConfig.3*

%changelog
%autochangelog
