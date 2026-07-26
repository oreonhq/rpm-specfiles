%global source0_hash 764d34efb50ecf12d83561f66ef6724f89c3dde6f5aa26ea18cf5f84c87bf7e1

Name:           perl-MD5
Version:        2.03
Release:        50%{?dist}
Summary:        Perl interface to the MD5 Message-Digest Algorithm
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MD5
Source0:        https://cpan.metacpan.org/modules/by-module/MD5/GAAS/MD5-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Digest::MD5) >= 2.00
BuildRequires:  perl(ExtUtils::MakeMaker)

%description
This module (MD5.pm) is just a thin wrapper around the Digest::MD5
module.  It is provided so that legacy code that rely on the old
interface continue to work with the speed benefit of the new module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MD5-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
