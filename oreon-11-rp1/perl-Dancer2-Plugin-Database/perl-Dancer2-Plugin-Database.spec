%global source0_hash 431f3405413366d2f36ebe0fd4661cc6d3c1354ba46018484799c0757dc638bd
Name:           perl-Dancer2-Plugin-Database
Version:        2.17
Release:        1%{?dist}
Summary:        Easy database connections for Dancer2 applications
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            http://metacpan.org/release/Dancer2-Plugin-Database/
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Dancer2-Plugin-Database-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Dancer2)
BuildRequires:  perl(Dancer2::Plugin)
BuildRequires:  perl(Dancer::Plugin::Database::Core)
BuildRequires:  perl(Dancer::Plugin::Database::Core::Handle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTTP::Request::Common)
BuildRequires:  perl(Plack::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Dancer2::Plugin::Database provides an easy way to obtain a connected
DBI database handle by simply calling the database keyword within
your Dancer2 application

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer2-Plugin-Database-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
