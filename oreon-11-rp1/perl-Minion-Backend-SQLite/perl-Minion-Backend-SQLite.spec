%global source0_hash cdde3d22b1affa7df6b1e12b2a52e9f3c1b681c8b593a1be4de3be68e4da5c72

Name:           perl-Minion-Backend-SQLite
Version:        5.0.7
Release:        10%{?dist}
Summary:        SQLite backend for Minion job queue
License:        Artistic-2.0

URL:            https://metacpan.org/release/Minion-Backend-SQLite/
Source0:        https://cpan.metacpan.org/authors/id/D/DB/DBOOK/Minion-Backend-SQLite-v%{version}.tar.gz

BuildArch:      noarch
# build deps
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::SQLite) >= 3.000
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(strict)
# test deps
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Minion) >= 9.0
BuildRequires:  perl(Minion::Backend)
BuildRequires:  perl(Module::Metadata)
BuildRequires:  perl(Mojo::IOLoop)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(constant)

%{?perl_default_filter}

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

%check
./Build test

%files
%doc Changes CONTRIBUTING.md examples README
%license LICENSE
%{perl_vendorlib}/Minion*
%{_mandir}/man3/Minion*

%changelog
%autochangelog
