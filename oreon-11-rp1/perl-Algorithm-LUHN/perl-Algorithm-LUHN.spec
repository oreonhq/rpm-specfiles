%global source0_hash e808fbba13e262608d37923efa917e18407453c4af96ab783fc77f9fe159b9c0

Name:		perl-Algorithm-LUHN
Version:	1.02
Release:	30%{?dist}
Summary:	Calculate the Modulus 10 Double Add Double checksum
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Algorithm-LUHN
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Algorithm-LUHN-%{version}.tar.gz

BuildArch:	noarch
BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(Test)
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	findutils

%description
This module calculates the Modulus 10 Double Add Double checksum, also
known as the LUHN Formula. This algorithm is used to verify credit
card numbers and Standard & Poor's security identifiers such as
CUSIP's and CSIN's.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-LUHN-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%if 0%{?_licensedir:1}
%license LICENSE
%else
%doc LICENSE
%endif
%{perl_vendorlib}/Algorithm/
%{_mandir}/man3/Algorithm::LUHN.3pm*

%changelog
%autochangelog
