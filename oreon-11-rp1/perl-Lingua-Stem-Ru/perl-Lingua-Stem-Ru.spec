%global source0_hash 1270ceb74764fdb958370a808834af976e87f69a85470f8bc46258797eab5228

Name:           perl-Lingua-Stem-Ru
Version:        0.04
Release:        28%{?dist}
Summary:        Porter's stemming algorithm for Russian (KOI8-R only)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Lingua-Stem-Ru
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-Stem-Ru-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter) >= 5.57
# Tests:
BuildRequires:  perl(Test::More) >= 0.88

%description
This module applies the Porter Stemming Algorithm to its parameters,
returning the stemmed words.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-Stem-Ru-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
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
