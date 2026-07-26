%global source0_hash 5d7d91560a0012245967bf422cf82d2442ad92b8449cad0d464b259e47d20439

Name:           perl-WebService-Validator-CSS-W3C
Version:        0.3
Release:        35%{?dist}
Summary:        Interface to the W3C CSS Validator
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/WebService-Validator-CSS-W3C
Source0:        https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/WebService-Validator-CSS-W3C-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(SOAP::Lite) >= 0.65
BuildRequires:  perl(strict)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::QueryParam)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optionals tests:
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
Requires:       perl(Class::Accessor)

%description
This module is an interface to the W3C CSS Validation online service 
<http://jigsaw.w3.org/css-validator/>, based on its SOAP 1.2 support. 
It helps to find errors in Cascading Style Sheets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n WebService-Validator-CSS-W3C-%{version}
sed -i 's/\r//' Changes README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
