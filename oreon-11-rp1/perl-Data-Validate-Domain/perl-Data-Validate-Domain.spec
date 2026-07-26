%global source0_hash 3c9f79187b0d3c71add1f8f559b80df1599300a6d203e0b161cbe18e176aab36

Name:           perl-Data-Validate-Domain
Version:        0.15
Release:        13%{?dist}
Summary:        Domain validation methods Perl module

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Validate-Domain
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Data-Validate-Domain-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Net::Domain::TLD) >= 1.74
BuildRequires:  perl(strict)
BuildRequires:  perl(Test2::Plugin::UTF8)
BuildRequires:  perl(Test::More) >= 1.302015
BuildRequires:  perl(warnings)

%description
This module collects domain validation routines to make input validation, and
untainting easier and more readable.

All functions return an untainted value if the test passes, and undef if it
fails. This means that you should always check for a defined status explicitly.
Don't assume the return will be true. (e.g. is_username('0'))

The value to test is always the first (and often only) argument.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Validate-Domain-%{version}
/usr/bin/find lib -name "*.pm" -exec chmod -c a-x {} +

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
