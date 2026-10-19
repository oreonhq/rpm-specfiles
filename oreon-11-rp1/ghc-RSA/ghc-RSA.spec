%global source1_hash d2e711da52c19e332d374b3c0202a77d3088b59a0ba64abe6107569752fd1e24
%global source0_hash 72c5d8c45ef1013e0e8aff763bb8894df0f022f28e698e33ae87bbdb33d69041
%global pkg_name RSA
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.4.1
Release:        1%{?dist}
Summary:        Implementation of RSA, using the padding schemes of PKCS#1 v2.1
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/RSA
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-crypto-api-prof
BuildRequires:  ghc-crypto-pubkey-types-devel
BuildRequires:  ghc-crypto-pubkey-types-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This library implements the RSA encryption and signature algorithms for
arbitrarily-sized ByteStrings. While the implementations work, they are not
necessarily the fastest ones on the planet. Particularly key generation.
The algorithms included are based of RFC 3447, or the Public-Key Cryptography
Standard for RSA, version 2.1 (a.k.a, PKCS#1 v2.1).

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
%files -n ghc-RSA-devel -f %{oreon_filedir}/ghc-RSA-devel.list
%files -n ghc-RSA-doc -f %{oreon_filedir}/ghc-RSA-doc.list
%files -n ghc-RSA-prof -f %{oreon_filedir}/ghc-RSA-prof.list

%changelog

%autochangelog
