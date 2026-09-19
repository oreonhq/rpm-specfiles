%global source0_hash ed8baa31cd388c82fd378ac375502f18e5276d7811b6e91f903898ec227fdf21

Name:           perl-Mojo-Pg
Version:        4.28
Release:        2%{?dist}
Summary:        Mojolicious ♥ PostgreSQL
License:        Artistic-2.0

URL:            https://metacpan.org/release/Mojo-Pg
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/Mojo-Pg-%{version}.tar.gz

BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(Mojolicious) >= 8.50
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::Pg) >= 3.7.4
BuildRequires:  perl(DBI)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Collection)
BuildRequires:  perl(Mojo::EventEmitter)
BuildRequires:  perl(Mojo::File)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::JSON)
BuildRequires:  perl(Mojo::Loader)
BuildRequires:  perl(Mojo::Promise)
BuildRequires:  perl(Mojo::URL)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(SQL::Abstract::Pg) >= 1.0
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(constant)
# Tests
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
Requires:       perl(SQL::Abstract) >= 1.85

%{?perl_default_filter}

%description
Mojo::Pg is a tiny wrapper around DBD::Pg that makes PostgreSQL a lot of
fun to use with the Mojolicious real-time web framework. Perform queries
blocking and non-blocking, use all SQL features PostgreSQL has to offer,
generate CRUD queries from data structures, manage your database schema
with migrations and build scalable real-time web applications with the
publish/subscribe pattern.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Mojo-Pg-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build} %{?_smp_mflags}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README.md
%license LICENSE
%{perl_vendorlib}/Mojo*
%{_mandir}/man3/Mojo*

%changelog
%autochangelog
