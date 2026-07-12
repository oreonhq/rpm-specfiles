%global source0_hash 66fccca6c6f330e7ecc898bd6a51846e2145b3e02d78c4997ba6b7de23b551ee

Name:		perl-Test-CheckDeps
Summary:	Check for presence of dependencies
Version:	0.010
Release:	44%{?dist}
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Test-CheckDeps
Source0:	https://cpan.metacpan.org/modules/by-module/Test/Test-CheckDeps-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(CPAN::Meta) >= 2.120920
BuildRequires:	perl(CPAN::Meta::Check) >= 0.007
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl(List::Util)
BuildRequires:	perl(Test::Builder) >= 0.82
# Test Suite
BuildRequires:	perl(blib)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(IO::Handle)
BuildRequires:	perl(IPC::Open3)
BuildRequires:	perl(Test::More) >= 0.88
# Release tests
# perl-Pod-Coverage-TrustPod → perl-Pod-Eventual → perl-Mixin-Linewise → perl-YAML-Tiny → perl-Test-CheckDeps
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Pod::Coverage::TrustPod)
BuildRequires:	perl(Test::Pod) >= 1.41
BuildRequires:	perl(Test::Pod::Coverage) >= 1.08
%endif
# Dependencies
# (none)

Provides:       perl(Test::CheckDeps)
Provides:       perl(Test::CheckDeps)
%description
This module adds a test that assures all dependencies have been installed
properly. If requested, it can bail out all testing on error.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-CheckDeps-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test RELEASE_TESTING=1

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::CheckDeps.3*

%changelog
%autochangelog
