%global source0_hash 7b3e3d1d0d31507a63afafbe56844aba000c47ab0301d466e11b2c63708772f0

Name:           perl-Lingua-EN-Numbers-Easy
Version:        2014120401
Release:        31%{?dist}
Summary:        Hash access to Lingua::EN::Numbers objects
License:        MIT
URL:            https://metacpan.org/release/Lingua-EN-Numbers-Easy
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABIGAIL/Lingua-EN-Numbers-Easy-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Lingua::EN::Numbers) >= 1.01
# Tests only
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00

%description
Lingua::EN::Numbers is a module that translates numbers to English words.
Unfortunately, it has an object oriented interface, which makes it hard to
interpolate them in strings. Lingua::EN::Numbers::Easy translates numbers
to words using a tied hash, which can be interpolated.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Numbers-Easy-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
