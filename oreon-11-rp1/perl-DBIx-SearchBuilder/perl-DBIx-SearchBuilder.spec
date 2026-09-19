%global source0_hash dc80d7e4f45576de3fd948b6b250fedc500cfd00abcd30b6a8b2d7789576b8f1

#
# --with oracle 
#	Build perl-DBIx-SearchBuilder-Oracle subpackage. 
#	Disabled by default, because it depends on packages outside of Fedora
#	at run-time
#

Name:		perl-DBIx-SearchBuilder
Version:	1.82
Release:	5%{?dist}
Summary:	Encapsulate SQL queries and rows in simple perl objects
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/DBIx-SearchBuilder
Source0:	https://cpan.metacpan.org/authors/id/B/BP/BPS/DBIx-SearchBuilder-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	%{__make}

BuildRequires:	perl(:VERSION) >= 5.10.1
BuildRequires:	perl-generators

BuildRequires:	perl(Cache::Simple::TimedExpiry) >= 0.21
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Class::ReturnValue) >= 0.4
BuildRequires:	perl(Carp)
BuildRequires:	perl(DBD::SQLite) > 1.60
BuildRequires:	perl(DBI)
BuildRequires:	perl(Encode) >= 1.99
BuildRequires:	perl(Exporter)
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.59
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Test::More) >= 0.52
BuildRequires:	perl(Want)

BuildRequires:	perl(base)
BuildRequires:	perl(strict)
BuildRequires:	perl(vars)
BuildRequires:	perl(version)
BuildRequires:	perl(warnings)

# Improved tests:
BuildRequires:	perl(Test::Pod)

# Optional features
BuildRequires:	perl(capitalization) >= 0.03
BuildRequires:	perl(Clone)
BuildRequires:	perl(DBIx::DBSchema)

BuildRequires:	perl(inc::Module::Install)
# Use Module::Install::ReadmeFromPod instead of bundled version
BuildRequires:	perl(Module::Install::ReadmeFromPod)

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
# --skipdeps causes ExtUtils::AutoInstall not to try auto-installing 
# missing optional features
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
chmod -R u+w "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%doc Changes
%doc README ROADMAP
%{perl_vendorlib}/DBIx
%{_mandir}/man3/*
%exclude %{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%exclude %{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*

%if "%{?_with_oracle}"
%package Oracle
Summary:	DBIx::SearchBuilder bindings for Oracle
Requires:	%name = %{version}-%{release}

%description Oracle
DBIx::SearchBuilder bindings for Oracle

%files Oracle
%{perl_vendorlib}/DBIx/SearchBuilder/Handle/Oracle*
%{_mandir}/man3/DBIx::SearchBuilder::Handle::Oracle*
%endif

%changelog
%autochangelog
