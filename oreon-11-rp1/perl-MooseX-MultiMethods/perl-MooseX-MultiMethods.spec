%global source0_hash 9890a1b83c21b90a573751f4aa215b8a4cff869848d0fe098bca20fe67cd2061
Name:           perl-MooseX-MultiMethods
Version:        0.10
Release:        1%{?dist}
Summary:        Multi Method Dispatch based on Moose type constraints
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/MooseX-MultiMethods
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-MultiMethods-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(MooseX::Types::VariantTable) >= 0.03
%{?perl_default_filter}
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Declare)
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(MooseX::Method::Signatures)
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::VariantTable)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)
BuildRequires:  perl(aliased)
BuildRequires:  perl(lib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides multi method dispatch based on Moose type constraints.
It does so by providing a multi keyword that extends the method keyword
provided by MooseX::Method::Signatures.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n MooseX-MultiMethods-%{version}

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}
%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
