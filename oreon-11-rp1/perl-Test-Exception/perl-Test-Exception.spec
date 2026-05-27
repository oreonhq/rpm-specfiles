%global source0_hash 156b13f07764f766d8b45a43728f2439af81a3512625438deab783b7883eb533

Name:           perl-Test-Exception
Version:        0.43
Release:        30%{?dist}
Summary:        Library of test functions for exception based Perl code
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Exception
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test-Exception-0.43.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Uplevel) >= 0.18
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(overload)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
# Dependencies
Requires:       perl(Carp)

# Avoid bogus perl(DB) provide
%{?perl_default_filter}

%description
This module provides a few convenience methods for testing exception
based code. It is built with Test::Builder and plays happily with
Test::More and friends.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n Test-Exception-%{version}

# Remove unnecessary exec permissions
chmod -c -x Changes

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
%doc Changes
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Exception.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.43-30
- Prepare for Oreon 11 (RP1)
