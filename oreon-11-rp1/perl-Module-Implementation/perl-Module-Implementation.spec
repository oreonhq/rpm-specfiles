%global source0_hash c15f1a12f0c2130c9efff3c2e1afe5887b08ccd033bd132186d1e7d5087fd66d
%bcond_with perl_Module_Implementation_enables_extra_test
%bcond_with perl_Module_Implementation_enables_optional_test
Name:		perl-Module-Implementation
Version:	0.09
Release:        1%{?dist}
Summary:        Loads one of several alternate underlying implementations for a module
License:	Artistic-2.0
URL:		https://metacpan.org/release/perl-Module-Implementation
Source0:        https://cpan.metacpan.org/modules/by-module/Module/Module-Implementation-%{version}.tar.gz
BuildArch:	noarch
%if %{with perl_Module_Implementation_enables_optional_test}
%if ! %{defined perl_bootstrap}
%endif
%endif
%if %{with perl_Module_Implementation_enables_extra_test}
%if ! %{defined perl_bootstrap}
%endif
%endif
Requires:	perl(Carp)
Provides:       perl(Module::Implementation)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(blib)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module abstracts out the process of choosing one of several underlying
implementations for a module. This can be used to provide XS and pure Perl
implementations of a module, or it could be used to load an implementation
for a given OS or any other case of needing to provide multiple
implementations.

This module is only useful when you know all the implementations ahead of
time. If you want to load arbitrary implementations then you probably want
something like a plugin system, not this module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Module-Implementation-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}
%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

%if %{defined perl_bootstrap}
make test
%else
%if %{with perl_Module_Implementation_enables_extra_test}
make test RELEASE_TESTING=1
%else
make test
%endif
%endif
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-43
- Prepare for Oreon 11 (RP1)
