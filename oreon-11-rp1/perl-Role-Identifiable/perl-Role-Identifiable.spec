%global source0_hash 5a735e9f7177f9ebae047eb7bae29b7ec29ec020ae37637aea5350d30c087b76

Name:           perl-Role-Identifiable
Version:        0.009
Release:        10%{?dist}
Summary:        Identifiable roles
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Role-Identifiable
Source0:        https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Role-Identifiable-%{version}.tar.gz
BuildArch:      noarch
# build requirements
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# runtime requirements
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requirements
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Test::More)

%{?perl_default_filter}

%description
This module provides several Moose roles for identifying things.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Role-Identifiable-%{version}

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
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
