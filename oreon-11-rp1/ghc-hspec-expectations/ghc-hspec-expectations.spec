%global source1_hash 4237f094a7931202ff57ac6475542b0b314b50a7024550e2b6eb87cfb0d4ff93
%global source0_hash 7b8dde7e230ecfda90c95fd80478b244a45e68602fb3dd4a76f4710619be21ff
%global pkg_name hspec-expectations
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.8.4
Release:        1%{?dist}
Summary:        Catchy combinators for HUnit
License:        MIT
URL:            https://hackage.haskell.org/package/hspec-expectations
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HUnit-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-call-stack-devel
BuildRequires:  ghc-call-stack-prof
BuildRequires:  ghc-nanospec-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Catchy combinators for HUnit.

The three main primitives are shouldBe, shouldSatisfy and shouldThrow. They can
be used with HUnit, or any framework that integrates with HUnit, like
test-framework or Hspec.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-hspec-expectations-devel -f %{oreon_filedir}/ghc-hspec-expectations-devel.list
%files -n ghc-hspec-expectations-doc -f %{oreon_filedir}/ghc-hspec-expectations-doc.list
%files -n ghc-hspec-expectations-prof -f %{oreon_filedir}/ghc-hspec-expectations-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.8.4-1
- Prepare for Oreon 11 (RP1)
