%global source1_hash a6a4e6d7858cbcbcfd2949d1fc83184887d2ee482a6345b5b186c011ac361e97
%global source0_hash 76ae082a9f1950555dae8f1fb57ac6a7da85f30114b2f252dd2fa5e567fbbe0f
%global pkg_name bitwise
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.0.0.1
Release:        1%{?dist}
Summary:        Fast multi-dimensional unboxed bit packed Bool arrays
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/bitwise
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Unboxed multidimensional bit packed Bool arrays with fast aggregate operations
based on lifting Bool operations to bitwise operations.

There are many other bit packed structures out there, but none met all of these
requirements:

(1) unboxed bit packed Bool array,

(2) multi-dimensional indexing,

(3) fast (de)serialization, or interoperable with foreign code,

(4) fast aggregate operations (fold, map, zip).

Quick tour of the bitwise library:

[Data.Bits.Bitwise] Lift boolean operations on 'Bool' to bitwise operations on
'Data.Bits.Bits'.

[Data.Array.BitArray] Immutable bit arrays.

[Data.Array.BitArray.ST] Mutable bit arrays in 'Control.Monad.ST.ST'.

[Data.Array.BitArray.IO] Mutable bit arrays in 'IO'.

[Data.Array.BitArray.ByteString] (De)serialization.

[Codec.Image.PBM] Portable bitmap monochrome 2D image format.

Very rough performance benchmarks:

* immutable random access single bit reads: 'BitArray ix' is about 40% slower
than 'UArray ix Bool',

* 'Control.Monad.ST.ST' mutable random access single bit reads: 'STBitArray s
ix' is about the same as 'STUArray s ix Bool',

* immutable map 'Bool -> Bool': 'BitArray ix' is about 85x faster than 'UArray
ix Bool',

* immutable zipWith 'Bool -> Bool -> Bool': 'BitArray ix' is about 1300x faster
than 'UArray ix Bool'.

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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup
cabal-tweak-remove-upperbound QuickCheck

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
%files -n ghc-bitwise-devel -f %{oreon_filedir}/ghc-bitwise-devel.list
%files -n ghc-bitwise-doc -f %{oreon_filedir}/ghc-bitwise-doc.list
%files -n ghc-bitwise-prof -f %{oreon_filedir}/ghc-bitwise-prof.list

%changelog

%autochangelog
