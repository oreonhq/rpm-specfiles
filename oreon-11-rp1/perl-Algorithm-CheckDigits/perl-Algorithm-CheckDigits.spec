%global source0_hash 0f2487a8fd1f31b19c51b2650842f2264c1e77d962487a13b521bbe066c4b4bc

Name:       perl-Algorithm-CheckDigits
Version:    1.3.6
Release:    13%{?dist}

Summary:    Perl extension to generate and test check digits

# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Algorithm-CheckDigits
Source0:    https://cpan.metacpan.org/authors/id/M/MA/MAMAWE/Algorithm-CheckDigits-v%{version}.tar.gz

BuildArch:  noarch
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(integer)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
# Tests
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More)
# Optional tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
BuildRequires:  perl(Test::Version)

%description
This module provides a number of methods to test and generate check digits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-CheckDigits-v%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes README
%{_bindir}/checkdigits.pl
%{perl_vendorlib}/*
%{_mandir}/man1/checkdigits.pl.1.*
%{_mandir}/man3/Algorithm::CheckDigits*3pm.*

%changelog
%autochangelog
