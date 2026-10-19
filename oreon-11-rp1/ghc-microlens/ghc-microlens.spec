%global source0_hash 04608e891112af94eb218b602e5edd5efa58bee9016764df914fa0bdb814bf65
%global pkg_name microlens
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.5.0.0
Release:        1%{?dist}
Summary:        A tiny lens library with no dependencies
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/microlens
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
NOTE: If you're writing an app, you probably want
<http://hackage.haskell.org/package/microlens-platform microlens-platform> – it
has the most features. <http://hackage.haskell.org/package/microlens microlens>
is intended more for library writers who want a tiny lens library (after all,
lenses are pretty useful for everything, not just for updating records!).

This library is an extract from <http://hackage.haskell.org/package/lens lens>
(with no dependencies). It's not a toy lenses library, unsuitable for “real
world”, but merely a small one. It is compatible with lens, and should have
same performance. It also has better documentation.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-microlens-devel -f %{oreon_filedir}/ghc-microlens-devel.list
%files -n ghc-microlens-doc -f %{oreon_filedir}/ghc-microlens-doc.list
%files -n ghc-microlens-prof -f %{oreon_filedir}/ghc-microlens-prof.list

%changelog

%autochangelog
