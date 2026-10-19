%global source1_hash f597208acc42ac1a68b968a4006f5c6cde9358dca5ee8ca989fe73633785b7a3
%global source0_hash 29a71456f8d33a1c2236b52dd8031f09d80912617cc5f0073d951c98136fbd1e
%global pkg_name tls-session-manager
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global cryptotoken crypto-token-0.1.2
%global subpkgs %{cryptotoken}
Name:           ghc-%{pkg_name}
Version:        0.1.0
Release:        1%{?dist}
Summary:        In-memory TLS session DB and session ticket
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/tls-session-manager
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cryptotoken}/%{cryptotoken}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-auto-update-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-clock-devel
BuildRequires:  ghc-clock-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-network-byte-order-devel
BuildRequires:  ghc-network-byte-order-prof
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-psqueues-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-serialise-devel
BuildRequires:  ghc-serialise-prof
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
# /oreon:deps
%description
TLS session manager with limitation, automatic pruning, energy saving and
replay resistance and session ticket manager.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{cryptotoken}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-tls-session-manager-devel -f %{oreon_filedir}/ghc-tls-session-manager-devel.list
%files -n ghc-tls-session-manager-doc -f %{oreon_filedir}/ghc-tls-session-manager-doc.list
%files -n ghc-tls-session-manager-prof -f %{oreon_filedir}/ghc-tls-session-manager-prof.list

%changelog

%autochangelog
