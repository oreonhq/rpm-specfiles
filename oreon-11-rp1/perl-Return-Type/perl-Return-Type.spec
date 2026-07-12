%global source0_hash 0dffa4e3a7a63885da029d8f04e79d99d04e0f48b3b890d4509e209bb865e1b4

Name:           perl-Return-Type
Version:        0.007
Release:        16%{?dist}
Summary:        Specify a return type for a function
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Return-Type
Source0:        https://cpan.metacpan.org/authors/id/T/TO/TOBYINK/Return-Type-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__perl}
BuildRequires:  %{__make}

BuildRequires:  perl-interpreter >= 0:5.008
BuildRequires:  perl-generators
BuildRequires:  perl(Attribute::Handlers)
BuildRequires:  perl(Eval::TypeTiny)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.17
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(Types::TypeTiny)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# optional
BuildRequires:  perl(Scope::Upper)
Suggests:       perl(Scope::Upper)


Provides:       perl(Return::Type)
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

%check
%{__make} test

%files
%doc Changes README CREDITS
%license COPYRIGHT LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
