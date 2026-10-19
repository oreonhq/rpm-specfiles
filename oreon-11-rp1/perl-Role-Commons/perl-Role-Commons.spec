%global source0_hash b23e8f692bab359012a419e1dcdb416fc4205b690bb7418e8983f21d1ba5368a
%bcond_without perl_Role_Commons_enables_optional_test
Name:           perl-Role-Commons
Version:        0.104
Release:        20%{?dist}
Summary:        Roles that can be commonly used
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Role-Commons/
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Role-Commons-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Role_Commons_enables_optional_test}
%endif
Requires:       perl(Types::TypeTiny) >= 1.000000
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Types::TypeTiny\\)$
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Object::ID)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::TypeTiny)
BuildRequires:  perl(match::simple)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Role-Commons is not yet another implementation of roles. It is a collection of
generic, reusable roles that hopefully you will love to apply to your classes.
These roles are built using Moo::Role, so automatically integrate into the
Moose object system if you're using it, but they do not require Moose.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Role-Commons-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
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
