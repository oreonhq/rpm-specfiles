%global source0_hash 4f09674d7a2888b8c621f32b7b104aba80b7c88ae83b4855c712d31e49a532f5
Name:           perl-DBIx-QueryLog
Version:        0.42
Release:        22%{?dist}
Summary:        Logging queries for DBI
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-QueryLog
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/DBIx-QueryLog-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::PostgreSQL)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::mysqld)
BuildRequires:  perl(Text::ASCIITable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
DBIx::QueryLog logs each execution time and the actual query.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-QueryLog-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
rm -rf $RPM_BUILD_ROOT/%{_bindir}
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
