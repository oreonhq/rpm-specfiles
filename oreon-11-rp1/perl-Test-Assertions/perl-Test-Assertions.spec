%global source0_hash fcdce41d57273881581adf680a20a6adf51a4c3b7e31c3f69866fb9109370280
Name:           perl-Test-Assertions
Version:        1.054
Release:        48%{?dist}
Summary:        Simple set of building blocks for both unit and runtime testing
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Test-Assertions
Source0:        https://cpan.metacpan.org/authors/id/B/BB/BBC/Test-Assertions-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp)
Requires:       perl(File::Compare)
Requires:       perl(File::Spec)
Requires:       perl(IO::CaptureOutput)
Requires:       perl(Test::More)
Provides:       perl(Test::Assertions)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Compare)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Getopt::Std)
BuildRequires:  perl(Log::Trace)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Assertions provides a convenient set of tools for constructing tests,
such as unit tests or run-time assertion checks (like C's ASSERT macro).
Unlike some of the Test:: modules available on CPAN, Test::Assertions is
not limited to unit test scripts; for example it can be used to check
output is as expected within a benchmarking script. When it is used for
unit tests, it generates output in the standard form for CPAN unit testing
(under Test::Harness).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Assertions-%{version}

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
