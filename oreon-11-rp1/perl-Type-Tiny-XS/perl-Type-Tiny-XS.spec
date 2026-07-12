%global source0_hash 9a61450dda90294f606cd7a3fa44f3b1a366bcd88a419917b054ee5e23d148bd

Name:           perl-Type-Tiny-XS
Version:        0.025
Release:        13%{?dist}
Summary:        Provides an XS boost for some of Type::Tiny's built-in type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Type-Tiny-XS/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-%{version}.tar.gz

BuildRequires:  %{__chmod}
BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  gcc
BuildRequires:  perl-devel

BuildRequires:  perl(:VERSION) >= 5.10.1
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(overload)

BuildRequires:  perl(Test::More) >= 0.92
BuildRequires:  perl(Type::Parser)

# Optional run-time requirement of Type::Parser
# Implicitly required by the testsuite
BuildRequires:  perl(Text::Balanced)

# Optional run-time requirement
Recommends:     perl(Type::Parser)


Provides:       perl(Type::Tiny::XS)
%description
This module is optionally used by Type::Tiny 0.045_03 and above to provide
faster, C-based implementations of some type constraints. (This package has
only core dependencies, and does not depend on Type::Tiny, so other data
validation frameworks might also consider using it!)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Type-Tiny-XS-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes CREDITS README
%license COPYRIGHT LICENSE
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Type*
%{_mandir}/man3/*

%changelog
%autochangelog
