%global source0_hash b9625992683b97378bea0947773f50e3c9f81974048b84f4c3422cae7e6082f4

Name:           perl-DBIx-Admin-TableInfo
Version:        3.04
Release:        15%{?dist}
Summary:        Wrapper for DBI's table_info(), column_info(), *_key_info()
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DBIx-Admin-TableInfo
Source0:        https://cpan.metacpan.org/authors/id/R/RS/RSAVAGE/DBIx-Admin-TableInfo-%{version}.tgz
# Remove stay shebangs from documentation
Patch0:         DBIx-Admin-TableInfo-3.04-Remove-usr-bin-env-from-shebangs.patch
# Do not load unnecessary modules in the tests
Patch1:         DBIx-Admin-TableInfo-3.04-Do-not-load-unneeded-modules.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Moo) >= 2.002004
# Tests:
BuildRequires:  perl(Test::More)
Requires:       perl(Moo) >= 2.002004

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Moo\\)$

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

%check
make test

%files
%license LICENSE
# Changelog.ini is redundant with Changes.
# README is not helpful.
%doc Changes scripts/*.pl
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
