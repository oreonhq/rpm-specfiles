%global source0_hash e0355da0a89afe100168ac1851e2bc53c83738f0db387a53038b1978829aad25

Summary:        Test case module for Perl
Name:           perl-Test-Manifest
Version:        2.026
Release:        3%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Manifest
Source0:        https://www.cpan.org/modules/by-module/Test/Test-Manifest-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(lib)
BuildRequires:  perl(Test::More) >= 1
BuildRequires:  perl(version) >= 0.86
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage)
# Dependencies
Requires:       perl(File::Spec)
Requires:       perl(Test::Harness)

Provides:       perl(Test::Manifest)
%description
MakeMaker assumes that you want to run all of the .t files in the t/ directory
in ASCII-betical order during make test unless you say otherwise. This leads to
some interesting naming schemes for test files to get them in the desired
order.

You can specify any order or any files that you like, though, with the test
directive to WriteMakefile.

Test::Manifest looks in the t/test_manifest file to find out which tests you
want to run and the order in which you want to run them. It constructs the
right value for MakeMaker to do the right thing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Manifest-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README.pod SECURITY.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::Manifest.3*

%changelog
%autochangelog
