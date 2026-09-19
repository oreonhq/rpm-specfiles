%global source0_hash a5810c091619adb805d5d451fa50a1aca1434fe0938ee1e67d940f01179419c2

Name:           perl-Class-DBI-Plugin-DeepAbstractSearch
Version:        0.08
Release:        47%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        SQL::Abstract for Class::DBI
Source:         https://cpan.metacpan.org/authors/id/S/SR/SRIHA/Class-DBI-Plugin-DeepAbstractSearch-%{version}.tar.gz
Url:            https://metacpan.org/release/Class-DBI-Plugin-DeepAbstractSearch
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Class::DBI::Plugin) >= 0.02
BuildRequires:  perl(SQL::Abstract) >= 1.18
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests only
BuildRequires:  perl(Class::DBI) >= 0.96
BuildRequires:  perl(Test::More) >= 0.32
Requires:       perl(Class::DBI) >= 0.96
Requires:       perl(Class::DBI::Plugin) >= 0.02
Requires:       perl(SQL::Abstract) >= 1.18

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::DBI::Plugin\\)$
%global __requires_exclude %__requires_exclude|^perl\\(SQL::Abstract\\)$

%description
This plugin provides a SQL::Abstract search method for Class::DBI.  It
is similar to Class::DBI::AbstractSearch, but allows you to search and
sort by fields from joined tables.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Class-DBI-Plugin-DeepAbstractSearch-%{version}
find . -type f -exec chmod -c -x {} +
find . -type f -exec perl -pi -e 's/\r//' {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
