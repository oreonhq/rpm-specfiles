%global source1_hash 1da9fd92e9577d26e73a046996d1b9ea20bc25963df118403102a6556df1694c
%global source0_hash cad8f45180f7d375262f72887be5f48f4ec55e34b381b5cb71269f006e91500e
%global pkg_name foldl
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch s390x
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        1.4.18
Release:        1%{?dist}
Summary:        Composable, streaming, and efficient left folds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/foldl
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-doctest-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This library provides strict left folds that stream in constant memory, and you
can combine folds using 'Applicative' style to derive new folds.
Derived folds still traverse the container just once and are often as efficient
as hand-written folds.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-foldl-devel -f %{oreon_filedir}/ghc-foldl-devel.list
%files -n ghc-foldl-doc -f %{oreon_filedir}/ghc-foldl-doc.list
%files -n ghc-foldl-prof -f %{oreon_filedir}/ghc-foldl-prof.list

%changelog

%autochangelog
