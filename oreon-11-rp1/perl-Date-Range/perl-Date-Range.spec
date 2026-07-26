%global source0_hash bf9897492b101c0503879d14a7e7ebe902544383601ae7c69a95de75cbd948b9

Name:		perl-Date-Range
Version:	1.41
Release:	13%{?dist}
License:	GPL-2.0-or-later
Summary:	Work with a range of dates
URL:		https://metacpan.org/release/Date-Range
Source0:	https://cpan.metacpan.org/modules/by-module/Date/Date-Range-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Date::Simple) >= 0.03
BuildRequires:	perl(strict)
# Test Suite
BuildRequires:	perl(Test::More) >= 0.04
# Optional Tests
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
# Dependencies
Requires:	perl(Date::Simple) >= 0.03

%description
Quite often, when dealing with dates, we don't just want to know information
about one particular date, but about a range of dates. For example, we may
wish to know whether a given date is in a particular range, or what the overlap
is between one range and another. This module lets you ask such questions.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Date-Range-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Date/
%{_mandir}/man3/Date::Range.3*

%changelog
%autochangelog
