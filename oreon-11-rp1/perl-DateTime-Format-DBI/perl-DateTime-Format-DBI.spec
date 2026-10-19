%global source0_hash 7e7d3e4b463321c17c299b71f36592580339205e93e583946857cb975bcc7a4d
Name:           perl-DateTime-Format-DBI
Version:        0.041
Release:        1%{?dist}
Summary:        Find a parser class for a database connection
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DateTime-Format-DBI
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFAERBER/DateTime-Format-DBI-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DateTime::Format::DB2)
Requires:       perl(DateTime::Format::MySQL)
Requires:       perl(DateTime::Format::Pg)
Requires:       perl(DateTime::Format::SQLite)
# oreon:deps
BuildRequires:  //bin/iconv
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DateTime)
BuildRequires:  perl(DateTime::Format::SQLite)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module finds a DateTime::Format::* class that is suitable for the use
with a given DBI connection (and DBD::* driver).

Note that this is most useful if you actually have the DateTime::Format::*
class for your particular database(s) installed!  See, e.g.,
perl-DateTime-MySQL, perl-DateTime-Oracle, perl-DateTime-DB2, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DateTime-Format-DBI-%{version}
iconv -f ISO-8859-1 -t UTF-8 LICENSE > LICENSE.utf && \
touch -r LICENSE LICENSE.utf && \
mv -f LICENSE.utf LICENSE

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
