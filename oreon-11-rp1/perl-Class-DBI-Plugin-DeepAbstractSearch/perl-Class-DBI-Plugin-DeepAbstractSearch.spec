%global source0_hash a5810c091619adb805d5d451fa50a1aca1434fe0938ee1e67d940f01179419c2
Name:           perl-Class-DBI-Plugin-DeepAbstractSearch
Version:        0.08
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        SQL::Abstract for Class::DBI
Source0:        https://cpan.metacpan.org/authors/id/S/SR/SRIHA/Class-DBI-Plugin-DeepAbstractSearch-%{version}.tar.gz
Url:            https://metacpan.org/release/Class-DBI-Plugin-DeepAbstractSearch
BuildArch:      noarch
Requires:       perl(Class::DBI) >= 0.96
Requires:       perl(Class::DBI::Plugin) >= 0.02
Requires:       perl(SQL::Abstract) >= 1.18
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Class::DBI::Plugin\\)$
%global __requires_exclude %__requires_exclude|^perl\\(SQL::Abstract\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Class::DBI)
BuildRequires:  perl(Class::DBI::Plugin)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(SQL::Abstract)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
