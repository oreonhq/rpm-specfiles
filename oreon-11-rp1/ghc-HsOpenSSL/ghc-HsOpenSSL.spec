%global source1_hash d04d57342c8af431f9b53d74448428d71818b3ea564af2e871a28dfb31a0d88d
%global source0_hash 78be4c69a2af5a08555efa6e4e7f58b74e0a9bf78e11560f1e6fb3a209f9d4ba
%global pkg_name HsOpenSSL
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.11.7.11
Release:        1%{?dist}
Summary:        Partial OpenSSL binding for Haskell
License:        CC0-1.0
URL:            https://hackage.haskell.org/package/HsOpenSSL
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  openssl-devel
# /oreon:deps
%description
HsOpenSSL is an OpenSSL binding for Haskell. It can generate RSA and DSA keys,
read and write PEM files, generate message digests, sign and verify messages,
encrypt and decrypt messages. It has also some capabilities of creating SSL
clients and servers.

This package is in production use by a number of Haskell based systems and stable.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openssl-devel%{?_isa}
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

%define cabal_configure_options --ghc-option="-optc=-Wno-incompatible-pointer-types"
%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-HsOpenSSL-devel -f %{oreon_filedir}/ghc-HsOpenSSL-devel.list
%files -n ghc-HsOpenSSL-doc -f %{oreon_filedir}/ghc-HsOpenSSL-doc.list
%files -n ghc-HsOpenSSL-prof -f %{oreon_filedir}/ghc-HsOpenSSL-prof.list

%changelog

%autochangelog
