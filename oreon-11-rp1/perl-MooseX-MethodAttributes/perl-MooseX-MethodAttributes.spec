%global source0_hash cb33886574b7d2dd39c42c0dcdc707acdb0aec7dbbde9a21c0422660368c197b

Name:           perl-MooseX-MethodAttributes
Summary:        Introspect your method code attributes
Version:        0.32
Release:        16%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-MethodAttributes-%{version}.tar.gz
URL:            https://metacpan.org/release/MooseX-MethodAttributes
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(lib)
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Moose) >= 0.98
BuildRequires:  perl(MooseX::Role::Parameterized)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(namespace::clean) >= 0.10
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
BuildRequires:  perl(Test::Requires)

%{?perl_default_filter}

%description
This module allows code attributes of methods to be introspected using
Moose meta method objects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-MethodAttributes-%{version}

# silence rpmlint warning
sed -i '1s,#!.*perl,#!/usr/bin/perl,' t/*.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes README t/
%license LICENCE
%{perl_vendorlib}/MooseX*
%{_mandir}/man3/MooseX*.3*

%changelog
%autochangelog
