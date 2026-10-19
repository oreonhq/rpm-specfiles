%global source0_hash dedd15b4b93483c30c07027134e21ce5114ae9b5ed2e4ab7736a2bf76fade28e
Name:           perl-MooseX-Role-TraitConstructor
Version:        0.01
Release:        1%{?dist}
Summary:        Wrapper for new that can accept a traits parameter
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-Role-TraitConstructor
Source0:        https://cpan.metacpan.org/authors/id/N/NU/NUFFIN/MooseX-Role-TraitConstructor-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moose) >= 0.40
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(constant)
BuildRequires:  perl(ok)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This role allows you to easily accept a traits argument (or another name)
into your constructor, which will easily mix roles into an anonymous class
before construction, much like Moose::Meta::Attribute does.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Role-TraitConstructor-%{version}

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
