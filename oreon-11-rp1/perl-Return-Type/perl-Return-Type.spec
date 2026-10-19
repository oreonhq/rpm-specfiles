%global source0_hash 0dffa4e3a7a63885da029d8f04e79d99d04e0f48b3b890d4509e209bb865e1b4
Name:           perl-Return-Type
Version:        0.007
Release:        1%{?dist}
Summary:        Specify a return type for a function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Return-Type
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Return-Type-%{version}.tar.gz
BuildArch:      noarch
Suggests:       perl(Scope::Upper)
Provides:       perl(Return::Type)
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  /usr/bin/perl
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scope::Upper)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::TypeTiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Return::Type allows you to specify a return type for your subs. Type
constraints from any Type::Tiny, MooseX::Types or MouseX::Types type
library are supported.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Return-Type-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
