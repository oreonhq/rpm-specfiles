%global source0_hash e2163cd4e3e805662c2ed6788fda35870fd804ecd949554c56454f50f8d1d1a1

Name:           perl-Version-Next
Version:        1.000
Release:        27%{?dist}
Summary:        Increment module version numbers simply and correctly
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://metacpan.org/release/Version-Next
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Version-Next-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(version) >= 0.81
# Tests:
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::Exception) >= 0.29
BuildRequires:  perl(Test::More) >= 0.88

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
