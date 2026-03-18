Name:		perl-Types-Serialiser
Summary:	Simple data types for common serialization formats
Version:	1.01
Release:	15%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Types-Serialiser
Source0:	https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/Types-Serialiser-%{version}.tar.gz
Patch0:		Types-Serialiser-1.01-provides.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(common::sense)
BuildRequires:	perl(overload)
# Test Suite
# (no dependencies)
# Dependencies
Requires:	perl(Carp)

%description
This module provides some extra data types that are used by common
serialization formats such as JSON or CBOR. The idea is to have a repository of
simple/small constants and containers that can be shared by different
implementations so they become inter-operable between each other.

%prep
%setup -q -n Types-Serialiser-%{version}

# Hide package declaration of JSON::PP::Boolean from rpm
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
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.01-15
- Prepare for Oreon 11 (RP1)
