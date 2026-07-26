%global source0_hash 387ffe25315d61270dbdd4728ce30cc59b302ed74f20be6940c62781751cf742

Name:           perl-Inline-Module
Version:        0.34
Release:        32%{?dist}
Summary:        Support for Inline-based CPAN extension modules
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Inline-Module
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Inline-Module-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::ShareDir::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
# Unused BuildRequires:  perl(Data::Dumper)
# Unused BuildRequires:  perl(ExtUtils::CppGuess)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
# Unused BuildRequires:  perl(File::Share)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Inline)
BuildRequires:  perl(Inline::C::Parser::RegExp)
BuildRequires:  perl(XXX)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(Data::Dumper)
Requires:       perl(File::Share)
Requires:       perl(Inline)
Requires:       perl(Inline::C::Parser::RegExp)

%description
This module provides support and documentation for creating and maintaining
CPAN extension modules. i.e. writing XS modules without having to learn XS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Inline-Module-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
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
