%global source0_hash 00a1379249dffad428a54152a508f08c6195cb3a3d0691f3cb7c6fbf619f8426
Name:           perl-Filter-signatures
Version:        0.19
Release:        1%{?dist}
Summary:        Very simplistic signatures for Perl < 5.20
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/Filter-signatures/
Source0:        https://cpan.metacpan.org/authors/id/C/CO/CORION/Filter-signatures-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(feature)
Requires:       perl(warnings)
Requires:       perl(warnings::register)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(CPAN::Meta::YAML)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Filter::Simple)
BuildRequires:  perl(Pod::Markdown)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::Balanced)
BuildRequires:  perl(feature)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(warnings::register)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module implements a backwards compatibility shim for formal Perl
subroutine signatures that were introduced to the Perl core with Perl 5.20.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Filter-signatures-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

unset FORCE_FILTER_SIGNATURES
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
