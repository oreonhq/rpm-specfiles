%global source1_hash 4940cab94a15d469845ccf5225f9cb3d354c15e8127ebb58425c8b681f7721d9
%global source0_hash ca0e299fee6c0c918f45ce0907afbff1c3891998bb792d1717e4d5f12350ef0d
%global pkg_name hashtables
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.4.2
Release:        1%{?dist}
Summary:        Mutable hash tables in the ST monad
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/hashtables
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This package provides a couple of different implementations of mutable
hash tables in the ST monad, as well as a typeclass abstracting their
common operations, and a set of wrappers to use the hash tables in the
IO monad.

This package currently contains three hash table implementations:

1. Data.HashTable.ST.Basic contains a basic open-addressing hash table
using linear probing as the collision strategy.

2. Data.HashTable.ST.Cuckoo contains an implementation of "cuckoo hashing"
which has worst-case O(1) lookups and can reach a high "load factor".

3. Data.HashTable.ST.Linear contains a linear hash table, which trades
some insert and lookup performance for higher space efficiency and
much shorter delays when expanding the table.

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
2. "Data.HashTable.ST.Basic" contains a basic open-addressing hash table using
linear probing as the collision strategy. On a pure speed basis it should
currently be the fastest available Haskell hash table implementation for
lookups, although it has a higher memory overhead than the other tables and can
suffer from long delays when the table is resized because all of the elements
in the table need to be rehashed.

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
%files -n ghc-hashtables-devel -f %{oreon_filedir}/ghc-hashtables-devel.list
%files -n ghc-hashtables-doc -f %{oreon_filedir}/ghc-hashtables-doc.list
%files -n ghc-hashtables-prof -f %{oreon_filedir}/ghc-hashtables-prof.list

%changelog

%autochangelog
