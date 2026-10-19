%global source0_hash 9d53ddfdc964cd8454cb0da4c695b6a3ae47b45839291c34cb9d8d1cfaab3202
Name:           perl-Test-Memory-Cycle
Version:        1.06
Release:        30%{?dist}
Summary:        Check for memory leaks and circular memory references
License:        Artistic-2.0
URL:            https://metacpan.org/release/Test-Memory-Cycle
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Memory-Cycle-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Devel::Cycle) >= 1.07
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Devel::Cycle\\)$
Provides:       perl(Test::Memory::Cycle)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(Devel::Cycle)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::Builder::Tester)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Perl's garbage collection has one big problem: Circular references
can't get cleaned up.  A circular reference can be as simple as two
objects that refer to each other.

"Test::Memory::Cycle" is built on top of "Devel::Cycle" to give you an
easy way to check for these circular references.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Memory-Cycle-%{version}

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
