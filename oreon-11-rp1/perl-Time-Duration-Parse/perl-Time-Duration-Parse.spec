%global source0_hash 1084a6463ee2790f99215bd76b135ca45afe2bfa6998fa6fd5470b69e1babc12

Name:       perl-Time-Duration-Parse
Version:    0.16
Release:    14%{?dist}
# see lib/Time/Duration/Parse.pm
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:    Parse string that represents time duration
Source:     https://cpan.metacpan.org/authors/id/N/NE/NEILB/Time-Duration-Parse-%{version}.tar.gz
Url:        https://metacpan.org/release/Time-Duration-Parse
BuildArch:  noarch

BuildRequires: %{__perl}
BuildRequires: %{__make}

BuildRequires: perl-generators
BuildRequires: perl(Carp)
BuildRequires: perl(Exporter) >= 5.57
BuildRequires: perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires: perl(Test::More) >= 0.88
BuildRequires: perl(strict)
BuildRequires: perl(warnings)
# optional tests
BuildRequires: perl(Time::Duration)


Provides:       perl(Time::Duration::Parse)
%description
Time::Duration::Parse is a module to parse human readable duration strings
like "2 minutes and 3 seconds" to seconds. It does the opposite of
duration_exact() in Time::Duration and is roundtrip safe.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Time-Duration-Parse-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="%{buildroot}"
%{_fixperms} %{buildroot}/*

%check
%{__make} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
