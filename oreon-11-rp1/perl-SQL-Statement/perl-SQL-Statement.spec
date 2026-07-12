%global source0_hash dde8bdcfa6a136eedda06519ba0f3efaec085c39db0df9c472dc0ec6cd781a49

Name:           perl-SQL-Statement
Version:        1.414
Release:        17%{?dist}
Summary:        SQL parsing and processing engine
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/SQL-Statement
Source0:        https://cpan.metacpan.org/authors/id/R/RE/REHSACK/SQL-Statement-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone) >= 0.30
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI) >= 1.616
BuildRequires:  perl(Encode)
BuildRequires:  perl(Errno)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Math::Base::Convert)
BuildRequires:  perl(Math::Trig)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Scalar::Util) >= 1.0
# XXX: BuildRequires:  perl(SQL::UserDefs)
BuildRequires:  perl(sort)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Text::Soundex)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
# Optional tests only
# DBD::CSV buildrequires SQL::Statement
%if 0%{!?perl_bootstrap:1}
BuildRequires:  perl(DBD::CSV) >= 0.30
%endif
BuildRequires:  perl(DBD::DBM) >= 0.06
BuildRequires:  perl(DBD::File) >= 0.40
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(MLDBM)
Requires:       perl(Clone) >= 0.30
Requires:       perl(DBI) >= 1.616
Requires:       perl(Math::Base::Convert)
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(Scalar::Util) >= 1.0
# This module doesn't seem to exist...
# XXX: Requires:       perl(SQL::UserDefs)
Requires:       perl(Text::Soundex)

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((Clone|Params::Util|Scalar::Util)\\)$

Provides:       perl(SQL::Statement)
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

%check
make test

%files
%license ARTISTIC-1.0 GPL-1 GPL-2.0 LICENSE
%doc Changes README README.md
%{perl_vendorlib}/SQL/
%{_mandir}/man3/*.3pm*

%changelog
%autochangelog
