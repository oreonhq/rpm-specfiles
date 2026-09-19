%global source0_hash 6dddba49dc7e0f0051afaa0abe16f13783a244cd1ebb5f81daa11acb628a4961

Name:           perl-Crypt-RandPasswd
Version:        0.07
Release:        13%{?dist}
Summary:        Random password generator based on FIPS-181
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Crypt-RandPasswd
Source0:        https://cpan.metacpan.org/authors/id/J/JA/JANITOR/Crypt-RandPasswd-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Crypt::RandPasswd provides three functions that can be used to generate
random passwords, constructed from words, letters, or characters.

This code is a Perl implementation of the Automated Password Generator
standard, like the program described in "A Random Word Generator For
Pronounceable Passwords" (not available on-line). This code is a
re-engineering of the program contained in Appendix A of
FIPS Publication 181, "Standard for Automated Password Generator".
In accordance with the standard, the results obtained from this
program are logically equivalent to those produced by the standard.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-RandPasswd-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Crypt*
%{_mandir}/man3/Crypt*

%changelog
%autochangelog
