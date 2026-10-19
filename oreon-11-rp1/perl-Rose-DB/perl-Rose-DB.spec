%global source0_hash 3d42a89eeb1f519b54c3fd7bd1be44863fa573677795289ee869006b44575099
Name:		perl-Rose-DB
Version:	0.786
Release:        1%{?dist}
Summary:        DBI wrapper and abstraction layer
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Rose-DB
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSIRACUSA/Rose-DB-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Bit::Vector::Overload)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone::PP)
BuildRequires:  perl(Config)
BuildRequires:  perl(DBD::MariaDB)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DateTime::Duration)
BuildRequires:  perl(DateTime::Format::MySQL)
BuildRequires:  perl(DateTime::Format::Oracle)
BuildRequires:  perl(DateTime::Format::Pg)
BuildRequires:  perl(DateTime::Infinite)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Rose::DateTime::Util)
BuildRequires:  perl(Rose::Object)
BuildRequires:  perl(SQL::ReservedWords)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::Clock)
BuildRequires:  perl(YAML)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Rose::DB is a wrapper and abstraction layer for DBI-related functionality.
A Rose::DB object "has a" DBI object; it is not a subclass of DBI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Rose-DB-%{version}

%build

find . -type f -executable -exec chmod -x {} \;
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

export AUTOMATED_TESTING=1
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
