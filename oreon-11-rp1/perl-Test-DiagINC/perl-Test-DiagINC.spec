%global source0_hash 5bcb8d356c509e359d53d869c07efdaa8fee5d6cf99897018b9a914ceb21222e
Name:           perl-Test-DiagINC
Version:        0.010
Release:        1%{?dist}
Summary:        List modules and versions loaded if tests fail
License:        Apache-2.0
URL:            https://metacpan.org/release/Test-DiagINC
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-DiagINC-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(B)
Requires:       perl(Cwd)
Requires:       perl(File::Spec)
Requires:       perl(strict)
Requires:       perl(warnings)
%{?perl_default_filter}
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(B)
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Config)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

%{make_build} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
