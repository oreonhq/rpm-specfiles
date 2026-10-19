%global source0_hash 269f3df865692596de214fe42b92dcf87d6a6bc22ddb7ed2abc7f48b82e45e6c
Name:           perl-Convert-Bencode
Version:        1.03
Release:        1%{?dist}
Summary:        Functions for converting to/from bencoded strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Bencode
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-Bencode-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Convert::Bencode)
Provides:       perl(Convert::Bencode)
Provides:       perl(Bencode)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(bytes)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides two functions, bencode and bdecode, which encode and
decode bencoded strings respectively.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Convert-Bencode-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
