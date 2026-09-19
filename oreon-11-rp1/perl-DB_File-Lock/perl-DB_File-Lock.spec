%global source0_hash 08a93109a404624562f353e1f7e738b93899d4defab55c2cea5b8657fb62a985

Name:           perl-DB_File-Lock
Version:        0.05
Release:        36%{?dist}
Summary:        Locking with flock wrapper for DB_File
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/DB_File-Lock
Source0:        https://cpan.metacpan.org/modules/by-module/DB_File/DB_File-Lock-%{version}.tar.gz
# defined() should not be used for hash RT#98224
Patch1:         DB_File-Lock-0.05-RT98224.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Carp)
BuildRequires:  perl(DB_File)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(Symbol)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

%description
This module provides a wrapper for the DB_File module, adding locking.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n DB_File-Lock-%{version}
%patch -P1 -p1

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
