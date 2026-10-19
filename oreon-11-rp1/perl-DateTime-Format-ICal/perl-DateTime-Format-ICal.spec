%global source0_hash 8b09f6539f5e9c0df0e6135031699ed4ef9eef8165fc80aefeecc817ef997c33
Name:           perl-DateTime-Format-ICal
Version:        0.09
Release:        1%{?dist}
Summary:        Parse and format iCal datetime and duration strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-ICal
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ICal-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DateTime) >= 0.17
Requires:       perl(DateTime::Event::ICal) >= 0.03
Requires:       perl(DateTime::Set) >= 0.1
Requires:       perl(DateTime::TimeZone) >= 0.22
Requires:       perl(Params::Validate) >= 0.59
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DateTime::Event::ICal\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Validate\\)$
Provides:       perl(DateTime::Format::ICal)
# oreon:deps
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Event::ICal)
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(DateTime::TimeZone)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n DateTime-Format-ICal-%{version}

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-48
- Prepare for Oreon 11 (RP1)
