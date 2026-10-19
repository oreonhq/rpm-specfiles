%global source0_hash bc99df7fe1c1ae615f82b40194e7d0bd2f42be6692de037fd6a267930b273ebb
Name:           perl-Convert-Base64
Version:        0.001
Release:        28%{?dist}
Summary:        Encoding and decoding of Base64 strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Base64
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Convert-Base64-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Convert::Base64)
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This Perl module provides functions to convert strings to and from the Base64
encoding as described in RFC 4648.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Convert-Base64-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.001-28
- Prepare for Oreon 11 (RP1)
