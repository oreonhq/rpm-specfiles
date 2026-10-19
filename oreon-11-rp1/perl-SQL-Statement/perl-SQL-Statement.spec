%global source0_hash dde8bdcfa6a136eedda06519ba0f3efaec085c39db0df9c472dc0ec6cd781a49
%{?!oreon_bootstrap:%global oreon_bootstrap %{nil}}
%oreon_bootstrap
Name:           perl-SQL-Statement
Version:        1.414
Release:        1%{?dist}
Summary:        SQL parsing and processing engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Statement
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/SQL-Statement-%{version}.tar.gz
BuildArch:      noarch
%if 0%{!?perl_bootstrap:1}
%endif
Requires:       perl(Clone) >= 0.30
Requires:       perl(DBI) >= 1.616
Requires:       perl(Math::Base::Convert)
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Scalar::Util) >= 1.0
Requires:       perl(Text::Soundex)
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Clone|Params::Util|Scalar::Util)\\)$
Provides:       perl(SQL::Statement)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBD::CSV)
BuildRequires:  perl(DBD::DBM)
BuildRequires:  perl(DBD::File)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(MLDBM)
BuildRequires:  perl(Math::Base::Convert)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::Soundex)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(sort)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The SQL::Statement module implements a pure Perl SQL parsing and execution
engine.  While it by no means implements full ANSI standard, it does support
many features including column and table aliases, built-in and user-defined
functions, implicit and explicit joins, complexly nested search conditions, and
other features.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n SQL-Statement-%{version}
find -type f -exec chmod a-x {} +
perl -pi -e 's/\r//go' README

%build

export SQL_STATEMENT_WARN_UPDATE=sure
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
