%global source0_hash 28d66ea0a8dc306b76da83ff0879493d808f73185bcf9c4ed372f3946fb543ec
Name:           perl-Role-Hooks
Version:        0.008
Release:        1%{?dist}
Summary:        Role callbacks
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Role-Hooks/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Role-Hooks-%{version}.tar.gz
BuildArch:      noarch
Recommends:	perl(Carp)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Class::Tiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Mouse::Role)
BuildRequires:  perl(Package::Variant)
BuildRequires:  perl(Role::Basic)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Role::Tiny::With)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
