%global source0_hash 338d5569e8e89a654935f843ec0bc84aaa486fe8dd1898fb9cab3eccecd5327a

# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Test_CleanNamespaces_enables_extra_test
%else
%bcond_with perl_Test_CleanNamespaces_enables_extra_test
%endif

Name:		perl-Test-CleanNamespaces
Summary:	Check for uncleaned imports
Version:	0.24
Release:	26%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-CleanNamespaces
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-CleanNamespaces-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(CPAN::Meta::Requirements) >= 2.120620
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Module::Metadata)
# Module
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Package::Stash) >= 0.14
BuildRequires:	perl(Package::Stash::XS)
BuildRequires:	perl(strict)
BuildRequires:	perl(Sub::Identify)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(warnings)
# Optional Runtime
BuildRequires:	perl(Role::Tiny) >= 1.003000
# Test Suite
BuildRequires:	perl(constant)
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(if)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(namespace::clean)
BuildRequires:	perl(overload)
BuildRequires:	perl(parent)
BuildRequires:	perl(Scalar::Util)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Test::Deep)
BuildRequires:	perl(Test::More) >= 0.96
BuildRequires:	perl(Test::Needs)
BuildRequires:	perl(Test::Tester)
BuildRequires:	perl(Test::Warnings) >= 0.009
# Optional Test Requirements
%if 0%{!?perl_bootstrap:1} && %{with perl_Test_CleanNamespaces_enables_extra_test}
BuildRequires:	perl(Class::MOP::Class)
BuildRequires:	perl(metaclass)
BuildRequires:	perl(Moo) >= 1.000007
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Moose::Exporter)
BuildRequires:	perl(Moose::Role)
BuildRequires:	perl(MooseX::Role::Parameterized)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Mouse::Role)
%endif
# Dependencies
Recommends:	perl(Role::Tiny) >= 1.003000

Provides:       perl(Test::CleanNamespaces)
%description
This module lets you check your module's namespaces for imported functions you
might have forgotten to remove with namespace::autoclean or namespace::clean
and are therefore available to be called as methods, which usually isn't want
you want.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-CleanNamespaces-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test AUTOMATED_TESTING=1

%files
%license LICENCE
%doc Changes CONTRIBUTING README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CleanNamespaces.3*

%changelog
%autochangelog
