%global source0_hash 2060f8a3f5ea26944d6ec013c81f46662ead6c1e32ad1b3ab394d9c0f7462d20

#This file is licensed under the terms of GNU GPLv2+.
Name:           perl-Proc-SyncExec
Version:        1.01
Release:        41%{?dist}
Summary:        Spawn processes but report exec() errors
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Proc-SyncExec
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROSCH/Proc-SyncExec-%{version}.tar.gz
Patch0:         %{name}-1.01-Adjust-test-to-confinded-Fedora-Koji-build-system.patch
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module contains functions for synchronized process spawning with full
error return. If the child's exec() call fails the reason for the failure
is reported back to the parent.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Proc-SyncExec-%{version}
%patch -P0 -p1 -b .koji

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
