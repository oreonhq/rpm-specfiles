%global source1_hash eb75c5c3fe65e3f51fc160baef549226408b8454ea7d0abbf5c952ea21779222
%global source0_hash 12f2133c8e7a9d6e6e14821362d9af6b4d9db84fb99e2e9323225c4c4676c44e
%global pkg_name hoauth2
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global binaryinstances binary-instances-1.0.6
%global subpkgs %{binaryinstances}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        2.15.2
Release:        1%{?dist}
Summary:        Haskell OAuth2 authentication client
License:        MIT
URL:            https://hackage.haskell.org/package/hoauth2
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{binaryinstances}/%{binaryinstances}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-devel
BuildRequires:  ghc-base64-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-orphans-devel
BuildRequires:  ghc-binary-orphans-prof
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-http-conduit-devel
BuildRequires:  ghc-http-conduit-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-memory-devel
BuildRequires:  ghc-memory-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-compat-devel
BuildRequires:  ghc-time-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-uri-bytestring-aeson-devel
BuildRequires:  ghc-uri-bytestring-aeson-prof
BuildRequires:  ghc-uri-bytestring-devel
BuildRequires:  ghc-uri-bytestring-prof
BuildRequires:  ghc-vector-binary-instances-devel
BuildRequires:  ghc-vector-binary-instances-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This is Haskell binding of OAuth2 Authorization framework and Bearer Token
Usage framework.

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
%ghc_lib_subpackage -l BSD-3-Clause %{binaryinstances}
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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-hoauth2-devel -f %{oreon_filedir}/ghc-hoauth2-devel.list
%files -n ghc-hoauth2-doc -f %{oreon_filedir}/ghc-hoauth2-doc.list
%files -n ghc-hoauth2-prof -f %{oreon_filedir}/ghc-hoauth2-prof.list

%changelog

%autochangelog
