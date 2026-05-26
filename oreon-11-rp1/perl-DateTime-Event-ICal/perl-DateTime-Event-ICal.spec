Name:           perl-DateTime-Event-ICal
Version:        0.13
Release:        29%{?dist}
Summary:        Perl DateTime extension for computing rfc2445 recurrences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Event-ICal
Source0:        https://cpan.metacpan.org/authors/id/F/FG/FGLOCK/DateTime-Event-ICal-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 53da4384ef5cf30ee87dc0131f4b6eee2121cc0eba347162a328b9bcfaf475ea
%global source0_file DateTime-Event-ICal-0.13.tar.gz
# oreon url source checksums end
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Event::Recurrence) >= 0.11
BuildRequires:  perl(DateTime::Set)
BuildRequires:  perl(DateTime::Span)
BuildRequires:  perl(DateTime::SpanSet)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Params::Validate)
BuildRequires:  perl(vars)
# Test suite
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
# Runtime

%description
This module provides convenience methods that let you easily create
DateTime::Set objects for rfc2445 style recurrences.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/DateTime-Event-ICal-0.13.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "53da4384ef5cf30ee87dc0131f4b6eee2121cc0eba347162a328b9bcfaf475ea" || { echo "oreon: Source0 SHA256 mismatch for DateTime-Event-ICal-0.13.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n DateTime-Event-ICal-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13-29
- Prepare for Oreon 11 (RP1)
