%global source0_hash e808fbba13e262608d37923efa917e18407453c4af96ab783fc77f9fe159b9c0
Name:		perl-Algorithm-LUHN
Version:	1.02
Release:        1%{?dist}
Summary:        Calculate the Modulus 10 Double Add Double checksum
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Algorithm-LUHN
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Algorithm-LUHN-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
