%global source0_hash a807fe3ffbb84ffa5396711acce75764f3a49f24236467350c71c8a77a5c3ec2

Summary: 	Calculate business hours in a time period
Name: 		perl-Business-Hours
Version: 	0.13
Release: 	22%{?dist}
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Business-Hours

Source0: https://cpan.metacpan.org/authors/id/B/BP/BPS/Business-Hours-%{version}.tar.gz
BuildArch: 	noarch

Requires:  perl(Set::IntSpan) >= 1.12

BuildRequires:	%{__perl}
BuildRequires:	%{__make}

BuildRequires:	perl-interpreter
BuildRequires:	perl-generators
BuildRequires:	perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:	perl(Set::IntSpan) >= 1.12
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl(warnings)
# Required by the tests
BuildRequires:	perl(Test::More)
# Optional tests:
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Set::IntSpan\\)$

%description
A simple tool for calculating business hours in a time period. Over time, 
additional functionality will be added to make it easy to calculate the 
number of business hours between arbitrary dates.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Business-Hours-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/Business
%{_mandir}/man3/*

%changelog
%autochangelog
