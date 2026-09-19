%global source0_hash 6a081d8820dc85f0af3976b0e28a6332b0a6fd43642db8fb06598920a8d2ace8

# Perform optional tests
%bcond_without perl_constant_tiny_enables_optional_test

Name:           perl-constant-tiny
Version:        1.02
Release:        32%{?dist}
Summary:        Perl pragma to declare constants
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/constant-tiny
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SAPER/constant-tiny-%{version}.tar.gz
# Restore compatibility with Perl 5.32, bug #1851246, CPAN RT#131757.
Patch0:         constant-tiny-1.02-Fix-injecting-INC-constant.pm.patch
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
# Tests:
BuildRequires:  perl(Test::More)
BuildRequires:  perl(vars)
%if %{with perl_constant_tiny_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Checker)
BuildRequires:  perl(Test::Pod) >= 1.14
%endif
Requires:       perl(Carp)

%description
This module is a lightweight version of Perl standard constant.pm. Here are
the keys differences: it doesn't support Unicode names, it has stricter rules
about valid names.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n constant-tiny-%{version}
%patch -P0 -p1
%if !%{with perl_constant_tiny_enables_optional_test}
rm t/pod.t
perl -i -ne 'print $_ unless m{^t/pod\.t\b}' MANIFEST
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
%doc Changes eg README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
