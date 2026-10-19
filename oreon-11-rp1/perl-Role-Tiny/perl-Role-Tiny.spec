%global source0_hash 4618ec524618c104dc28a8cc86af129a00cad282aea7f4c75060ba05d4c8f4d7
Name:           perl-Role-Tiny
Version:        2.002005
Release:        1%{?dist}
Summary:        A nouvelle cuisine portion size slice of Moose
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Role-Tiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Role-Tiny-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.05
Requires:       perl(mro)
Provides:       perl(Role::Tiny)
Provides:       perl(Role::Tiny::With)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Role::Tiny is a minimalist role composition tool.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Role-Tiny-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
