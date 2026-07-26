%global source0_hash 086face7ee925d49782a0dc6c699d27e1ac3c5cc6dfc6e99d3e7d892d2038d9b

%global cpan_version 0.111
Name:           perl-Data-Munge
Version:        0.111
Release:        5%{?dist}
Summary:        Utility functions for working with perl data structures and code references
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Data-Munge
Source0:        https://cpan.metacpan.org/modules/by-module/Data/Data-Munge-%{cpan_version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
# Run-time:
# Scalar::Util not used since perl 5.016
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test2::V0)
BuildRequires:  perl(Test::Pod)

%description
This module defines a few generally useful utility functions that process
perl data structures and code references.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Data-Munge-%{cpan_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/Data*
%{_mandir}/man3/Data*

%changelog
%autochangelog
