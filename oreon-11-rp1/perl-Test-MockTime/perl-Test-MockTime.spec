%global source0_hash 3363e118b2606f1d6abc956f22b0d09109772b7086155fb5c9c7f983350602f9

Name:           perl-Test-MockTime
Version:        0.17
Release:        24%{?dist}
Summary:        Replaces actual time with simulated time
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-MockTime
Source0:        https://cpan.metacpan.org/authors/id/D/DD/DDICK/Test-MockTime-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::Local)
BuildRequires:  perl(Time::Piece) >= 1.08
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# for improved tests
BuildRequires:  perl(Test::Pod) >= 1.00

Requires:       perl(Time::Piece) >= 1.08

%description
This module was created to enable test suites to test code at specific
points in time. Specifically it overrides localtime, gmtime and time at
compile time and then relies on the user supplying a mock time via
set_relative_time, set_absolute_time or set_fixed_time to alter future
calls to gmtime,time or localtime.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-MockTime-%{version}

# fix up broken permissions
chmod -x lib/Test/MockTime.pm t/test.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
