%global source0_hash fbda92d37e0481d18eebc81e48d025228b57184c59b2d5a6f6bdf87042e8c7b2

Name:           perl-Test-Exit
Version:        0.11
Release:        25%{?dist}
Summary:        Test that some code calls exit without terminating testing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Exit
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARODLAND/Test-Exit-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Return::MultiLevel)
# Test::Builder::Module version from Test::Builder in META
BuildRequires:  perl(Test::Builder::Module) >= 0.86
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
# Pod::Coverage::TrustPod not used
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Test::Builder::Module version from Test::Builder in META
Requires:       perl(Test::Builder::Module) >= 0.86

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::Builder::Module\\)$

%description
Test::Exit Perl module provides some simple tools for testing code that might
call exit(), providing you with the status code without exiting the test file.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Exit-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
