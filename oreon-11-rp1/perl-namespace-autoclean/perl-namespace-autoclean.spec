# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_namespace_autoclean_enables_optional_test
%else
%bcond_with perl_namespace_autoclean_enables_optional_test
%endif

Name:           perl-namespace-autoclean
Version:        0.31
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Keep imports out of your namespace
URL:            https://metacpan.org/release/namespace-autoclean
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/namespace-autoclean-0.31.tar.gz
# oreon url source checksums begin
%global source0_sha256 d3b32c82e1d2caa9d58b8c8075965240e6cab66ab9350bd6f6bea4ca07e938d6
%global source0_file namespace-autoclean-0.31.tar.gz
# oreon url source checksums end

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(B::Hooks::EndOfScope) >= 0.12
BuildRequires:  perl(List::Util)
BuildRequires:  perl(namespace::clean) >= 0.20
BuildRequires:  perl(strict)
BuildRequires:  perl(Sub::Util) >= 1.40
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(overload)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Needs)
%if %{with perl_namespace_autoclean_enables_optional_test}
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
BuildRequires:  perl(Moo) >= 1.004000
%if ! %{defined perl_bootstrap}
# Break build-cycle: perl-namespace-autoclean → perl-Moose
# → perl-Package-DeprecationManager → perl-namespace-autoclean
# Break build-cycle: perl-namespace-autoclean → perl-Mouse → perl-Moose
# → perl-Package-DeprecationManager → perl-namespace-autoclean
BuildRequires:  perl(Class::MOP)
BuildRequires:  perl(Moose) >= 0.56
BuildRequires:  perl(Moose::Role)
BuildRequires:  perl(MooseX::Role::WithOverloading) >= 0.09
BuildRequires:  perl(Mouse)
%endif
BuildRequires:  perl(Sub::Install)
BuildRequires:  perl(Sub::Name)
%endif
# Dependencies
Requires:       perl(Sub::Util) >= 1.40

%description
When you import a function into a Perl package, it will naturally also be
available as a method. The 'namespace::autoclean' pragma will remove all
imported symbols at the end of the current package's compile cycle. Functions
called in the package itself will still be bound by their name, but they won't
show up as methods on your class or instances. This module is very similar to
namespace::clean, except it will clean all imported functions, no matter if you
imported them before or after you 'use'd the pragma. It will also not touch
anything that looks like a method.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/namespace-autoclean-0.31.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d3b32c82e1d2caa9d58b8c8075965240e6cab66ab9350bd6f6bea4ca07e938d6" || { echo "oreon: Source0 SHA256 mismatch for namespace-autoclean-0.31.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n namespace-autoclean-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/namespace/
%{_mandir}/man3/namespace::autoclean.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.31-4
- Prepare for Oreon 11 (RP1)
