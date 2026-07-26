%global source0_hash 32f5aec3ebc77ce939bb762c1ea81a04d4d589ac2b4166b454b48f8a97cf5437

Name:           perl-HTML-CalendarMonthSimple
Version:        1.27
Release:        3%{?dist}
Summary:        Perl Module for Generating HTML Calendars
License:        BSD-3-Clause
URL:            https://metacpan.org/release/HTML-CalendarMonthSimple
Source0:        https://cpan.metacpan.org/modules/by-module/HTML/HTML-CalendarMonthSimple-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Date::Calc)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test
BuildRequires:  perl(Test::More)

%description
HTML::CalendarMonthSimple is a Perl module for generating, manipulating,
and printing a HTML calendar grid for a specified month. It is intended as
a faster and easier-to-use alternative to HTML::CalendarMonth.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-CalendarMonthSimple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
%make_build

%install
%make_install
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc README.md Changes
%license LICENSE
%{perl_vendorlib}/HTML/
%{_mandir}/man3/HTML::CalendarMonthSimple.3pm*

%changelog
%autochangelog
