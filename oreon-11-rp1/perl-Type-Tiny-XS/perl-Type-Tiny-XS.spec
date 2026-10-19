%global source0_hash 9a61450dda90294f606cd7a3fa44f3b1a366bcd88a419917b054ee5e23d148bd
Name:           perl-Type-Tiny-XS
Version:        0.025
Release:        1%{?dist}
Summary:        Provides an XS boost for some of Type::Tiny's built-in type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Type-Tiny-XS/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Type-Tiny-XS-%{version}.tar.gz
Recommends:     perl(Type::Parser)
Provides:       perl(Type::Tiny::XS)
# oreon:deps
BuildRequires:  //bin/perl
BuildRequires:  /usr/bin/chmod
BuildRequires:  /usr/bin/make
BuildRequires:  gcc
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(Type::Parser)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
