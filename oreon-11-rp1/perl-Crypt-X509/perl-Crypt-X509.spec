%global source0_hash 14796b11d15f76ad7444e78a619b70ffdd9130868dd0b00d858579c9303821c7

Name:           perl-Crypt-X509
Version:        0.55
Release:        8%{?dist}

Summary:        Parse a X.509 certificate
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-X509
Source0:        https://cpan.metacpan.org/authors/id/M/MR/MRSCOTTY/Crypt-X509-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Carp)
BuildRequires:  perl(Convert::ASN1) >= 0.19
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

Requires:       perl(Convert::ASN1) >= 0.19

# Filter out unversioned R: perl(Convert::ASN1)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Convert::ASN1\\)

%description
Crypt::X509 parses X.509 certificates. Methods are provided for accessing
most certificate elements.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-X509-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
