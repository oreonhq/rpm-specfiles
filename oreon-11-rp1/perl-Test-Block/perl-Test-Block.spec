%global source0_hash 3dd81b5aafba85b097985faa071886ec55749732fb49c55669d8b0fc0d1d391b

Name:       perl-Test-Block
Version:    0.13
Release:    39%{?dist}
# see lib/Test/Block.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Specify fine granularity test plans
Source:     https://cpan.metacpan.org/authors/id/A/AD/ADIE/Test-Block-%{version}.tar.gz
Url:        https://metacpan.org/release/Test-Block
BuildArch:  noarch
# Fixed Test-Block-0.13 for perl 5.23.8 and later (CPAN RT#112462)
Patch0:     Test-Block-0.13-Make-Test-Block-work-with-perl-5.23.8.patch

BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-interpreter
BuildRequires: perl-generators
BuildRequires: perl(ExtUtils::MakeMaker)
# Run-time
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter)
BuildRequires: perl(overload)
BuildRequires: perl(Scalar::Util)
BuildRequires: perl(strict)
BuildRequires: perl(Test::Builder) >= 0.17
BuildRequires: perl(Tie::Scalar)
BuildRequires: perl(Tie::StdScalar)
BuildRequires: perl(warnings)
# Tests
BuildRequires: perl(Test::Builder::Tester) >= 1.01
BuildRequires: perl(Test::Exception) >= 0.15
BuildRequires: perl(Test::More) >= 0.47

%description
This module allows you to specify the number of expected tests at a finer
level of granularity than an entire test script. It is built with
Test::Builder and plays happily with Test::More and friends.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Block-%{version}
%patch -P0 -p2

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
