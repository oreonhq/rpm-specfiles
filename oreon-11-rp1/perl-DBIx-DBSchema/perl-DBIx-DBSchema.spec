%global source0_hash eeee210dc14a8d63eb01ac2d66c67a1dc279f9289be96a61724c8951791c5212

Name:           perl-DBIx-DBSchema
Version:        0.47
Release:        10%{?dist}
Summary:        Database-independent schema objects

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-DBSchema
Source0:	https://cpan.metacpan.org/authors/id/I/IV/IVAN/DBIx-DBSchema-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:	%{__make}
BuildRequires:	perl-generators

BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:	perl(DBI)
BuildRequires:  perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(FreezeThaw)
BuildRequires:  perl(Storable)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Required by the tests
BuildRequires:  perl(Test::More)
BuildRequires:	perl(DBD::Pg) >= 1.41

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

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
