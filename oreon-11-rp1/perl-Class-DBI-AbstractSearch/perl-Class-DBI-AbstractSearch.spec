%global source0_hash d93209f38fc1b296c985afed46f3858f5d2b070f655f503cdcbfb227ab22dec9

Name:           perl-Class-DBI-AbstractSearch
Version:        0.07
Release:        54%{?dist}
Summary:        Abstract Class::DBI's SQL with SQL::Abstract
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Class-DBI-AbstractSearch
Source0:        https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Class-DBI-AbstractSearch-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-doc
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(DBD::SQLite)
BuildRequires:  perl(DBI)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Pod::Perldoc)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(SQL::Abstract::Limit)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
Requires:  perl(Class::DBI)

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-AbstractSearch-%{version}
perldoc -t perlartistic > Artistic
perldoc -t perlgpl > COPYING

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Artistic COPYING Changes
%{perl_vendorlib}/Class/DBI
%{_mandir}/man3/*.3*

%changelog
%autochangelog
