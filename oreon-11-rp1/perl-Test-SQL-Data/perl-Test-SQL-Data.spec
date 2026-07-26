%global source0_hash ad108f1b1b968d112e6f46ceac9e8493b02b40f4a91cad8fdb0bf5c381547716

Name:           perl-Test-SQL-Data
Version:        0.0.6
Release:        25%{?dist}
Summary:        Helps running SQL tests: database preparing and result matching
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://github.com/frankiejol/Test-SQL-Data
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBIx::Connector) >= 0.4.5
BuildRequires:  perl(DBD::SQLite) >= 1.20
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Path)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Perl::Critic)
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
BuildRequires:  perl(Test::Pod) >= 1.14
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl(YAML)
Requires:       perl(DBIx::Connector) >= 0.4.5
Requires:       perl(DBD::SQLite) >= 1.20

%description
The purpose of Test::SQL::Data is to give your module a clean database to
work with. When the module loads it prepares the database. You can have it
empty or pre-load some SQL code before running your tests. Then you can use
the module again to check if your expected results match the contents of
the tables of the database.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n Test-SQL-Data-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc INSTALL.md README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
