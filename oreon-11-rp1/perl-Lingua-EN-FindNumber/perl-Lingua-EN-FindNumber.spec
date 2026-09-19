%global source0_hash 1d176d1c863fb9844bd19d2c2a4e68a0ed73da158f724a89405b90db7e8dbd04

Name:           perl-Lingua-EN-FindNumber
Version:        1.32
Release:        29%{?dist}
Summary:        Locate (written) numbers in English text
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-FindNumber
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-FindNumber-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Lingua::EN::Words2Nums)
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%description
This module provides a regular expression for finding numbers in
English text. It also provides functions for extracting and
manipulating such numbers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-FindNumber-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
