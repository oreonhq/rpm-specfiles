%global source0_hash 4f09674d7a2888b8c621f32b7b104aba80b7c88ae83b4855c712d31e49a532f5

Name:           perl-DBIx-QueryLog
Version:        0.42
Release:        22%{?dist}
Summary:        Logging queries for DBI
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-QueryLog

Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAICRON/DBIx-QueryLog-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Run-time
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Text::ASCIITable)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)

# Testing
BuildRequires:  perl(base)
BuildRequires:  perl(Benchmark)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::mysqld)
BuildRequires:  perl(Test::PostgreSQL)
BuildRequires:  perl(Test::Requires)

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
# don't install benchmark suite
rm -rf $RPM_BUILD_ROOT/%{_bindir}

find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%license LICENSE
%doc Changes README.md script/
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
