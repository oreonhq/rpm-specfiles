%global source0_hash 45d26088eca2971752b4fbcd350f2cf3e0e54295fd93b74e1132e16152d00c03

Name:           perl-Test-mysqld
Version:        1.0030
Release:        6%{?dist}
Summary:        Mysqld runner for tests
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-mysqld

Source0:        https://cpan.metacpan.org/authors/id/S/SO/SONGMU/Test-mysqld-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build::Tiny) >= 0.035
BuildRequires:  perl(strict)

# Run-time
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(DBI)
BuildRequires:  perl(File::Copy::Recursive)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)
BuildRequires:  mariadb-server

# Testing
BuildRequires:  perl(DBD::MariaDB)
BuildRequires:  perl(DBD::mysql)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::SharedFork) >= 0.06

Requires:       perl(DBD::mysql)
Requires:       mariadb-server

%description
Test::mysqld automatically setups a mysqld instance in a temporary
directory, and destroys it when the perl script exits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-mysqld-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
