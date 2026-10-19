%global source0_hash 8f2180abcbc110bedd9182e4ea3e7852df15f39ae49dc3dadd020b081ffcea08
Name:           perl-MooseX-ArrayRef
Version:        0.005
Release:        30%{?dist}
Summary:        Blessed array references with Moose
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND (GPL-1.0-or-later OR Artistic-1.0-Perl OR LicenseRef-Callaway-CC-BY-SA)
URL:            https://metacpan.org/release/MooseX-ArrayRef
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/MooseX-ArrayRef-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 2.00
Requires:       perl(strict)
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Moose\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Exporter)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::MetaRole)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
