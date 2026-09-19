%global source0_hash 51b1aef30c5c4009f640267a08589212e87dcd101800f0d20f9c635c9ffe88a1

Name:           perl-Return-MultiLevel
Version:        0.08
Release:        12%{?dist}
Summary:        Return across multiple call levels
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Return-MultiLevel
Source0:        https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Return-MultiLevel-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
# Dependencies
# (none)
# Optional Functionality
BuildRequires:  perl(Scope::Upper) >= 0.29
Requires:       perl(Scope::Upper) >= 0.29

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

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Return/
%{_mandir}/man3/Return::MultiLevel.3*

%changelog
%autochangelog
