%global source0_hash 96a94d2cc690c1fa8fd34113e3b084bf2a469a323a9780285aef92ddc381e63a
Name:           perl-DBIx-Introspector
Version:        0.001005
Release:        20%{?dist}
Summary:        Detect what database you are connected to
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Introspector
Source0:        https://cpan.metacpan.org/authors/id/F/FR/FREW/DBIx-Introspector-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DBI::Const::GetInfoType) >= 1.628
Provides:       perl(DBIx::Introspector::Driver) = %{version}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBI::Const::GetInfoType)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Roo)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::Introspector is a module factored out of the DBIx::Class database
detection code. Most code that needs to detect which database it is
connected to assumes that there is a one-to-one mapping from database
drivers to database engines. Unfortunately reality is rarely that simple.
For instance, DBD::ODBC is typically used to connect to SQL Server, but
ODBC can be used to connect to PostgreSQL, MySQL, and Oracle. Additionally,
while ODBC is the most common way to connect to SQL Server, it is not the
only option, as DBD::ADO can also be used.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Introspector-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
