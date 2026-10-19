%global source0_hash 7830b4a57f7ec7410620d6c0150185449d7b4c9964c39a7dc397056032c32a08
%if ! (0%{?rhel}) || (0%{?oreon} >= 11)
%bcond_without perl_Devel_Hide_enables_optional_test
%else
%bcond_with perl_Devel_Hide_enables_optional_test
%endif
Name:           perl-Devel-Hide
Version:        0.0016
Release:        2%{?dist}
Summary:        Forces the unavailability of specified Perl modules (for testing)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-Hide
Source0:        https://cpan.metacpan.org/modules/by-module/Devel/Devel-Hide-%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Devel_Hide_enables_optional_test}
%endif
Provides:       perl(Devel::Hide)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(ExtUtils::MakeMaker)
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
Given a list of Perl modules/filenames, this module makes require and use
statements fail (regardless of whether the specified files/modules are
installed or not).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Devel-Hide-%{version}

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

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0016-2
- Import
