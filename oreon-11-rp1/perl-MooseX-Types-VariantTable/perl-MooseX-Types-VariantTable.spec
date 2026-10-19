%global source0_hash 3029abda57d530991f4af4d21f23b61f5e522a5b1e3bd69202edd6960a38d070
Name:           perl-MooseX-Types-VariantTable
Version:        0.04
Release:        1%{?dist}
Summary:        Type constraint based variant table
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/dist/MooseX-Types-VariantTable
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-Types-VariantTable-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::Clone) >= 0.03
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Hash::Util::FieldHash::Compat)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Util::TypeConstraints)
BuildRequires:  perl(MooseX::Clone)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::Structured)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Exporter)
BuildRequires:  perl(Sub::Name)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::use::ok)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
This object implements a simple dispatch table based on Moose type
constraints.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-Types-VariantTable-%{version}

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
