# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 c15f1a12f0c2130c9efff3c2e1afe5887b08ccd033bd132186d1e7d5087fd66d
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%if ! (0%{?rhel})
# Run extra test
%bcond_without perl_Module_Implementation_enables_extra_test
# Run optional test
%bcond_without perl_Module_Implementation_enables_optional_test
%else
%bcond_with perl_Module_Implementation_enables_extra_test
%bcond_with perl_Module_Implementation_enables_optional_test
%endif

Name:		perl-Module-Implementation
Version:	0.09
Release:	43%{?dist}
Summary:	Loads one of several alternate underlying implementations for a module
License:	Artistic-2.0
URL:		https://metacpan.org/release/perl-Module-Implementation
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/Module-Implementation-0.09.tar.gz

BuildArch:	noarch
# ===================================================================
# Build requirements
# ===================================================================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Carp)
BuildRequires:	perl(Module::Runtime) >= 0.012
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# ===================================================================
# Test suite requirements
# ===================================================================
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Test::Fatal) >= 0.006
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Requires)
%if %{with perl_Module_Implementation_enables_optional_test}
# ===================================================================
# Optional test requirements
# ===================================================================
BuildRequires:	perl(CPAN::Meta) >= 2.120900
%if ! %{defined perl_bootstrap}
# Build cycle: Test::CleanNamespaces → Package::Stash → Module::Implementation
BuildRequires:	perl(Test::CleanNamespaces)
%endif
BuildRequires:	perl(Test::Taint)
%endif
%if %{with perl_Module_Implementation_enables_extra_test}
# ===================================================================
# Author/Release test requirements
# ===================================================================
# Release tests include circular dependencies, so don't do them when bootstrapping:
%if ! %{defined perl_bootstrap}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::CPAN::Changes) >= 0.19
BuildRequires:	perl(Test::EOL)
BuildRequires:	perl(Test::NoTabs)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
# Can't use EPEL packages as BR: for RHEL package
%if ! 0%{?rhel}
BuildRequires:	hunspell-en
BuildRequires:	perl(Pod::Wordlist)
BuildRequires:	perl(Test::Pod::LinkCheck)
BuildRequires:	perl(Test::Pod::No404s)
BuildRequires:	perl(Test::Spelling) >= 0.12
%endif
%endif
%endif
# ===================================================================
# Dependencies
# ===================================================================
Requires:	perl(Carp)

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
%oreon_verify_sources
%setup -q -n Module-Implementation-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
%if %{defined perl_bootstrap}
make test
%else
%if %{with perl_Module_Implementation_enables_extra_test}
# Don't run the author tests for EL builds (see above)
%if ! 0%{?rhel}
make test AUTHOR_TESTING=1 RELEASE_TESTING=1
%else
make test RELEASE_TESTING=1
%endif
%else
make test
%endif
%endif

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Module/
%{_mandir}/man3/Module::Implementation.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.09-43
- Prepare for Oreon 11 (RP1)
