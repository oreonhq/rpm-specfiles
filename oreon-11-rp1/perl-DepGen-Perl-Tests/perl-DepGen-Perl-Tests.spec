%global source0_hash 8c2773ee615aa354555ea8d243ff503914c4de6a3065929d24cae0d1350a1645
%global dist_name DepGen-Perl-Tests
Name:           perl-%{dist_name}
Version:        0.1.2
Release:        29%{?dist}
Summary:        Tests for RPM dependency generator for Perl packages
License:        GPL-3.0-or-later
URL:            http://ppisar.fedorapeople.org/%{dist_name}/
Source0:        http://ppisar.fedorapeople.org/%{dist_name}/%{dist_name}-v%{version}.tar.gz
BuildArch:      noarch
Requires:       rpm-build
Requires:       tar
Requires:       findutils
Requires:       gcc
Requires:       make
Requires:       perl-devel
Requires:       perl-generators
Requires:       perl(AutoLoader)
Requires:       perl(Exporter)
Requires:       perl(ExtUtils::MakeMaker)
Requires:       perl(Test::Simple)
Requires:       perl(version) >= 0.77
Requires:       perl(XSLoader)
%global __requires_exclude_from %{?__requires_exclude_from:%__requires_exclude_from|}^%{perl_vendorlib}/auto/share/
%global __provides_exclude_from %{?__provides_exclude_from:%__provides_exclude_from|}^%{perl_vendorlib}/auto/share/
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(AutoLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(RPM2)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Simple)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  rpm-build
BuildRequires:  tar
# /oreon:deps
%description
This is a regression test suite for Perl RPM dependency generator.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{dist_name}-v%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
