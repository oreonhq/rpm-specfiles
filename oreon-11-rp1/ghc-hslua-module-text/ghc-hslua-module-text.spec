%global source0_hash 15ac6f05bca6ca0e4f984d19193ac9aa3a466012a48172733a5dd76242acd62e
%global pkg_name hslua-module-text
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.2.0
Release:        1%{?dist}
Summary:        Lua module for text
License:        MIT
URL:            https://hackage.haskell.org/package/hslua-module-text
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hslua-core-devel
BuildRequires:  ghc-hslua-core-prof
BuildRequires:  ghc-hslua-marshalling-devel
BuildRequires:  ghc-hslua-marshalling-prof
BuildRequires:  ghc-hslua-packaging-devel
BuildRequires:  ghc-hslua-packaging-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
UTF-8 aware subset of Lua's `string` module.

This package is part of HsLua, a Haskell framework built around the embeddable
scripting language <https://lua.org Lua>.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-hslua-module-text-devel -f %{oreon_filedir}/ghc-hslua-module-text-devel.list
%files -n ghc-hslua-module-text-doc -f %{oreon_filedir}/ghc-hslua-module-text-doc.list
%files -n ghc-hslua-module-text-prof -f %{oreon_filedir}/ghc-hslua-module-text-prof.list

%changelog

%autochangelog
