%global source0_hash 269f3df865692596de214fe42b92dcf87d6a6bc22ddb7ed2abc7f48b82e45e6c

Name:           perl-Convert-Bencode
Version:        1.03
Release:        43%{?dist}
Summary:        Functions for converting to/from bencoded strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Bencode
Source0:        https://cpan.metacpan.org/modules/by-module/Convert/Convert-Bencode-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(bytes)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(locale)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test::More) >= 0.45
# Dependencies
# (none)

Provides:       perl(Convert::Bencode)
Provides:       perl(Convert::Bencode)
Provides:       perl(Bencode)
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

%check
make test

%files
%license LICENSE
%doc Changes README Todo
%{perl_vendorlib}/Convert/
%{_mandir}/man3/Convert::Bencode.3*

%changelog
%autochangelog
