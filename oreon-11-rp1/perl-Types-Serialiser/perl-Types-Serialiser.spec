# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash f8c7173b0914d0e3d957282077b366f0c8c70256715eaef3298ff32b92388a80
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:		perl-Types-Serialiser
Summary:	Simple data types for common serialization formats
Version:	1.01
Release:	1%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Types-Serialiser
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Types-Serialiser-%{version}.tar.gz
Patch0:		Types-Serialiser-1.01-provides.patch
BuildArch:	noarch
BuildRequires: oreon-rpm-macros
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Carp)
BuildRequires:	perl(common::sense)
BuildRequires:	perl(overload)
Requires:	perl(Carp)

%description
This module provides some extra data types that are used by common
serialization formats such as JSON or CBOR. The idea is to have a repository of
simple/small constants and containers that can be shared by different
implementations so they become inter-operable between each other.

%prep
%oreon_sha256
%setup -q -n Types-Serialiser-%{version}

%patch -P 0

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
%license COPYING
%doc Changes README
%{perl_vendorlib}/Types/
%{_mandir}/man3/Types::Serialiser.3*
%{_mandir}/man3/Types::Serialiser::Error.3*

%changelog
%autochangelog
