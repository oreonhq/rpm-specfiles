%global source0_hash 3dd81b5aafba85b097985faa071886ec55749732fb49c55669d8b0fc0d1d391b
Name:       perl-Test-Block
Version:    0.13
Release:        39%{?dist}
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Specify fine granularity test plans
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADIE/Test-Block-%{version}.tar.gz
Url:        https://metacpan.org/release/Test-Block
BuildArch:  noarch
Patch0:     Test-Block-0.13-Make-Test-Block-work-with-perl-5.23.8.patch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Tie::Scalar)
BuildRequires:  perl(Tie::StdScalar)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
