%global source0_hash 28d66ea0a8dc306b76da83ff0879493d808f73185bcf9c4ed372f3946fb543ec

Name:           perl-Role-Hooks
Version:        0.008
Release:        10%{?dist}
Summary:        Role callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/dist/Role-Hooks/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Role-Hooks-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  make

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.1

BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(List::Util) >= 1.45
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Test::Requires)

BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testsuite requirements
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)

# Optional testsuite requirements
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Package::Variant)
BuildRequires:  perl(Role::Basic)

# Not sure, if this dep should be mandatory
Recommends:	perl(Carp)

%description
This module allows a role to run a callback when it is applied to a class
or to another role.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Role-Hooks-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install} DESTDIR="$RPM_BUILD_ROOT"
%{_fixperms} "$RPM_BUILD_ROOT"/*

%check
%{__make} test

%files
%license LICENSE COPYRIGHT
%doc Changes CREDITS README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
