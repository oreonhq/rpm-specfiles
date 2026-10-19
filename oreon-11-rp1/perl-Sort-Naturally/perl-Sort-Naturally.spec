%global source0_hash eaab1c5c87575a7826089304ab1f8ffa7f18e6cd8b3937623e998e865ec1e746
Name:       perl-Sort-Naturally 
Version:    1.03
Release:        39%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Sort lexically, but sort numeral parts numerically
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Sort-Naturally-%{version}.tar.gz
Url:        https://metacpan.org/release/Sort-Naturally
BuildArch:  noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(integer)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module exports two functions, 'nsort' and 'ncmp'; they are used in
implementing my idea of a "natural sorting" algorithm. Under natural
sorting, numeric substrings are compared numerically, and other
word-characters are compared lexically.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sort-Naturally-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
