%global source1_hash f0b1b514dfc085281d0b4b9338fc0bd0c1d25ee77306f2a144ffe012b0afef8c
%global source0_hash 6423597d3528ac66c54beaab9f5408429c0a29b8cb98c45a1645f255aef7fef0
%global pkg_name indexed-traversable
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.5
Release:        1%{?dist}
Summary:        FunctorWithIndex, FoldableWithIndex, TraversableWithIndex
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/indexed-traversable
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
This package provides three useful generalizations:

'class Functor f => FunctorWithIndex i f | f -> i' (imap)

'class Foldable f => FoldableWithIndex i f | f -> i' (ifoldMap)

'class (FunctorWithIndex i t, FoldableWithIndex i t, Traversable t) =>
TraversableWithIndex i t | t -> i' (itraverse)

This package contains instances for types in GHC boot libraries.
For some additional instances see indexed-traversable-instances.

The keys package provides similar functionality,
but uses (associated) 'TypeFamilies' instead of 'FunctionalDependencies'.

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
This package provides the Haskell %{pkg_name} library
documentation.
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

%files -f %{oreon_filedir}/main.list
%files -n ghc-indexed-traversable-devel -f %{oreon_filedir}/ghc-indexed-traversable-devel.list
%files -n ghc-indexed-traversable-doc -f %{oreon_filedir}/ghc-indexed-traversable-doc.list
%files -n ghc-indexed-traversable-prof -f %{oreon_filedir}/ghc-indexed-traversable-prof.list

%changelog

%autochangelog
