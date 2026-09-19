%global source0_hash 73c9099b4bf1e9c01e795e2cb6c7357ff200570ec989b6d67fa08ddb319280e6

Name:           perl-Test-Net-LDAP
Version:        0.07
Release:        17%{?dist}
Summary:        Net::LDAP subclass for testing
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Net-LDAP/
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Net-LDAP-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(IO::Socket)
BuildRequires:  perl(Net::LDAP)
BuildRequires:  perl(Net::LDAP::Constant)
BuildRequires:  perl(Net::LDAP::Entry)
BuildRequires:  perl(Net::LDAP::Filter)
BuildRequires:  perl(Net::LDAP::FilterMatch)
BuildRequires:  perl(Net::LDAP::Util)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(Net::LDAP::Bind)
Requires:       perl(Net::LDAP::RootDSE)
Requires:       perl(Net::LDAP::Search)

%description
This module provides some testing methods for LDAP operations, such
as search, add, and modify, where each method is suffixed with either
_ok or _is.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Net-LDAP-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make_build

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
