%global source0_hash 69a7a891cd3888ed8b02c5e99a1f489f92a62ec351c0bc7894fd7bd7d1447ea9

Name:           perl-enum
Version:        1.12
Release:        13%{?dist}
Summary:        C-style enumerated types and bitmask flags in Perl
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/enum

Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/enum-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time:
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)

# Testing
BuildRequires:  perl(Carp)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Test::More)

%description
This module is used to define a set of constants with ordered numeric
values, similar to the enum type in the C programming language.
You can also define bitmask constants, where the value assigned to
each constant has exactly one bit set (e.g. 1, 2, 4, 8, etc).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n enum-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc README Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
