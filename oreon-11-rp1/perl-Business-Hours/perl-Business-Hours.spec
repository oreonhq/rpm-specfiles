%global source0_hash a807fe3ffbb84ffa5396711acce75764f3a49f24236467350c71c8a77a5c3ec2
Summary:        Calculate business hours in a time period
Name: 		perl-Business-Hours
Version: 	0.13
Release:        1%{?dist}
License: 	GPL-1.0-or-later OR Artistic-1.0-Perl
URL: 		https://metacpan.org/release/Business-Hours
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/Business-Hours-%{version}.tar.gz
BuildArch: 	noarch
Requires:  perl(Set::IntSpan) >= 1.12
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Set::IntSpan\\)$
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Set::IntSpan)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
