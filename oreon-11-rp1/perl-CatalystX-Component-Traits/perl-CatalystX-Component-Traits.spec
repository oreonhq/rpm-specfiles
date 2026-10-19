%global source0_hash 084944e9c9d0dfb10d4ab3453e1c125fdee39129b46d17c0234c3c5351640447
Name:           perl-CatalystX-Component-Traits
Summary:        Automatic Trait Loading and Resolution for
Version:        0.19
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RK/RKITOVER/CatalystX-Component-Traits-%{version}.tar.gz
URL:            https://metacpan.org/release/CatalystX-Component-Traits
BuildArch:      noarch
Requires:       perl(Catalyst::Runtime) >= 5.80005
Requires:       perl(MooseX::Traits::Pluggable) >= 0.08
%{?perl_default_filter}
%{?perl_default_subpackage_tests}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(CPAN)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Catalyst)
BuildRequires:  perl(Catalyst::Controller)
BuildRequires:  perl(Catalyst::Model)
BuildRequires:  perl(Catalyst::Runtime)
BuildRequires:  perl(Catalyst::Utils)
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  perl(Moose)
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::MethodAttributes)
BuildRequires:  perl(MooseX::Traits::Pluggable)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(namespace::autoclean)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
