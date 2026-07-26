%global source0_hash f655e0ab88907a82382e7f1e05e55c763846077baab30b39832e52fbd7839aa3

Name:    postgresqltuner
Version: 1.0.1
Release: %autorelease
Summary: Simple script to analyze PostgreSQL database configuration and tuning

# Automatically converted from old format: GPLv3 - review is highly recommended.
License: GPL-3.0-only
URL:     https://github.com/jfcoz/postgresqltuner/
Source0: https://github.com/jfcoz/postgresqltuner/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch: noarch

Requires: perl(DBI)
Requires: perl(DBD::Pg)
Requires: perl(Getopt::Long)
Requires: perl(Term::ANSIColor)

BuildRequires: postgresql-test-rpm-macros
BuildRequires: perl(DBI)
BuildRequires: perl(DBD::Pg)
BuildRequires: perl(Getopt::Long)
BuildRequires: perl(Term::ANSIColor)

%description
postgresqltuner is a simple script to analyze your PostgreSQL database. It is 
inspired by mysqltuner.pl

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%install
mkdir -p %{buildroot}/%{_bindir}
cp -a postgresqltuner.pl %{buildroot}%{_bindir}/postgresqltuner

%check
%postgresql_tests_run
%{buildroot}%{_bindir}/postgresqltuner --host=$PGHOST --port=$PGPORT --database=mockbuild --user=mockbuild --password=mockbuild

%files
%{_bindir}/postgresqltuner

%doc README.md README.fr.md
%license LICENSE.txt

%changelog
%autochangelog
