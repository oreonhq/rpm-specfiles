%global source0_hash cdde3d22b1affa7df6b1e12b2a52e9f3c1b681c8b593a1be4de3be68e4da5c72
Name:           perl-Minion-Backend-SQLite
Version:        5.0.7
Release:        10%{?dist}
Summary:        SQLite backend for Minion job queue
License:        Artistic-2.0
URL:            https://metacpan.org/release/Minion-Backend-SQLite/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Minion-Backend-SQLite-v%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Minion)
BuildRequires:  perl(Minion::Backend)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Mojo::SQLite)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Minion::Backend::SQLite is a backend for Minion based on Mojo::SQLite. All
necessary tables will be created automatically with a set of migrations
named minion. If no connection string or :temp: is provided, the database
will be created in a temporary directory.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Minion-Backend-SQLite-v%{version}

%build

/usr/bin/perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
