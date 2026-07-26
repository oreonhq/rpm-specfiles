%global source0_hash 8f2180abcbc110bedd9182e4ea3e7852df15f39ae49dc3dadd020b081ffcea08

Name:           perl-MooseX-ArrayRef
Version:        0.005
Release:        30%{?dist}
Summary:        Blessed array references with Moose
# CONTRIBUTING: GPL+ or Artistic or CC-BY-SA
# other files:  GPL+ or Artistic
# Automatically converted from old format: (GPL+ or Artistic) and (GPL+ or Artistic or CC-BY-SA) - review is highly recommended.
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://metacpan.org/release/MooseX-ArrayRef
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooseX-ArrayRef-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
# Run-time:
BuildRequires:  perl(constant)
BuildRequires:  perl(Moose) >= 2.00
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Scalar::Util)
# Tests:
BuildRequires:  perl(Test::More) >= 0.61
Requires:       perl(Moose) >= 2.00
Requires:       perl(strict)

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moose\\)$

%description
Objects implemented with array references are often faster than those
implemented with hash references. Moose's default object implementation is
hash reference based. This is object implementation based on array references.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-ArrayRef-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes CONTRIBUTING COPYRIGHT CREDITS examples README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
