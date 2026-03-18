# Run optional tests
%bcond_without perl_Perl_OSType_enables_optional_test

Name:		perl-Perl-OSType
Version:	1.010
Release:	522%{?dist}
Summary:	Map Perl operating system names to generic types
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Perl-OSType
Source0:	https://cpan.metacpan.org/modules/by-module/Perl/Perl-OSType-%{version}.tar.gz
Patch2:		Perl-OSType-1.010-stopwords.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.17
# Module
BuildRequires:	perl(Exporter)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(constant)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Optional tests, not run for this dual-lived module when bootstrapping
# Also not run for EPEL builds due to package unavailability
%if !%{defined perl_bootstrap} && 0%{?fedora} && %{with perl_Perl_OSType_enables_optional_test}
BuildRequires:	glibc-langpack-en
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Perl::Critic::Policy::Lax::ProhibitStringyEval::ExceptForRequire)
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Pod::Wordlist)
BuildRequires:	perl(Test::CPAN::Meta)
BuildRequires:	perl(Test::MinimumVersion)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
BuildRequires:	perl(Test::Portability::Files)
BuildRequires:	perl(Test::Spelling), hunspell-en
BuildRequires:	perl(Test::Version)
%endif
# Dependencies
# (none)

%description
Modules that provide OS-specific behaviors often need to know if the current
operating system matches a more generic type of operating systems. For example,
'linux' is a type of 'Unix' operating system and so is 'freebsd'.

This module provides a mapping between an operating system name as given by $^O
and a more generic type. The initial version is based on the OS type mappings
provided in Module::Build and ExtUtils::CBuilder (thus, Microsoft operating
systems are given the type 'Windows' rather than 'Win32').

%prep
%setup -q -n Perl-OSType-%{version}

# More stopwords for the spell checker
%patch -P 2

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test
%if !%{defined perl_bootstrap} && 0%{?fedora} && %{with perl_Perl_OSType_enables_optional_test}
LANG=en_US make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%license LICENSE
%doc Changes CONTRIBUTING.mkdn README
%{perl_vendorlib}/Perl/
%{_mandir}/man3/Perl::OSType.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.010-522
- Prepare for Oreon 11 (RP1)
