%global source0_hash 1956efbb1047b9f5fc646f7d68ceeafbf335aae7e6fe154eba9f86871738b796
%global pkg_name HsOpenSSL-x509-system
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.0.4
Release:        1%{?dist}
Summary:        Use the system's native CA certificate store with HsOpenSSL
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/HsOpenSSL-x509-system
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         HsOpenSSL-x509-system-ca-bundle.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HsOpenSSL-devel
BuildRequires:  ghc-HsOpenSSL-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
A cross-platform library that tries to find a (reasonable) CA certificate
bundle that can be used with 'HsOpenSSL' to verify the certificates of remote
peers.

This package is for 'HsOpenSSL' what 'x509-system' is for the 'tls' package.
Additionally, it borrows some ideas from 'x509-system'.

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
# End cabal-rpm setup
%patch -P0 -p1 -b .orig

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-HsOpenSSL-x509-system-devel -f %{oreon_filedir}/ghc-HsOpenSSL-x509-system-devel.list
%files -n ghc-HsOpenSSL-x509-system-doc -f %{oreon_filedir}/ghc-HsOpenSSL-x509-system-doc.list
%files -n ghc-HsOpenSSL-x509-system-prof -f %{oreon_filedir}/ghc-HsOpenSSL-x509-system-prof.list

%changelog

%autochangelog
