%global source0_hash 5739a9af3fc0fc162b38032df610a070035263bfbe0bec16aec52f0dddd7b647

Name:           perl-Mojo-SQLite
Version:        3.009
Release:        12%{?dist}
Summary:        Tiny Mojolicious wrapper for SQLite
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojo-SQLite/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Mojo-SQLite-%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# run deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite) >= 1.68
BuildRequires:  perl(DBI) >= 1.627
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(SQL::Abstract::Pg)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# test deps
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(URI) >= 1.69
BuildRequires:  perl(URI::db) >= 0.15
BuildRequires:  perl(URI::file) >= 4.21

%{?perl_default_filter}

%description
Mojo::SQLite is a tiny wrapper around DBD::SQLite that makes SQLite a lot
of fun to use with the Mojolicious real-time web framework. Use all SQL
features SQLite has to offer, generate CRUD queries from data structures,
and manage your database schema with migrations.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojo-SQLite-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 ./Build test

%files
%doc Changes CONTRIBUTING.md README
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
%autochangelog
