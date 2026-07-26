%global source0_hash 686556797cd2a4eaa066f19bbf03ab25c06278292c9ead2f187dfd9031ea1d85

Name:           perl-Lingua-EN-Words2Nums
Version:        0.18
Release:        31%{?dist}
Summary:        Convert English text to numbers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-EN-Words2Nums
Source0:        https://cpan.metacpan.org/authors/id/J/JO/JOEY/Lingua-EN-Words2Nums-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Test)

%description
This module converts English text into numbers. It supports both ordinal
and cardinal numbers, negative numbers, and very large numbers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Words2Nums-%{version}
chmod -c a-x testnum

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README samples testnum TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
