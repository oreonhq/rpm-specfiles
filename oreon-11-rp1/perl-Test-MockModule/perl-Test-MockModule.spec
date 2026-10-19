%global source0_hash 92e6de1caf40c38d5557ad2192e1a34f7a518a9101bc6af953b23bcfcffc52d3
%bcond_with perl_Test_MockModule_enables_optional_test
Name:           perl-Test-MockModule
Version:        0.185.3
Release:        1%{?dist}
Summary:        Override subroutines in a module for unit testing
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-MockModule
Source0:        https://cpan.metacpan.org/authors/id/G/GF/GFRANKS/Test-MockModule-v%{version}.tar.gz
BuildArch:      noarch
%if %{with perl_Test_MockModule_enables_optional_test}
%endif
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(Carp)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(SUPER)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Warnings)
BuildRequires:  perl(lib)
BuildRequires:  perl(parent)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
