%global source0_hash 6af2a222e987e7d985589d0c869a13b48fab43a67a5ee374ddbc2708ee059c1f

Name:           perl-Algorithm-BloomFilter
Version:        0.02
Release:        22%{?dist}
Summary:        A simple bloom filter data structure
# lib/Algorithm/BloomFilter.pm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Algorithm-BloomFilter
Source0:        https://cpan.metacpan.org/authors/id/S/SM/SMUELLER/Algorithm-BloomFilter-%{version}.tar.gz

# build requirements
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(Test::More)

%description
This module implements a simple bloom filter in C/XS.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-BloomFilter-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Algorithm*
%{_mandir}/man3/*

%changelog
%autochangelog
