%global source0_hash 30d90f54ce840893c7ba2cac2a4d1eecd4c9cdf805910c595e3ae89dfd644738

Name:           perl-Test-Time
Version:        0.092
Release:        11%{?dist}
Summary:        Overrides the time() and sleep() core functions for testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Test-Time
Source0:        https://cpan.metacpan.org/authors/id/A/AN/ANATOFUZ/Test-Time-%{version}.tar.gz

BuildArch:      noarch

# Spec file requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  sed

# The module itself
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Name::FromLine)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

%{?perl_default_filter}

%description
Test::Time can be used to test modules that deal with time. Once you use
this module, all references to time and sleep will be internalized. You can
set custom time by passing time => number after the use statement.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Time-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
