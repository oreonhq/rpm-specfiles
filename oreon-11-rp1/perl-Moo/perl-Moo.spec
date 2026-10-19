%global source0_hash fb5a2952649faed07373f220b78004a9c6aba387739133740c1770e9b1f4b108
%bcond perl_Moo_enables_optional_test %{undefined rhel}
Name:           perl-Moo
Version:        2.005005
Release:        1%{?dist}
Summary:        Minimalist Object Orientation (with Moose compatibility)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Moo
Source0:        https://cpan.metacpan.org/authors/id/H/HA/HAARG/Moo-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Moo_enables_optional_test}
%endif
%if %{with perl_Moo_enables_optional_test}
%endif
Requires:       perl(Carp)
Requires:       perl(Class::Method::Modifiers) >= 1.10
Requires:       perl(Import::Into) >= 1.002
Requires:       perl(Module::Runtime) >= 0.012
Requires:       perl(mro)
Requires:       perl(Role::Tiny) >= 1.003003
%{?perl_default_filter}
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Devel::GlobalDestruction|Import::Into|Module::Runtime|Role::Tiny)\\)$
Provides:       perl(Moo)
Provides:       perl(Moo::Role)
Provides:       perl(Method::Generate::Accessor)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(B::Deparse)
BuildRequires:  perl(CPAN::Meta::Requirements)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Method::Modifiers)
BuildRequires:  perl(Class::XSAccessor)
BuildRequires:  perl(Class::XSAccessor::Array)
BuildRequires:  perl(Config)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Import::Into)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Role::Tiny)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Sub::Defer)
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Sub::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(mro)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(threads)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is an extremely light-weight, high-performance Moose
replacement. It also avoids depending on any XS modules to allow simple
deployments. The name Moo is based on the idea that it provides almost -but
not quite- two thirds of Moose.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Moo-%{version}

%build

/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.005005-11
- Prepare for Oreon 11 (RP1)
