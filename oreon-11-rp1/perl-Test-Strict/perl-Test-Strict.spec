%global source0_hash f6807517823a90a96b40deeaed9aa080082ded4b50a51204f5be1e7ce774c85c

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_Strict_enables_optional_test
%else
%bcond_with perl_Test_Strict_enables_optional_test
%endif

Name:           perl-Test-Strict
Version:        0.54
Release:        4%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Check syntax, presence of use strict/warnings, and test coverage
Source:         https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-%{version}.tar.gz
Url:            https://metacpan.org/release/Test-Strict
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Config)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::Builder)
# Tests only
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::More)
# Optional tests only
%if %{with perl_Test_Strict_enables_optional_test}
BuildRequires:  perl(Moose::Autobox)
BuildRequires:  perl(Test::CheckManifest) >= 1.28
BuildRequires:  perl(Test::DistManifest) >= 1.012
BuildRequires:  perl(Test::Version) >= 1.003001
BuildRequires:  perl(Test::Pod) >= 1.48
BuildRequires:  perl(Test::Pod::Coverage) >= 1.10
%endif

Provides:       perl(Test::Strict)
%description
"Test::Strict" lets you check the syntax, presence of "use strict;" and
"use warnings;" in your perl code.  It reports its results in standard 
"Test::Simple" fashion. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Strict-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
find . -type f -name '*.list' -delete
make test

%files
%license LICENSE
%doc README Changes 
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test::Strict*

%changelog
%autochangelog
