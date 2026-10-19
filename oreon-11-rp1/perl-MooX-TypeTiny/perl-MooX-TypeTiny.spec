%global source0_hash d81e26ff6f8db10261f0087f96dc54367dcb49a9f3de8d53238f834ece19624b
Name:           perl-MooX-TypeTiny
Version:        0.002003
Release:        1%{?dist}
Summary:        Optimized type checks for Moo + Type::Tiny
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooX-TypeTiny
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/MooX-TypeTiny-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Moo) >= 2.004
Requires:       perl(Type::Tiny) >= 1.008
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}perl\\(Moo::_
Provides:       perl(MooX::TypeTiny)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Type::Tiny)
BuildRequires:  perl(Types::Standard)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module optimizes Moo type checks when used with Type::Tiny to perform
better. It will automatically apply to isa checks and coercions that use
Type::Tiny. Non-Type::Tiny isa checks will work as normal.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n MooX-TypeTiny-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
