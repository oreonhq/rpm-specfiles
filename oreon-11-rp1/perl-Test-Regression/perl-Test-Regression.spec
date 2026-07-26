%global source0_hash 21f9f74bcf9d0685e7a5021b4abb99ab557a9b6fffbef9607349c5adaa41c9fb

Name:           perl-Test-Regression
Version:        0.08
Release:        28%{?dist}
Summary:        Test library that can generate outputs and compare against them
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Regression
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Regression-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(FileHandle)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Module)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DirHandle)
BuildRequires:  perl(English)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
# Optional tests:
# Test::CheckChanges not used
# Test::CheckManifest not used
BuildRequires:  perl(Test::MockObject::Extends)
# Test::Perl::Critic not used
# Test::Pod not used
# Test::Pod::Coverage not used
# Test::Prereq::Build not used
# Test::Spelling not used

%{?perl_default_filter}

%description
Using the various Test:: modules you can compare the output of a function
against what you expect. However if the output is complex and changes from
version to version, maintenance of the expected output could be costly.
This module allows one to use the test code to generate the expected
output, so that if the differences with model output are expected, one can
easily refresh the model output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Regression-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset TEST_AUTHOR TEST_REGRESSION_GEN
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
