%global source0_hash 7e097074efb235115a7af03b14d9f99be8e8f8213a092c1e66870387b86c42bd
%global pkg_name haskell-src-exts
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.24.0
Release:        1%{?dist}
Summary:        Library for manipulating Haskell source
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/haskell-src-exts
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  happy
# /oreon:deps
%description
Haskell-Source with Extensions is an extension of the standard haskell-src
package, and handles most registered syntactic extensions to Haskell, including:
* Multi-parameter type classes with functional dependencies
* Indexed type families (including associated types)
* Empty data declarations
* GADTs
* Implicit parameters
* Template Haskell
and a few more. All extensions implemented in GHC are supported.
Apart from these standard extensions, it also handles regular patterns
as per the HaRP extension as well as HSX-style embedded XML syntax.

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-haskell-src-exts-devel -f %{oreon_filedir}/ghc-haskell-src-exts-devel.list
%files -n ghc-haskell-src-exts-doc -f %{oreon_filedir}/ghc-haskell-src-exts-doc.list
%files -n ghc-haskell-src-exts-prof -f %{oreon_filedir}/ghc-haskell-src-exts-prof.list

%changelog

%autochangelog
