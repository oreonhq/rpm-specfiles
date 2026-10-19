%global source1_hash 627fe0c379b4548cc1344057cb388d46e26cad77dd8dcc0b93531691c59756ae
%global source0_hash 8917d1041232165f090c9200af07dd98e793fb89e2e0bc0a83ea900f309feb25
%global pkg_name vector-space
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.19
Release:        1%{?dist}
Summary:        Vector and affine spaces, linear maps, and derivatives
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/vector-space
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Boolean-devel
BuildRequires:  ghc-Boolean-prof
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-MemoTrie-devel
BuildRequires:  ghc-MemoTrie-prof
BuildRequires:  ghc-NumInstances-devel
BuildRequires:  ghc-NumInstances-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Classes and generic operations for vector spaces and affine spaces.
It also defines a type of infinite towers of generalized derivatives.
A generalized derivative is a linear transformation rather than one of
the common concrete representations (scalars, vectors, matrices, ...).

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-vector-space-devel -f %{oreon_filedir}/ghc-vector-space-devel.list
%files -n ghc-vector-space-doc -f %{oreon_filedir}/ghc-vector-space-doc.list
%files -n ghc-vector-space-prof -f %{oreon_filedir}/ghc-vector-space-prof.list

%changelog

%autochangelog
