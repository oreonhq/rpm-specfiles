%global source0_hash b9625992683b97378bea0947773f50e3c9f81974048b84f4c3422cae7e6082f4
Name:           perl-DBIx-Admin-TableInfo
Version:        3.04
Release:        1%{?dist}
Summary:        Wrapper for DBI's table_info(), column_info(), *_key_info()
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Admin-TableInfo
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/DBIx-Admin-TableInfo-%{version}.tgz
Patch0:         DBIx-Admin-TableInfo-3.04-Remove-usr-bin-env-from-shebangs.patch
Patch1:         DBIx-Admin-TableInfo-3.04-Do-not-load-unneeded-modules.patch
BuildArch:      noarch
Requires:       perl(Moo) >= 2.002004
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a convenient wrapper around all of these DBI methods:

    - table_info()
    - column_info()
    - primary_key_info()
    - foreign_key_info()

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DBIx-Admin-TableInfo-%{version}
%patch -P0 -p1
%patch -P1 -p1

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
