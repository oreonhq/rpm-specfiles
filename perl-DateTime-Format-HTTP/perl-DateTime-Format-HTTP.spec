Name:           perl-DateTime-Format-HTTP
Version:        0.43
Release:        4%{?dist}
Summary:        HTTP protocol date conversion routines
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-HTTP
Source0:        https://cpan.metacpan.org/modules/by-module/DateTime/DateTime-Format-HTTP-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DateTime) >= 0.17
BuildRequires:  perl(HTTP::Date) => 1.44
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 0.47
# Dependencies
Requires:       perl(DateTime) >= 0.17
Requires:       perl(HTTP::Date) >= 1.44

# Filter underspecified dependencies
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(DateTime\\)$
%global __requires_exclude %{?__requires_exclude|%__requires_exclude|}^perl\\(HTTP::Date\\)$

%description
This module provides functions that deal with the date formats used by the
HTTP protocol (and then some).

%prep
%setup -q -n DateTime-Format-HTTP-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes CREDITS README
%{perl_vendorlib}/DateTime/
%{_mandir}/man3/DateTime::Format::HTTP.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.43-4
- Prepare for Oreon 11 (RP1)
