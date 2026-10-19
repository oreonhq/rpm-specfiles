%global source0_hash c802f9ec4e05668e3eeb2cbb0a827f342854211315f9bb74c1e79253c589783b
%global pkg_name haskell-src-exts-util
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.5
Release:        1%{?dist}
Summary:        Helper functions for working with haskell-src-exts trees
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/haskell-src-exts-util
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-haskell-src-exts-devel
BuildRequires:  ghc-haskell-src-exts-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroups-devel
BuildRequires:  ghc-semigroups-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-uniplate-prof
# /oreon:deps
%description
A small suite of helper functions for working with haskell-src-exts:
- Free variables
- Bound variables
- Minimal (approximate) rebracketing of AST values such that prettyprint
  roundtrips.

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

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-haskell-src-exts-util-devel -f %{oreon_filedir}/ghc-haskell-src-exts-util-devel.list
%files -n ghc-haskell-src-exts-util-doc -f %{oreon_filedir}/ghc-haskell-src-exts-util-doc.list
%files -n ghc-haskell-src-exts-util-prof -f %{oreon_filedir}/ghc-haskell-src-exts-util-prof.list

%changelog

%autochangelog
