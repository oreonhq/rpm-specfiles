%global source0_hash 60f3a814d2313f08e03e43d89870fa0bc83ff0b7a59674d71015a64e2badc023
%global pkg_name microlens-platform
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.4.4.2
Release:        1%{?dist}
Summary:        Microlens + all batteries included (best for apps)
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/microlens-platform
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-ghc-devel
BuildRequires:  ghc-microlens-ghc-prof
BuildRequires:  ghc-microlens-mtl-devel
BuildRequires:  ghc-microlens-mtl-prof
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
This package exports a module which is the recommended starting point for using
microlens if you aren't trying to keep your dependencies minimal.
By importing 'Lens.Micro.Platform' you get all functions and instances from
microlens, microlens-th, microlens-mtl, microlens-ghc, as well as
instances for 'Vector', 'Text', and 'HashMap'.

The minor and major versions of microlens-platform are incremented whenever the
minor and major versions of any other microlens package are incremented, so you
can depend on the exact version of microlens-platform without specifying the
version of microlens (microlens-mtl, etc) you need.

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
%files -n ghc-microlens-platform-devel -f %{oreon_filedir}/ghc-microlens-platform-devel.list
%files -n ghc-microlens-platform-doc -f %{oreon_filedir}/ghc-microlens-platform-doc.list
%files -n ghc-microlens-platform-prof -f %{oreon_filedir}/ghc-microlens-platform-prof.list

%changelog

%autochangelog
