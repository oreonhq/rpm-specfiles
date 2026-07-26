%global source0_hash f45af2c73e686b7f57b2834128026e3d3b92d5c1345616ce410ce0e5f53e5626

%bcond_with network_tests

Name:		perl-Test-Kwalitee-Extra
Version:	0.4.0
Release:	27%{?dist}
Summary:	Run Kwalitee tests including optional indicators
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-Kwalitee-Extra
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-Kwalitee-Extra-v%{version}.tar.gz
Patch0:		Test-Kwalitee-Extra-v0.4.0-CPAN128602.patch
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Carp)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(MetaCPAN::Client)
BuildRequires:	perl(Module::CoreList) > 2.31
BuildRequires:	perl(Module::CPANTS::Analyse) >= 0.87
BuildRequires:	perl(Module::CPANTS::Kwalitee::Prereq)
BuildRequires:	perl(Module::Extract::Namespaces)
BuildRequires:	perl(strict)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(version) >= 0.77
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(English)
BuildRequires:	perl(File::Spec::Functions)
BuildRequires:	perl(FindBin)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(lib)
BuildRequires:	perl(Module::CPANTS::Kwalitee)
BuildRequires:	perl(Term::ANSIColor)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
# Author/Release Tests
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Perl::Critic)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
# Dependencies
# (none)

%description
CPANTS checks Kwalitee indicators, which is not quality but
automatically-measurable indicators of how good your distribution is.
Module::CPANTS::Analyse calculates Kwalitee but it is not directly applicable
to your module test. CPAN has already had Test::Kwalitee for the test module of
Kwalitee. It is, however, impossible to calculate prereq_matches_use indicator,
because dependent module Module::CPANTS::Analyse itself cannot calculate
prereq_matches_use indicator. It is marked as needs_db, but only limited
information is needed to calculate the indicator. This module calculates
prereq_matches_use by querying needed information from MetaCPAN.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Kwalitee-Extra-v%{version}

# Work around issues with M:C:A 1.00 (CPAN RT#128602)
%patch -P 0

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
%if !%{with network_tests}
mv t/{01-kwalitee,04-prereq_maches_use,05-build_prereq_matches_use,06-minperlver}.t ./
%endif

make test AUTHOR_TESTING=1 RELEASE_TESTING=1

%if !%{with network_tests}
mv ./{01-kwalitee,04-prereq_maches_use,05-build_prereq_matches_use,06-minperlver}.t t/
%endif

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Kwalitee::Extra.3*

%changelog
%autochangelog
