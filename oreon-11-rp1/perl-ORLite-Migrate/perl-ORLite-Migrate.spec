%global source0_hash e0a8c5d3916a86c608509fee079489345664d40e5e5e8e9647b9233ff4e3863a
Name:           perl-ORLite-Migrate
Version:        1.10
Release:        1%{?dist}
Summary:        Light weight SQLite-specific schema migration
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/ORLite-Migrate
Source0:        https://cpan.metacpan.org/authors/id/A/AD/ADAMK/ORLite-Migrate-%{version}.tar.gz
Patch0:         perl-ORLite-Migrate-req.patch
Patch1:         ORLite-Migrate-1.10-Remove-using-of-MI-DSL.patch
BuildArch:      noarch
Requires:       perl(File::pushd)
Requires:       perl(IPC::Run3)
Requires:       perl(Probe::Perl)
Requires:       perl(DBD::SQLite) >= 1.21
Requires:       perl(DBI) >= 1.58
Requires:       perl(File::Path) >= 2.04
Requires:       perl(File::Spec) >= 3.28
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBD::SQLite|DBI|File::Path|File::Spec\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::pushd)
BuildRequires:  perl(IPC::Run3)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(ORLite)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Probe::Perl)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
SQLite is a light weight single file SQL database that provides an excellent 
platform for embedded storage of structured data. ORLite is a light weight 
single class Object-Relational Mapper (ORM) system specifically designed 
for (and limited to only) work with SQLite. ORLite::Migrate is a light 
weight single class Database Schema Migration enhancement for ORLite.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n ORLite-Migrate-%{version}
%patch -P0 -p1
%patch -P1 -p1
# Remove bundled modules
rm -r ./inc/*
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
