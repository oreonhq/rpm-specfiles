# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 8b09f6539f5e9c0df0e6135031699ed4ef9eef8165fc80aefeecc817ef997c33
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           perl-DateTime-Format-ICal
Version:        0.09
Release:        48%{?dist}
Summary:        Parse and format iCal datetime and duration strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-ICal
Source0:        https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-Format-ICal-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(DateTime) >= 0.17
BuildRequires:  perl(DateTime::Event::ICal) >= 0.03
BuildRequires:  perl(DateTime::Set) >= 0.1
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(DateTime::TimeZone) >= 0.22
BuildRequires:  perl(Params::Validate) >= 0.59
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Test::More)
Requires:       perl(DateTime) >= 0.17
Requires:       perl(DateTime::Event::ICal) >= 0.03
Requires:       perl(DateTime::Set) >= 0.1
Requires:       perl(DateTime::TimeZone) >= 0.22
Requires:       perl(Params::Validate) >= 0.59

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %__requires_exclude|^perl\\(DateTime::Event::ICal\\)$
%global __requires_exclude %__requires_exclude|^perl\\(Params::Validate\\)$

%description
This module understands the ICal date/time and duration formats, as defined
in RFC 2445. It can be used to parse these formats in order to create the
appropriate objects.

%prep
%oreon_verify_sources
%setup -q -n DateTime-Format-ICal-%{version}

%build
perl Build.PL installdirs=vendor
./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*

%check
./Build test

%files
%license LICENSE
%doc Changes TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-48
- Prepare for Oreon 11 (RP1)
