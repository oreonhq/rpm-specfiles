%global source1_hash a67f89b5533b1148ad465dc7f24baeed2e2e9e7d81d2a147fc7fa8ff1089ca4d
%global source0_hash 63949799ffd10675ef70ea701c1eb63e618629b3b2f7b25f07c5a966e24e77f4
%global pkg_name serialise
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.6.1
Release:        1%{?dist}
Summary:        A binary serialisation library for Haskell values
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/serialise
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
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cborg-devel
BuildRequires:  ghc-cborg-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-half-devel
BuildRequires:  ghc-half-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-strict-devel
BuildRequires:  ghc-strict-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This package (formerly 'binary-serialise-cbor') provides pure, efficient
serialization of Haskell values directly into 'ByteString's for storage or
transmission purposes. By providing a set of type class instances, you can also
serialise any custom data type you have as well.

The underlying binary format used is the 'Concise Binary Object
Representation', or CBOR, specified in RFC 7049. As a result, serialised
Haskell values have implicit structure outside of the Haskell program itself,
meaning they can be inspected or analyzed without custom tools.

An implementation of the standard bijection between CBOR and JSON is provided
by the [cborg-json](/package/cborg-json) package. Also see
[cbor-tool](/package/cbor-tool) for a convenient command-line utility for
working with CBOR data.

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

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-serialise-devel -f %{oreon_filedir}/ghc-serialise-devel.list
%files -n ghc-serialise-doc -f %{oreon_filedir}/ghc-serialise-doc.list
%files -n ghc-serialise-prof -f %{oreon_filedir}/ghc-serialise-prof.list

%changelog

%autochangelog
