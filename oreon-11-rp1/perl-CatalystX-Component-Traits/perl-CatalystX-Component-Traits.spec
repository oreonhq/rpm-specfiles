%global source0_hash 084944e9c9d0dfb10d4ab3453e1c125fdee39129b46d17c0234c3c5351640447

Name:           perl-CatalystX-Component-Traits
Summary:        Automatic Trait Loading and Resolution for
Version:        0.19
Release:        33%{?dist}
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl

Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CatalystX-Component-Traits-%{version}.tar.gz
URL:            https://metacpan.org/release/CatalystX-Component-Traits

BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Model)
BuildRequires:  perl(Catalyst::Runtime) >= 5.80005
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(CPAN)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable) >= 3.9
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::MethodAttributes)
BuildRequires:  perl(MooseX::Traits::Pluggable) >= 0.08
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)

Requires:       perl(Catalyst::Runtime) >= 5.80005
Requires:       perl(MooseX::Traits::Pluggable) >= 0.08

%{?perl_default_filter}
%{?perl_default_subpackage_tests}

%description
Adds a "COMPONENT" method to your Catalyst component base class that
reads the optional 'traits' parameter from app and component config
and instantiates the component subclass with those traits using
MooseX::Traits/new_with_traits from MooseX::Traits::Pluggable.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n CatalystX-Component-Traits-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'

%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
%autochangelog
