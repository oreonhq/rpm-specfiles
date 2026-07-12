%global source0_hash 43678d2f670b241e9568b4e4f45aa42aa79bb2350d0d804c830392aeff6f54c4

# Perform optional tests
%if 0%{?rhel} >= 10
%bcond_with perl_Test_CheckChanges_enables_optional_test
%else
%bcond_without perl_Test_CheckChanges_enables_optional_test
%endif

Name:		perl-Test-CheckChanges
Summary:	Check that the Changes file matches the distribution
Version:	0.14
Release:	45%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-CheckChanges
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-CheckChanges-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Cwd)
BuildRequires:	perl(File::Basename)
BuildRequires:	perl(File::Glob)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Module::Build::Version)
BuildRequires:	perl(Test::Builder)
# Test Suite
BuildRequires:	perl(English)
BuildRequires:	perl(Test::More) >= 0.88
%if %{with perl_Test_CheckChanges_enables_optional_test}
# Optional Tests
BuildRequires:	perl(Perl::Critic::Policy::NamingConventions::Capitalization)
BuildRequires:	perl(Perl::Critic::Policy::ValuesAndExpressions::ProhibitMagicNumbers)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.00
BuildRequires:	perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
Requires:	perl(Module::Build::Version)

Provides:       perl(Test::CheckChanges)
%description
This module checks that your Changes file has an entry for the current version
of the Module being tested. The version information for the distribution being
tested is taken out of the Build data, or if that is not found, out of the
Makefile. It then attempts to open, in order, a file with the name Changes or
CHANGES. The Changes file is then parsed for version numbers. If one and only
one of the version numbers matches, the test passes; otherwise the test fails.
A message with the current version is printed if the test passes; otherwise
diagnostic messages are printed to help explain the failure.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-CheckChanges-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
%if %{with perl_Test_CheckChanges_enables_optional_test}
export TEST_AUTHOR=1
%endif
./Build test

%files
%doc Changes examples/ README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CheckChanges.3*

%changelog
%autochangelog
