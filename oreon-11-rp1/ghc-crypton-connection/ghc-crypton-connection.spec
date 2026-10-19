%global source2_hash f8b985e88618f3b457a6b588cda7d27b0adf753bc339093b8da99dfb73671dd7
%global source1_hash a836087e5c277413c79e6d94a7bf346bfb61eaffb2f55555875c76dfeca69f3b
%global source0_hash d686b7855817ea8c4bc8def79b78bc24aef725973e82a8afd109d528c9c54034
%global pkg_name crypton-connection
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global cryptonsocks crypton-socks-0.6.2
%global subpkgs %{cryptonsocks}
Name:           ghc-%{pkg_name}
Version:        0.4.6
Release:        1%{?dist}
Summary:        Simple and easy network connection API
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/crypton-connection
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{cryptonsocks}/%{cryptonsocks}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
Obsoletes:      ghc-connection < %{version}-%{release}
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-x509-store-devel
BuildRequires:  ghc-crypton-x509-store-prof
BuildRequires:  ghc-crypton-x509-system-devel
BuildRequires:  ghc-crypton-x509-system-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
# /oreon:deps
%description
Simple network library for all your connection needs.

Features: Really simple to use, SSL/TLS, SOCKS.

This library provides a very simple api to create sockets to a destination with
the choice of SSL/TLS, and SOCKS.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      ghc-connection-devel < %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
Obsoletes:      ghc-connection-doc < %{version}-%{release}
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
Obsoletes:      ghc-connection-prof < %{version}-%{release}
%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{cryptonsocks}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-crypton-connection-devel -f %{oreon_filedir}/ghc-crypton-connection-devel.list
%files -n ghc-crypton-connection-doc -f %{oreon_filedir}/ghc-crypton-connection-doc.list
%files -n ghc-crypton-connection-prof -f %{oreon_filedir}/ghc-crypton-connection-prof.list

%changelog

%autochangelog
