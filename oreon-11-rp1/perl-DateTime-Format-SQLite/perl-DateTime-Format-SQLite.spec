%global source0_hash cc1f4e0ae1d39b0d4c3dddccfd7423c77c67a70950c4b5ecabf8ca553ab294b4

Name:           perl-DateTime-Format-SQLite 
Summary:        Parse and format SQLite dates and times 
Version:        0.11
Release:        45%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/DateTime-Format-SQLite-%{version}.tar.gz 
URL:            https://metacpan.org/release/DateTime-Format-SQLite
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(DateTime::Format::Builder) >= 0.6
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(DateTime) >= 0.10
BuildRequires:  perl(Test::More)
Requires:       perl(DateTime::Format::Builder) >= 0.6

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(DateTime::Format::Builder\\)$

%description
This module understands the formats used by SQLite for its 'date',
'datetime' and 'time' functions. It can be used to parse these formats
in order to create the DateTime manpage objects, and it can take a
DateTime object and produce a timestring accepted by SQLite.*NOTE:*
SQLite does not have real date/time types but stores everything as
strings. This module deals with the date/time strings as
understood/returned by SQLite's 'date', 'time', 'datetime', 'julianday'
and 'strftime' SQL functions. You will usually want to store your dates
in one of these formats.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-SQLite-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
