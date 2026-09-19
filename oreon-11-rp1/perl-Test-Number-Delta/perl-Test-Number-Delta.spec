%global source0_hash 535430919e6fdf6ce55ff76e9892afccba3b7d4160db45f3ac43b0f92ffcd049

Name:           perl-Test-Number-Delta
Version:        1.06
Release:        33%{?dist}
Summary:        Compare the difference between numbers against a given tolerance
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Number-Delta
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Number-Delta-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Builder::Tester) >= 1.02
BuildRequires:  perl(Test::More)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies

%description
At some point or another, most programmers find they need to compare
floating-point numbers for equality. The typical idiom is to test if
the absolute value of the difference of the numbers is within a
desired tolerance, usually called epsilon. This module provides such
a function for use with Test::Harness.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Number-Delta-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Number::Delta.3*

%changelog
%autochangelog
