%global source0_hash 5c32272e5e96ea9b63f304fab9ce711f0a9027208d1ab2138a473b4d9f09b225

Name:           perl-HTML-Template-Expr
Version:        0.07
Release:        53%{?dist}
Summary:        Expression support extension for HTML::Template
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/HTML-Template-Expr
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAMTREGAR/HTML-Template-Expr-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(HTML::Template) >= 2.4
BuildRequires:  perl(Parse::RecDescent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests only
BuildRequires:  perl(constant)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Test::More)

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

%check
%{make_build} test

%files
%license ARTISTIC GPL
%doc ANNOUNCE Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
