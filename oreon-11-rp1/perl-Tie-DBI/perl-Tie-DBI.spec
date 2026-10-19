%global source0_hash 03b1db8957645a68b9b5e94c212b0db53c12bbb69e69513f3c69ad9f70e08765
Name:           perl-Tie-DBI
Version:        1.08
Release:        20%{?dist}
Summary:        Tie hashes to DBI relational databases
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Tie-DBI
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TODDR/Tie-DBI-%{version}.tar.gz
BuildArch:      noarch
Requires:  perl(Encode)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This distribution contains Tie::DBI and Tie::RDBM, two modules that
allow you to tie associative arrays to relational databases using the
DBI library.  The hash is tied to a table in a local or networked
database.  Reading from the hash retrieves values from the database.
Storing into the hash updates the database (if you have sufficient
privileges).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Tie-DBI-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor
make 
%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
