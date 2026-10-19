%global source0_hash eeee210dc14a8d63eb01ac2d66c67a1dc279f9289be96a61724c8951791c5212
Name:           perl-DBIx-DBSchema
Version:        0.47
Release:        1%{?dist}
Summary:        Database-independent schema objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-DBSchema
Source0:        https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FreezeThaw)
BuildRequires:  perl(Storable)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
# /oreon:deps
%description
DBIx::DBSchema objects are collections of DBIx::DBSchema::Table objects and 
represent a database schema.

This module implements an OO-interface to database schemas. Using this module, 
you can create a database schema with an OO Perl interface. You can read the
schema from an existing database. You can save the schema to disk and restore
it a different process. Most importantly, DBIx::DBSchema can write SQL CREATE
statements statements for different databases from a single source.

Currently supported databases are MySQL and PostgreSQL. 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-DBSchema-%{version}
find -name '*.pm' -exec chmod -x {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
