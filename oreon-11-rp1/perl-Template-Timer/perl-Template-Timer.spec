%global source0_hash b7314cb365209d93557b8054e0311ae8c3cb5d1c9d228d1eb3e3fc193a5b77b4
Name:           perl-Template-Timer
Version:        1.00
Release:        1%{?dist}
Summary:        Template::Timer Perl module
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Template-Timer
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PETDANCE/Template-Timer-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Template)
BuildRequires:  perl(Template::Context)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Template::Timer provides inline timings of the template processing
througout your code.  It's an overridden version of Template::Context that
wraps the process() and include() methods.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Template-Timer-%{version}
perl -pi -e 's|^#!perl|#!/usr/bin/perl|' t/*.t

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
