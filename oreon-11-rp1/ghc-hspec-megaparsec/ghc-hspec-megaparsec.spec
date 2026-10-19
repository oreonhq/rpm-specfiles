%global source0_hash 65f4f57f96c05fce5f55e8ad6aafcf4f2e5726d95d74855a95d6779927936a2d
%global pkg_name hspec-megaparsec
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        2.2.1
Release:        1%{?dist}
Summary:        Utility functions for testing Megaparsec parsers with Hspec
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/hspec-megaparsec
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-hspec-expectations-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Utility functions for testing Megaparsec parsers with Hspec.

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
%files -n ghc-hspec-megaparsec-devel -f %{oreon_filedir}/ghc-hspec-megaparsec-devel.list
%files -n ghc-hspec-megaparsec-doc -f %{oreon_filedir}/ghc-hspec-megaparsec-doc.list
%files -n ghc-hspec-megaparsec-prof -f %{oreon_filedir}/ghc-hspec-megaparsec-prof.list

%changelog

%autochangelog
