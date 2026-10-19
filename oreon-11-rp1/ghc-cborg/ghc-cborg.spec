%global source1_hash 47c044ade185e59433ec301fd3d85c7a1b9709cc752daf8b6388c9190aa618aa
%global source0_hash 17fe070c38fc498cab49bcb9d6215b7747d53bedf96502e9bcce9cad73b9c797
%global pkg_name cborg
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.10.0
Release:        1%{?dist}
Summary:        Concise Binary Object Representation (CBOR)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cborg
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
Patch0:         https://patch-diff.githubusercontent.com/raw/well-typed/cborg/pull/337.patch
Patch1:         cborg-Magic-ix86.patch
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-ghc-bignum-devel
BuildRequires:  ghc-ghc-bignum-prof
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-half-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-vector-devel
# /oreon:deps
%description
This package provides an efficient implementation of the Concise Binary Object
Representation (CBOR), as specified by [RFC
7049](https://tools.ietf.org/html/rfc7049).

If you are looking for a library for serialisation of Haskell values, have a
look at the [serialise](/package/serialise) package, which is built upon this
library.

An implementation of the standard bijection between CBOR and JSON is provided
by the [cborg-json](/package/cborg-json) package. Also see
[cbor-tool](/package/cbor-tool) for a convenient command-line utility for
working with CBOR data.

This package was formerly known as 'binary-serialise-cbor'.

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
cabal-tweak-remove-upperbound QuickCheck
%ifarch %{ix86}
%patch -P0 -p2 -b .orig
%patch -P1 -p1
%endif

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
%files -n ghc-cborg-devel -f %{oreon_filedir}/ghc-cborg-devel.list
%files -n ghc-cborg-doc -f %{oreon_filedir}/ghc-cborg-doc.list
%files -n ghc-cborg-prof -f %{oreon_filedir}/ghc-cborg-prof.list

%changelog

%autochangelog
