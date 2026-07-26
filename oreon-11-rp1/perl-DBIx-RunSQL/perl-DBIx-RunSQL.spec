%global source0_hash 75d7114ca874253a0f8712d9f0c3201dff844a71dc0dace98dc14dd171f0c077

Name:           perl-DBIx-RunSQL
Version:        0.26
Release:        3%{?dist}
Summary:        Run SQL commands from a file
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-RunSQL

Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/DBIx-RunSQL-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(DBI)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Module::Load)

# Testing
BuildRequires:  perl-experimental
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Table)

Requires:       perl(Getopt::Long) >= 2.36
Requires:       perl(Pod::Usage)

%description
This module abstracts away the "run these SQL statements to set up
a database" into a module. It also abstracts away the reading of
SQL from a file and allows for various command line parameters
to be passed in.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-RunSQL-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/run-sql.pl
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
