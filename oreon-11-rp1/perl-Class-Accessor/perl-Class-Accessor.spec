# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash bf12a3e5de5a2c6e8a447b364f4f5a050bf74624c56e315022ae7992ff2f411c
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           perl-Class-Accessor
Version:        0.51
Release:        1%{?dist}
Summary:        Automated accessor generation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-Accessor
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: oreon-rpm-macros
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Hash)

%description
This module automagically generates accessors/mutators for your class.

%prep
%oreon_sha256
%setup -q -n Class-Accessor-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make  %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes examples/ README
%{perl_vendorlib}/Class/
%{_mandir}/man3/Class::Accessor.3*
%{_mandir}/man3/Class::Accessor::Fast.3*
%{_mandir}/man3/Class::Accessor::Faster.3*

%changelog
%autochangelog
