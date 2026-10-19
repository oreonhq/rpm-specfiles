%global source0_hash 45c11c728e022770f646db40d85f5ab3223f1fa2297f59f73e4b60ba1f489154
%bcond_without perl_Convert_Age_enables_optional_tests
Name:       perl-Convert-Age
Version:    0.04
Release:        37%{?dist}
Summary:        Perl module that converts integer seconds into a "compact" form and back
License:    GPL-1.0-or-later OR Artistic-1.0-Perl
URL:        https://metacpan.org/release/Convert-Age
Source0:        https://cpan.metacpan.org/authors/id/C/CF/CFEDDE/Convert-Age-%{version}.tar.gz
BuildArch:  noarch
%if !%{with perl_Convert_Age_enables_optional_tests}
%endif
%if %{with perl_Convert_Age_enables_optional_tests}
%endif
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This is a rather simple Perl module for dealing with time intervals.
Convert 189988007 seconds to compact form 6y7d10h26m47s.
Convert compact 5h37m5s to seconds 20225.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-Age-%{version}
%if !%{with perl_Convert_Age_enables_optional_tests}
rm t/pod*.t
perl -i -ne 'print $_ unless m{^t/pod.*\.t}' MANIFEST
%endif

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
