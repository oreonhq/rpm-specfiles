%global source0_hash bc38ac7f009cae15f0a0fbf4a5aaa38fbbcb1fc8db513eaeba0d70b91464e5f1
%global pkg_name hspec
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.11.18
Release:        1%{?dist}
Summary:        A Testing Framework for Haskell
License:        MIT
URL:            https://hackage.haskell.org/package/hspec
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hspec-core-devel
BuildRequires:  ghc-hspec-core-prof
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-hspec-discover-prof
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-hspec-expectations-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Hspec is a testing framework for Haskell. Some of Hspec's distinctive features
are:

* a friendly DSL for defining tests

* integration with QuickCheck, SmallCheck, and HUnit

* parallel test execution

* automatic discovery of test files

The Hspec Manual is at <https://hspec.github.io/>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development files.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-hspec-devel -f %{oreon_filedir}/ghc-hspec-devel.list
%files -n ghc-hspec-doc -f %{oreon_filedir}/ghc-hspec-doc.list
%files -n ghc-hspec-prof -f %{oreon_filedir}/ghc-hspec-prof.list

%changelog

%autochangelog
