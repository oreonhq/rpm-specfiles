%global source0_hash ace11cb7ccffa98a2b124fa039eef9a35854303b53915e65c339a9504a72ff5e
%global pkg_name managed
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.0.11
Release:        1%{?dist}
Summary:        A monad for managed values
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/managed
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
In Haskell you very often acquire values using the 'with...' idiom using
functions of type '(a -> IO r) -> IO r'. This idiom forms a 'Monad', which is a
special case of the 'ContT' monad (from 'transformers') or the 'Codensity'
monad (from 'kan-extensions'). The main purpose behind this package is to
provide a restricted form of these monads specialized to this unusually common
case.

The reason this package defines a specialized version of these types is to:

* be more beginner-friendly,
* simplify inferred types and error messages, and:
* provide some additional type class instances that would otherwise be orphan
instances.

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
%files -n ghc-managed-devel -f %{oreon_filedir}/ghc-managed-devel.list
%files -n ghc-managed-doc -f %{oreon_filedir}/ghc-managed-doc.list
%files -n ghc-managed-prof -f %{oreon_filedir}/ghc-managed-prof.list

%changelog

%autochangelog
