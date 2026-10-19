%global source0_hash ad108f1b1b968d112e6f46ceac9e8493b02b40f4a91cad8fdb0bf5c381547716
Name:           perl-Test-SQL-Data
Version:        0.0.6
Release:        25%{?dist}
Summary:        Helps running SQL tests: database preparing and result matching
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/frankiejol/Test-SQL-Data
Source0:        https://github.com/frankiejol/Test-SQL-Data/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(DBIx::Connector) >= 0.4.5
Requires:       perl(DBD::SQLite) >= 1.20
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBIx::Connector)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(YAML)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
The purpose of Test::SQL::Data is to give your module a clean database to
work with. When the module loads it prepares the database. You can have it
empty or pre-load some SQL code before running your tests. Then you can use
the module again to check if your expected results match the contents of
the tables of the database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Test-SQL-Data-%{version}
%oreon_prep
%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
