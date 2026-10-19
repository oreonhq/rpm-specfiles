%global source0_hash f6807517823a90a96b40deeaed9aa080082ded4b50a51204f5be1e7ce774c85c
%bcond_with perl_Test_Strict_enables_optional_test
Name:           perl-Test-Strict
Version:        0.54
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Summary:        Check syntax, presence of use strict/warnings, and test coverage
Source0:        https://cpan.metacpan.org/authors/id/M/MA/MANWAR/Test-Strict-%{version}.tar.gz
Url:            https://metacpan.org/release/Test-Strict
BuildArch:      noarch
%if %{with perl_Test_Strict_enables_optional_test}
%endif
Provides:       perl(Test::Strict)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Config)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(ExtUtils::Manifest)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

find . -type f -name '*.list' -delete
make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
