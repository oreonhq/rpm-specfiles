%global source0_hash 39e249cb6624e440e9820fa661582eae02fa80bed97f9d060d26fbd7074127a7

Name:           perl-Sort-Maker
Version:        0.06
Release:        37%{?dist}
Summary:        Simple way to make efficient sort subs
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Sort-Maker
Source0:        https://cpan.metacpan.org/modules/by-module/Sort/Sort-Maker-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(base)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(strict)
# Tests:
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
Requires:       perl(B::Deparse)
Requires:       perl(List::Util)

%description
This module has two main goals: to make it easy to create correct sort
functions, and to make it simple to select the optimum sorting algorithm
for the number of items to be sorted. Sort::Maker generates complete sort
subroutines in one of four styles: plain, Orcish Maneuver, Schwartzian
Transform, and the Guttman-Rosler Transform. You can also get the source for
a sort sub you create via the sorter_source call.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Sort-Maker-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
