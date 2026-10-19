%global source0_hash 6ba4de60779eb1989db5ceb445059fd2b2e58c293c3d25b9d5548c02ff6b36b0
%global pkg_name microlens-ghc
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.4.15.2
Release:        1%{?dist}
Summary:        Microlens + array, bytestring, containers, transformers
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/microlens-ghc
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-microlens-devel
BuildRequires:  ghc-microlens-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Use this package instead of <http://hackage.haskell.org/package/microlens
microlens> if you don't mind depending on all dependencies here –
'Lens.Micro.GHC' reexports everything from 'Lens.Micro' and additionally
provides orphan instances of microlens classes for packages coming with GHC
(<http://hackage.haskell.org/package/array array>,
<http://hackage.haskell.org/package/bytestring bytestring>,
<http://hackage.haskell.org/package/containers containers>,
<http://hackage.haskell.org/package/transfromers transformers>).

The minor and major versions of microlens-ghc are incremented whenever the
minor and major versions of microlens are incremented, so you can depend on the
exact version of microlens-ghc without specifying the version of microlens you
need.

This package is a part of the <http://hackage.haskell.org/package/microlens
microlens> family; see the readme
<https://github.com/stevenfontanella/microlens#readme on Github>.

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
%files -n ghc-microlens-ghc-devel -f %{oreon_filedir}/ghc-microlens-ghc-devel.list
%files -n ghc-microlens-ghc-doc -f %{oreon_filedir}/ghc-microlens-ghc-doc.list
%files -n ghc-microlens-ghc-prof -f %{oreon_filedir}/ghc-microlens-ghc-prof.list

%changelog

%autochangelog
