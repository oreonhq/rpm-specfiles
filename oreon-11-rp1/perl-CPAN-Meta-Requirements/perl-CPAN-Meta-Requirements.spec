%global source0_hash 1557093e3ff0d650262a8340a1dafc5d033af986f98ee3e8a889d04b53e18019
%bcond_with perl_CPAN_Meta_Requirements_enables_optional_test
Name:           perl-CPAN-Meta-Requirements
Version:        2.145
Release:        1%{?dist}
Summary:        Set of version requirements for a CPAN dist
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/CPAN-Meta-Requirements
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/CPAN-Meta-Requirements-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(version) >= 0.88
%global six_digit_version %(LC_ALL=C; printf '%.6f' '%{version}')
%if "%{version}" != "%{six_digit_version}"
Provides:       perl(CPAN::Meta::Requirements) = %{six_digit_version}
%global __provides_exclude ^perl\\(CPAN::Meta::Requirements\\)$
%endif
Provides:       perl(CPAN::Meta::Requirements::Range) = %{version}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(B)
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
A CPAN::Meta::Requirements object models a set of version constraints like
those specified in the META.yml or META.json files in CPAN distributions. It
can be built up by adding more and more constraints, and it will reduce them
to the simplest representation.

Logically impossible constraints will be identified immediately by thrown
exceptions.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n CPAN-Meta-Requirements-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 UNINST=0
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test AUTHOR_TESTING=1
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.145-1
- Import
