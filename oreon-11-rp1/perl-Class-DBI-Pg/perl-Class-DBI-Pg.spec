%global source0_hash d8044e624117406293855dbd98dd6c081714cf5d0fd41b5f3394f315889e1f7f

Name:           perl-Class-DBI-Pg
Version:        0.09
Release:        53%{?dist}
Summary:        Class::DBI extension for PostgreSQL
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-Pg
Source0:        https://cpan.metacpan.org/authors/id/D/DM/DMAKI/Class-DBI-Pg-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(DBD::Pg)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:  perl(Carp)
Requires:  perl(DBD::Pg)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Pg-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Artistic COPYING Changes
%{perl_vendorlib}/Class/DBI
%{_mandir}/man3/*.3*

%changelog
%autochangelog
