%global source0_hash 5c32272e5e96ea9b63f304fab9ce711f0a9027208d1ab2138a473b4d9f09b225
Name:           perl-HTML-Template-Expr
Version:        0.07
Release:        1%{?dist}
Summary:        Expression support extension for HTML::Template
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Template-Expr
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/HTML-Template-Expr-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(HTML::Template)
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides an extension to HTML::Template which allows
expressions in the template syntax.  This is purely an addition - all
the normal HTML::Template options, syntax and behaviors will still
work.  Expression support includes comparisons, math operations,
string operations and a mechanism to allow you add your own functions
at runtime.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n HTML-Template-Expr-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
