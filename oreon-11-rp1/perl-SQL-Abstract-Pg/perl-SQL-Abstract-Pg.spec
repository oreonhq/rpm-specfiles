%global source0_hash 3e27360df37b8d88f3c52dac9b03493f9bd3eeff6c8d88f9b086d2711553f547
Name:           perl-SQL-Abstract-Pg
Version:        1.0
Release:        1%{?dist}
Summary:        PostgreSQL features for SQL::Abstract
License:        Artistic-2.0
URL:            https://metacpan.org/release/SQL-Abstract-Pg
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRI/SQL-Abstract-Pg-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(SQL::Abstract::Test)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
SQL::Abstract::Pg extends SQL::Abstract with a few PostgreSQL features used
by Mojo::Pg.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n SQL-Abstract-Pg-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
