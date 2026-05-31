%global source0_hash 390e60361d2c1c404463a46d496681b05458d50d811ee99282992b9b61ed6cf6

# Run optional test
%if ! (0%{?rhel})
%bcond_without perl_Test_MockModule_enables_optional_test
%else
%bcond_with perl_Test_MockModule_enables_optional_test
%endif

Name:           perl-Test-MockModule
Version:        0.180.0
Release:        3%{?dist}
Summary:        Override subroutines in a module for unit testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-MockModule
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-MockModule-v%{version}.tar.gz



BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build) >= 0.4234
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(Carp)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(SUPER) >= 1.20
BuildRequires:  perl(vars)
# Test Suite
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(Test::Warnings)
%if %{with perl_Test_MockModule_enables_optional_test}
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
BuildRequires:  perl(Test::Pod::Coverage) >= 1.00
%endif
# Dependencies
# (none)

%description
Test::MockModule lets you temporarily redefine subroutines in other packages
for the purposes of unit testing.

A Test::MockModule object is set up to mock subroutines for a given module. The
object remembers the original subroutine so it can easily be restored. This
happens automatically when all MockModule objects for the given module go out
of scope, or when you unmock() the subroutine.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-MockModule-v%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}

%check
./Build test

%files
%license LICENSE
%doc Changes README.md
%{perl_vendorlib}/Test/
%{_mandir}/man3/Test::MockModule.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.180.0-3
- Prepare for Oreon 11 (RP1)
