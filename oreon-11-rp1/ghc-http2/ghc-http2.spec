%global source3_hash 7cc49e6168f0da25e2d1701396c1617734c404b8ea4b892e9d893a696ff9ee2f
%global source2_hash 05d40d381e5c72beefb209b7e82877b457fbca2880e60ed849bad480b6795b10
%global source1_hash 9ccee90bcbbfb29f30f7aed063c62edf0f3eb084ba63dbf9baffbd5db573714f
%global source0_hash 242b2811d376fed626f65eadbdbf6d4fe09908824930cdbe50e089f5cfe59c79
%global pkg_name http2
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global httpsemantics http-semantics-0.3.0
%global networkcontrol network-control-0.1.7
%global subpkgs %{httpsemantics} %{networkcontrol}
Name:           ghc-%{pkg_name}
Version:        5.4.6
Release:        1%{?dist}
Summary:        HTTP/2 library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/http2
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{httpsemantics}/%{httpsemantics}.tar.gz
Source2:        https://hackage.haskell.org/package/%{networkcontrol}/%{networkcontrol}.tar.gz
Source3:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-byte-order-devel
BuildRequires:  ghc-network-byte-order-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-psqueues-devel
BuildRequires:  ghc-psqueues-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-time-manager-prof
BuildRequires:  ghc-unix-time-devel
BuildRequires:  ghc-unix-time-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
# /oreon:deps
%description
HTTP/2 library including frames, priority queues, HPACK, client and server.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{httpsemantics}
%ghc_lib_subpackage -l BSD-3-Clause %{networkcontrol}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2
dos2unix -k -n %{SOURCE3} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-http2-devel -f %{oreon_filedir}/ghc-http2-devel.list
%files -n ghc-http2-doc -f %{oreon_filedir}/ghc-http2-doc.list
%files -n ghc-http2-prof -f %{oreon_filedir}/ghc-http2-prof.list

%changelog

%autochangelog
