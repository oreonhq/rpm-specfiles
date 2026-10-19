%global source0_hash 51b1aef30c5c4009f640267a08589212e87dcd101800f0d20f9c635c9ffe88a1
Name:           perl-Return-MultiLevel
Version:        0.08
Release:        1%{?dist}
Summary:        Return across multiple call levels
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Return-MultiLevel
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Return-MultiLevel-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Scope::Upper) >= 0.29
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scope::Upper)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides a way to return immediately from a deeply nested call
stack. This is similar to exceptions, but exceptions don't stop automatically
at a target frame (and they can be caught by intermediate stack frames using
eval). In other words, this is more like setjmp(3)/longjmp(3) than die.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Return-MultiLevel-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
