%global source1_hash c152c3b72328987f10dd0e2007c703404787e29d0947cad7d033a223a506bbd3
%global source0_hash 9667bc4a1aa3ca672d6322721288cbc924429582d9fd3197c8b1dab25f8fb54f
%global pkg_name servant-client
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.20.3.0
Release:        1%{?dist}
Summary:        Automatic derivation of querying functions for servant
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/servant-client
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-base-compat-devel
BuildRequires:  ghc-base-compat-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-entropy-devel
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-generics-sop-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-media-devel
BuildRequires:  ghc-http-media-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-kan-extensions-devel
BuildRequires:  ghc-kan-extensions-prof
BuildRequires:  ghc-markdown-unlit
BuildRequires:  ghc-markdown-unlit-devel
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-servant-client-core-devel
BuildRequires:  ghc-servant-client-core-prof
BuildRequires:  ghc-servant-devel
BuildRequires:  ghc-servant-prof
BuildRequires:  ghc-servant-server-devel
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-warp-devel
# /oreon:deps
%description
This library lets you derive automatically Haskell functions that let you query
each endpoint of a <http://hackage.haskell.org/package/servant servant>
webservice.

See <http://docs.servant.dev/en/stable/tutorial/Client.html the client section
of the tutorial>.

<https://github.com/haskell-servant/servant/blob/master/servant-client/CHANGELOG.md
CHANGELOG>.

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
%files -n ghc-servant-client-devel -f %{oreon_filedir}/ghc-servant-client-devel.list
%files -n ghc-servant-client-doc -f %{oreon_filedir}/ghc-servant-client-doc.list
%files -n ghc-servant-client-prof -f %{oreon_filedir}/ghc-servant-client-prof.list

%changelog

%autochangelog
