%global source0_hash 48c9cca9f7d99eee741176445b431adf09c029e1aa57c4703c9f46f7601d40d4
Name:           perl-Test-Pod-Coverage
Version:        1.10
Release:        32%{?dist}
Summary:        Check for pod coverage in your distribution
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Pod-Coverage
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Test-Pod-Coverage-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(Test::Pod::Coverage)
Provides:       perl(Test::Pod::Coverage::TrustMe)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Pod::Coverage::CountParents)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Pod::Coverage is used to create a test for your distribution, to
ensure that all relevant files in your distribution are appropriately
documented in pod.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Pod-Coverage-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.10-32
- Prepare for Oreon 11 (RP1)
