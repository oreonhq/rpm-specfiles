%global source0_hash 9890a1b83c21b90a573751f4aa215b8a4cff869848d0fe098bca20fe67cd2061

Name:           perl-MooseX-MultiMethods
Version:        0.10
Release:        46%{?dist}
Summary:        Multi Method Dispatch based on Moose type constraints
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/MooseX-MultiMethods
Source0:        https://cpan.metacpan.org/authors/id/F/FL/FLORA/MooseX-MultiMethods-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(aliased)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Devel::Declare) >= 0.004000
BuildRequires:  perl(Devel::Declare::Context::Simple)
BuildRequires:  perl(Devel::PartialDump)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Meta::Method)
BuildRequires:  perl(Moose::Object)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Method::Signatures) >= 0.29
BuildRequires:  perl(MooseX::Types::Moose)
BuildRequires:  perl(MooseX::Types::VariantTable) >= 0.03
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(warnings)
# tests
BuildRequires:  perl(MooseX::Declare)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::NoWarnings)

Requires:       perl(MooseX::Types::VariantTable) >= 0.03

%{?perl_default_filter}

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

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/Moose*
%{_mandir}/man3/Moose*

%changelog
%autochangelog
