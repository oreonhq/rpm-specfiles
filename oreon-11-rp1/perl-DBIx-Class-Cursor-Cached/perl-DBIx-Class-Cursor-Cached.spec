%global source0_hash 37085232a1230a5aa8754399fb59b0f8fcd5f597a1e2e348c5227461a1926225

Name:           perl-DBIx-Class-Cursor-Cached
Version:        1.001004
Release:        27%{?dist}
Summary:        Cursor class with built-in caching support
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Class-Cursor-Cached
Source0:        https://cpan.metacpan.org/authors/id/A/AR/ARCANEZ/DBIx-Class-Cursor-Cached-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.8.1
BuildRequires:  perl-generators
BuildRequires:  perl(inc::Module::Install) >= 1
BuildRequires:  perl(Module::Install::AutoInstall)
BuildRequires:  perl(Module::Install::Metadata)
BuildRequires:  perl(Module::Install::WriteAll)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp::Clan) >= 6.0
BuildRequires:  perl(DBD::SQLite) >= 1.25
BuildRequires:  perl(Digest::SHA)
BuildRequires:  perl(Storable)
BuildRequires:  perl(vars)
# Tests
BuildRequires:  perl(base)
BuildRequires:  perl(Cache::FileCache)
BuildRequires:  perl(DBIx::Class) >= 0.08124
BuildRequires:  perl(DBIx::Class::Core)
BuildRequires:  perl(DBIx::Class::Schema)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp::Clan) >= 6.0
Requires:       perl(DBIx::Class) >= 0.08124

%?perl_default_filter
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Carp::Clan\\)$

%description
This module provides a DBIx cursor class with built-in caching support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Class-Cursor-Cached-%{version}
# Remove bundled libraries
rm -r inc
sed -i -e '/^inc\// d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
