%global source0_hash 53da4384ef5cf30ee87dc0131f4b6eee2121cc0eba347162a328b9bcfaf475ea
Name:           perl-DateTime-Event-ICal
Version:        0.13
Release:        1%{?dist}
Summary:        Perl DateTime extension for computing rfc2445 recurrences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Event-ICal
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
BuildArch:      noarch
Provides:       perl(DateTime::Event::ICal)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Event::Recurrence)
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(DateTime::SpanSet)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides convenience methods that let you easily create
DateTime::Set objects for rfc2445 style recurrences.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Event-ICal-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13-29
- Prepare for Oreon 11 (RP1)
