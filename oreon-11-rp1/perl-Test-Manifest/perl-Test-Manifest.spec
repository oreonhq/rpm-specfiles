%global source0_hash e0355da0a89afe100168ac1851e2bc53c83738f0db387a53038b1978829aad25
Summary:        Test case module for Perl
Name:           perl-Test-Manifest
Version:        2.026
Release:        1%{?dist}
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Manifest
Source0:        https://www.cpan.org/modules/by-module/Test/Test-Manifest-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(File::Spec)
Requires:       perl(Test::Harness)
Provides:       perl(Test::Manifest)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(base)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
