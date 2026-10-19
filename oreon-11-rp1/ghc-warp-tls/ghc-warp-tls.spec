%global source1_hash 8632dfb2fdde3c5c688c02bcc77a02da076a9c852987a16bf321dfa83d5d66c1
%global source0_hash 9554c08c45091b0da85364d30f30b13f333afce9e146a7d3559db0dbaab9b713
%global pkg_name warp-tls
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        3.4.14
Release:        1%{?dist}
Summary:        HTTP over TLS support for Warp via the TLS package
License:        MIT
URL:            https://hackage.haskell.org/package/warp-tls
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-recv-devel
BuildRequires:  ghc-recv-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-tls-devel
BuildRequires:  ghc-tls-prof
BuildRequires:  ghc-tls-session-manager-devel
BuildRequires:  ghc-tls-session-manager-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
# /oreon:deps
%description
SSLv1 and SSLv2 are obsoleted by IETF. We should use TLS 1.2 (or TLS 1.1 or TLS
1.0 if necessary). HTTP/2 can be negotiated by ALPN. API docs and the README
are available at <http://www.stackage.org/package/warp-tls>.

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
%files -n ghc-warp-tls-devel -f %{oreon_filedir}/ghc-warp-tls-devel.list
%files -n ghc-warp-tls-doc -f %{oreon_filedir}/ghc-warp-tls-doc.list
%files -n ghc-warp-tls-prof -f %{oreon_filedir}/ghc-warp-tls-prof.list

%changelog

%autochangelog
