%global source0_hash dc80d7e4f45576de3fd948b6b250fedc500cfd00abcd30b6a8b2d7789576b8f1
Name:		perl-DBIx-SearchBuilder
Version:	1.82
Release:        1%{?dist}
Summary:        Encapsulate SQL queries and rows in simple perl objects
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/DBIx-SearchBuilder
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/DBIx-SearchBuilder-%{version}.tar.gz
BuildArch:	noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Cache::Simple::TimedExpiry)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor)
BuildRequires:  perl(Class::ReturnValue)
BuildRequires:  perl(Clone)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(DBIx::DBSchema)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Want)
BuildRequires:  perl(base)
BuildRequires:  perl(capitalization)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This module provides an object-oriented mechanism for retrieving and
updating data in a DBI-accessible database.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-SearchBuilder-%{version}
rm -r inc
sed -i -e '/^inc\/.*$/d' MANIFEST

# Perms in tarball are broken 
find -type f -exec chmod -x {} \;

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
chmod -R u+w "$RPM_BUILD_ROOT"/*
%oreon_autofiles main

%check

%{__make} test
%package Oracle
Summary:	DBIx::SearchBuilder bindings for Oracle
Requires:	%name = %{version}-%{release}
%description Oracle
DBIx::SearchBuilder bindings for Oracle

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
