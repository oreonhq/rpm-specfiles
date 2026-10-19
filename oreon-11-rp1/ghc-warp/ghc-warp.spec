%global source1_hash 8daf77c57f529503dd3038efc3813a8001032ed810bdddff0acb0faca039b721
%global source0_hash 7dd09b9f2f868e4647fe96162f063a99da791a0e57479d1ea74b210ecb8b2f17
%global pkg_name warp
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global recv recv-0.1.1
%global subpkgs %{recv}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        3.4.16
Release:        1%{?dist}
Summary:        A fast, light-weight web server for WAI applications
License:        MIT
URL:            https://hackage.haskell.org/package/warp
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{recv}/%{recv}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-auto-update-devel
BuildRequires:  ghc-auto-update-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bsb-http-chunked-devel
BuildRequires:  ghc-bsb-http-chunked-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-date-devel
BuildRequires:  ghc-http-date-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-http2-devel
BuildRequires:  ghc-http2-prof
BuildRequires:  ghc-iproute-devel
BuildRequires:  ghc-iproute-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-simple-sendfile-devel
BuildRequires:  ghc-simple-sendfile-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-manager-devel
BuildRequires:  ghc-time-manager-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-word8-devel
BuildRequires:  ghc-word8-prof
# /oreon:deps
%description
HTTP/1.0, HTTP/1.1 and HTTP/2 are supported. For HTTP/2, Warp supports direct
and ALPN (in TLS) but not upgrade.

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
%ghc_lib_subpackage -l BSD-3-Clause %{recv}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup
cabal-tweak-drop-dep bytestring-builder

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-warp-devel -f %{oreon_filedir}/ghc-warp-devel.list
%files -n ghc-warp-doc -f %{oreon_filedir}/ghc-warp-doc.list
%files -n ghc-warp-prof -f %{oreon_filedir}/ghc-warp-prof.list

%changelog

%autochangelog
