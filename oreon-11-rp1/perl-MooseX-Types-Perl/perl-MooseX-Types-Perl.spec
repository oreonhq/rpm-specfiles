%global source0_hash 87644354f74fa65235cb2bfca44277930a7eabe51acc5f81fb631530a8355e24

Name:           perl-MooseX-Types-Perl
Version:        0.101344
Release:        10%{?dist}
Summary:        Moose types that check against Perl syntax
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-Types-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/MooseX-Types-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MooseX::Types)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(Params::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(version) >= 0.82

%{?perl_default_filter}

%description
This library provides Moose types for checking things (mostly strings)
against syntax that is, or is a reasonable subset of, Perl syntax.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-Perl-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*

%changelog
%autochangelog
