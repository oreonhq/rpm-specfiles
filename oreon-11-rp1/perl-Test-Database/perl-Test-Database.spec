%global source0_hash b29fc4b709afebd07ee981c98d1db7aac37df71f679f986b83e472f4a26a80e9

Name:           perl-Test-Database
Version:        1.113
Release:        31%{?dist}
Summary:        Database handles ready for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Database
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOOK/Test-Database-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::DBM)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(version)
BuildRequires:  perl(YAML::Tiny) >= 1.62
# Recommended run-time:
# DBD::CSV 0.30 not used at tests
BuildRequires:  perl(DBD::SQLite) >= 1.27
# Tests:
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::Util)
# Pod::Coverage::TrustPod not used
# SQL::Statement not needed
# Test::CPAN::Meta not used
BuildRequires:  perl(Test::More) >= 0.88
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
Requires:       perl(YAML::Tiny) >= 1.62

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(YAML::Tiny\\)$

%description
Test::Database Perl module provides a simple way for test authors to request
a test database, without worrying about environment variables or the test host
configuration.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Database-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
