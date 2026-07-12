%global source0_hash 3b7aa07abefce56ea2416f8f7f20afcc95d7003e326f4173bc9874f125d75b6d

Name:           perl-Convert-Bencode_XS
Version:        0.06
Release:        48%{?dist}
Summary:        Faster conversions to/from Bencode format
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Bencode_XS
Source0:        https://cpan.metacpan.org/authors/id/I/IW/IWADE/Convert-Bencode_XS-%{version}.tar.gz
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
# Tests only
BuildRequires:  perl(Test::More)
# Optional tests only
BuildRequires:  perl(Devel::Leak)

Provides:       perl(Convert::Bencode_XS)
Provides:       perl(Convert::Bencode_XS)
%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Convert-Bencode_XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*

%check
# PERL_PERTURB_KEYS to work around randomized hashes, CPAN RT#87012 
PERL_PERTURB_KEYS=0 make test

%files
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Convert*
%{_mandir}/man3/*

%changelog
%autochangelog
