%global source0_hash 5bcb8d356c509e359d53d869c07efdaa8fee5d6cf99897018b9a914ceb21222e

Name:           perl-Test-DiagINC
Version:        0.010
Release:        10%{?dist}
Summary:        List modules and versions loaded if tests fail
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0

URL:            https://metacpan.org/release/Test-DiagINC
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-DiagINC-%{version}.tar.gz

BuildArch:      noarch
# build requirements
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# runtime requirements
BuildRequires:  perl(B)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# test requrements
BuildRequires:  perl(Capture::Tiny) >= 0.21
BuildRequires:  perl(Config)
BuildRequires:  perl(Test::More)
Requires:       perl(B)
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(strict)
Requires:       perl(warnings)

%{?perl_default_filter}

%description
Assuming you shipped your module to CPAN with working tests, test failures
from CPAN Testers might be due to platform issues, Perl version issues or
problems with dependencies. This module helps you diagnose deep dependency
problems by showing you exactly what modules and versions were loaded
during a test run.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-DiagINC-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{make_build} test

%files
%doc Changes CONTRIBUTING.mkdn README examples
%license LICENSE
%{perl_vendorlib}/Test*
%{_mandir}/man3/Test*

%changelog
%autochangelog
