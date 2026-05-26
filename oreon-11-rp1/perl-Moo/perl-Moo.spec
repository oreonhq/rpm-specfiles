# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond perl_Moo_enables_optional_test %{undefined rhel}

Name:           perl-Moo
Version:        2.005005
Release:        11%{?dist}
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

URL:            https://metacpan.org/release/Moo
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(B)
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers) >= 1.10
BuildRequires:  perl(Config)
BuildRequires:  perl(constant)
BuildRequires:  perl(Exporter)
# Filter::Simple not used at test-time
BuildRequires:  perl(Import::Into) >= 1.002
BuildRequires:  perl(Module::Runtime) >= 0.014
BuildRequires:  perl(mro)
# MRO::Compat not needed with modern perl
BuildRequires:  perl(overload)
BuildRequires:  perl(Role::Tiny) >= 2.002004
BuildRequires:  perl(Scalar::Util) >= 1.00
BuildRequires:  perl(Sub::Defer) >= 2.006006
BuildRequires:  perl(Sub::Quote) >= 2.006006
# Text::Balanced not used at test-time
# Optional run-time:
%if %{with perl_Moo_enables_optional_test}
BuildRequires:  perl(Class::XSAccessor) >= 1.18
%endif
BuildRequires:  perl(Sub::Util)
# lib/Moo/HandleMoose.pm requires Moose modules. Moo::HandleMoose is used only
# if Moose has been loaded. So this is circular optional dependency definitly
# not suitable for Moo because Moo is reimplementation of Moose:
#   Class::MOP
#   Moose
#   Moose::Meta::Method::Constructor
#   Moose::Util::TypeConstraints
# Tests:
BuildRequires:  perl(B::Deparse)
%if %{with perl_Moo_enables_optional_test}
BuildRequires:  perl(Class::XSAccessor::Array)
%endif
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(lib)
# MooX::ArrayRef is defined internally via %%INC
BuildRequires:  perl(Test::More) >= 0.96
BuildRequires:  perl(threads)
# Optional tests:
BuildRequires:  perl(CPAN::Meta::Requirements)
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.10
Requires:       perl(Import::Into) >= 1.002
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(mro)
Requires:       perl(Role::Tiny) >= 1.003003

%{?perl_default_filter}
# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Devel::GlobalDestruction|Import::Into|Module::Runtime|Role::Tiny)\\)$

%description
This module is an extremely light-weight, high-performance Moose
replacement. It also avoids depending on any XS modules to allow simple
deployments. The name Moo is based on the idea that it provides almost -but
not quite- two thirds of Moose.

%prep
%oreon_verify_sources
%setup -q -n Moo-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
%{make_build} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.005005-11
- Prepare for Oreon 11 (RP1)
