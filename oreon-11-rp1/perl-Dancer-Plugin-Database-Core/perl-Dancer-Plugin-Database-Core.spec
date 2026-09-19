%global source0_hash 345536603883e2fcc599ef79ead66d97a8ec0c2e31e24f60a55298e8d498150a

Name:           perl-Dancer-Plugin-Database-Core
Version:        0.20
Release:        23%{?dist}
Summary:        Shared core for Dancer and Dancer2 Database plugins
License:        Artistic-2.0

URL:            http://metacpan.org/release/Dancer-Plugin-Database-Core/
Source0:        https://cpan.metacpan.org/authors/id/B/BI/BIGPRESH/Dancer-Plugin-Database-Core-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(Carp)
BuildRequires:  perl(DBI)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod) >= 1.22

%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(DBI::db\\)$

%description
Dancer::Plugin::Database::Core is a shared core for Dancer and Dancer2
database plugins. This module should not be used directly. It is a
shared library for Dancer::Plugin::Database and
Dancer2::Plugin::Database modules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Dancer-Plugin-Database-Core-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
RELEASE_TESTING=1 make test

%files
%doc Changes README
%{perl_vendorlib}/Dancer*
%{_mandir}/man3/Dancer*

%changelog
%autochangelog
