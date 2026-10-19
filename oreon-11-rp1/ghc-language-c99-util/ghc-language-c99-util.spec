%global source0_hash 241b4ffce7339744eeb0b92d22814d04c6d137467a0e2f172dbec66d3e474633
%global pkg_name language-c99-util
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.0
Release:        1%{?dist}
Summary:        Utilities for language-c99
License:        MIT
URL:            https://hackage.haskell.org/package/language-c99-util
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-ieee754-devel
BuildRequires:  ghc-ieee754-prof
BuildRequires:  ghc-language-c99-devel
BuildRequires:  ghc-language-c99-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This library contains a number of utility functions and wrappers for the
'language-c99' package. For an actual high-level approach to writing C99
programs, see 'language-c99-simple'.

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
%files -n ghc-language-c99-util-devel -f %{oreon_filedir}/ghc-language-c99-util-devel.list
%files -n ghc-language-c99-util-doc -f %{oreon_filedir}/ghc-language-c99-util-doc.list
%files -n ghc-language-c99-util-prof -f %{oreon_filedir}/ghc-language-c99-util-prof.list

%changelog

%autochangelog
