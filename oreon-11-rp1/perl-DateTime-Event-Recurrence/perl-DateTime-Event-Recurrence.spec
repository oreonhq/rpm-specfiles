%global source0_hash f9408789a461107766ca1a232bb3ec1e702eec7ca8167401ea6ec3f4b6d0b5a5
Name:           perl-DateTime-Event-Recurrence
Version:        0.19
Release:        26%{?dist}
Summary:        DateTime::Set extension for create basic recurrence sets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Event-Recurrence
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-Recurrence-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DateTime) >= 0.27
Requires:       perl(DateTime::Set) >= 0.3600
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime::Set\\)$
Provides:       perl(DateTime::Event::Recurrence)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(DateTime::SpanSet)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides convenience methods that let you easily create
DateTime::Set objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Event-Recurrence-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19-26
- Prepare for Oreon 11 (RP1)
