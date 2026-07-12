%global source0_hash cbc1e9b35a05e71febc13e5ef547a31c8249899bb6011dbdc9d9ff366ddab6c2

Name:           perl-Test-SubCalls
Version:        1.10
Release:        24%{?dist}
Summary:        Track the number of times subs are called
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-SubCalls
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-SubCalls-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Hook::LexWrap) >= 0.20
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More) >= 0.42
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Test::Builder::Tester)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Dependencies
# (none)

Provides:       perl(Test::SubCalls)
%description
There are a number of different situations (like testing caching code) where
you want to want to do a number of tests, and then verify that some underlying
subroutine deep within the code was called a specific number of times. This
module provides a number of functions for doing testing in this way, in
association with your normal Test::More (or similar) test scripts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-SubCalls-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::SubCalls.3*

%changelog
%autochangelog
