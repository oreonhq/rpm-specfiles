%global source0_hash 7332b323913eb6a2684d094755196304b2f8606f70eaab913654ca91f273eac2

# Perform optional tests
%bcond_without perl_Test_Dir_enables_optional_test

Name:           perl-Test-Dir
Version:        1.16
Release:        28%{?dist}
Summary:        Some simple tests on directories and folders
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Dir
Source0:        https://cpan.metacpan.org/authors/id/M/MT/MTHURN/Test-Dir-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(lib)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Path) >= 2.07
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
%if %{with perl_Test_Dir_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif

%description
This modules provides a collection of test utilities for directory and folder
attributes. Use it in combination with Test::More in your test programs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Dir-%{version}
rm -r inc
perl -i -ne 'print $_ unless m{^inc/}' MANIFEST
%if !%{with perl_Test_Dir_enables_optional_test}
rm -r t/pod*.t
perl -i -ne 'print $_ unless m{^t/pod.\.t}' MANIFEST
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
