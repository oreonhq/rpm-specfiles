Name:           perl-DateTime-Event-Recurrence
Version:        0.19
Release:        26%{?dist}
Summary:        DateTime::Set extension for create basic recurrence sets
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Event-Recurrence
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-Recurrence-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtimea
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime) >= 0.27
BuildRequires:  perl(DateTime::Set) >= 0.3600
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(integer)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(DateTime::SpanSet)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(DateTime) >= 0.27
Requires:       perl(DateTime::Set) >= 0.3600

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime::Set\\)$

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for various recurrences, such as "once a month" or
"every day". You can also create more complicated recurrences, such as
"every Monday, Wednesday and Thursday at 10:00 AM and 2:00 PM".

%prep
%setup -q -n DateTime-Event-Recurrence-%{version}

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
%doc Changes CREDITS README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.19-26
- Prepare for Oreon 11 (RP1)
