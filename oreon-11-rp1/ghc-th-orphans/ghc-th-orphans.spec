%global source0_hash 9c67fb484c9f1e7f761ed7de453f73c087c4c46123d9bf41a9038156aa5e9062
%global pkg_name th-orphans
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch armv7hl
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        0.13.17
Release:        1%{?dist}
Summary:        Orphan instances for TH datatypes
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/th-orphans
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-compat-devel
BuildRequires:  ghc-th-compat-prof
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-th-reify-many-devel
BuildRequires:  ghc-th-reify-many-prof
# /oreon:deps
%description
Orphan instances for TH datatypes. In particular, instances for Ord and Lift,
as well as a few missing Show / Eq. These instances used to live in
haskell-src-meta, and that's where the version number started.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-th-orphans-devel -f %{oreon_filedir}/ghc-th-orphans-devel.list
%files -n ghc-th-orphans-doc -f %{oreon_filedir}/ghc-th-orphans-doc.list
%files -n ghc-th-orphans-prof -f %{oreon_filedir}/ghc-th-orphans-prof.list

%changelog

%autochangelog
