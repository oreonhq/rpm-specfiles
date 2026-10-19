%global source0_hash 42781e9943a7a215e662c4973b9feafdc019fd16469bdb849a8537ee58956273
Name:           perl-Test-Deep
Version:        1.205
Release:        3%{?dist}
Summary:        Extremely flexible deep comparison
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Deep
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-Deep-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Test::Builder)
Provides:       perl(Test::Deep)
Provides:       perl(Test::Deep::NoTest)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::Builder)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)
BuildRequires:  perl(base)
BuildRequires:  perl(if)
BuildRequires:  perl(lib)
BuildRequires:  perl(overload)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test::Deep gives you very flexible ways to check that the result you
got is the result you were expecting. At its simplest it compares two
structures by going through each level, ensuring that the values
match, that arrays and hashes have the same elements and that
references are blessed into the correct class. It also handles
circular data structures without getting caught in an infinite loop.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-Deep-%{version}

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

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.205-3
- Prepare for Oreon 11 (RP1)
