%global source0_hash da34ef9029f6849d6026201d49127d054ee6ac4b979c82210315f5721964a96f
Name:           perl-Test-FailWarnings
Version:        0.008
Release:        37%{?dist}
Summary:        Add test failures if warnings are caught
License:        Apache-2.0
URL:            https://metacpan.org/release/Test-FailWarnings
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-%{version}.tar.gz
BuildArch:      noarch
%{?perl_default_filter}
Provides:       perl(Test::FailWarnings)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Capture::Tiny)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Cwd)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More's
fail() calls. It is designed to be used with done_testing, when you don't
need to know the test count in advance.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-FailWarnings-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.008-37
- Prepare for Oreon 11 (RP1)
