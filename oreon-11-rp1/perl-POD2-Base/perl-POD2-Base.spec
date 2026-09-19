%global source0_hash 071910a2233d11767c9576f1909b8686b4696acb6a7035d1513f9c15ccf0237e

Name:           perl-POD2-Base
Version:        0.043
Release:        43%{?dist}
Summary:        Base module for translations of Perl documentation
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/POD2-Base
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/POD2-Base-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test::More)
# Optional tests:
BuildRequires:  perl(Test::Pod) >= 1.18
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04

%description
This module is an abstraction of the code in POD2::IT and POD2::FR. These
modules belong to the Italian and the French translation projects of core
Perl pods.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n POD2-Base-%{version}

%build
perl Makefile.PL INSTALLDIRS=perl
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%doc eg
%{perl_privlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
