%global source0_hash e2163cd4e3e805662c2ed6788fda35870fd804ecd949554c56454f50f8d1d1a1
Name:           perl-Version-Next
Version:        1.000
Release:        1%{?dist}
Summary:        Increment module version numbers simply and correctly
License:        Apache-2.0
URL:            https://metacpan.org/release/Version-Next
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Version-Next-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a simple, correct way to increment a Perl module
version number. It does not attempt to guess what the original version
number author intended, it simply increments in the smallest possible
fashion. Decimals are incremented like an odometer. Dotted decimals are
incremented piece-wise and presented in a standardized way.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Version-Next-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
