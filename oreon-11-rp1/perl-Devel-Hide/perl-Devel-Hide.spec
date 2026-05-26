# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 7830b4a57f7ec7410620d6c0150185449d7b4c9964c39a7dc397056032c32a08
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

# Run optional tests
%if ! (0%{?rhel}) || 0%{?oreon}
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
Source0:        https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Devel-Hide-0.0016.tar.gz

BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(lib)
# Module::CoreList is used from a private subroutine that is never called
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.82
%if %{with perl_Devel_Hide_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.18
BuildRequires:  perl(Test::Pod::Coverage) >= 1.04
%endif
# Dependencies
# (none)

%description
Given a list of Perl modules/filenames, this module makes require and use
statements fail (regardless of whether the specified files/modules are
installed or not).

%prep
%oreon_verify_sources
%setup -q -n Devel-Hide-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Devel/
%{_mandir}/man3/Devel::Hide.3*

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.0016-2
- Import
