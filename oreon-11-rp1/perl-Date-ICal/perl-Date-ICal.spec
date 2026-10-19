%global source0_hash 9e876e9007bb7c3c4852ab76c90f055c9d0735b5ac494ca087be4f7e38955d2d
Name:           perl-Date-ICal
Version:        2.682
Release:        1%{?dist}
Summary:        Perl extension for ICalendar date objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Date-ICal
Source0:        https://cpan.metacpan.org/modules/by-module/Date/Date-ICal-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Date::Leapyear) >= 1.03
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Date::Leapyear\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Date::Leapyear)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(integer)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Date::ICal talks the ICal date format, and is intended to be a base class
for other date/calendar modules that know about ICal time format also.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-ICal-%{version}
chmod a-x lib/Date/ICal.pm

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
