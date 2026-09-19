%global source0_hash cba98a80403fb898a14c928f237f44816b4848641840ce2517363c2c071b5327

Name:           perl-Crypt-CAST5_PP
Version:        1.04
Release:        49%{?dist}
Summary:        CAST5 block cipher in pure Perl
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-CAST5_PP
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-CAST5_PP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Carp)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More) >= 0.47
# Optional tests only
BuildRequires:  perl(Crypt::CBC) >= 1.22
BuildRequires:  perl(Test::Taint)

%description
This module provides a pure Perl implementation of the CAST5 block cipher.
CAST5 is also known as CAST-128. It is a product of the CAST design
procedure developed by C. Adams and S. Tavares.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-CAST5_PP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes mkschedule README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
