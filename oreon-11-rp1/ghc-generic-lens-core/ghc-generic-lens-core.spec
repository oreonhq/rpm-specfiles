%global source1_hash 8837e26a0ed6b7c7872bcdabe610ba329d880c7a9c99b5e4bcb9348d46639738
%global source0_hash 1d31236d072e408e59bfa1dd88659293646ee381f639f33b6a49bce48d525ae0
%global pkg_name generic-lens-core
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.3.0.0
Release:        1%{?dist}
Summary:        Generically derive traversals, lenses and prisms
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/generic-lens-core
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-indexed-profunctors-devel
BuildRequires:  ghc-indexed-profunctors-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This library uses GHC.Generics to derive efficient optics (traversals, lenses
and prisms) for algebraic data types in a type-directed way, with a focus on
good type inference and error messages when possible.

This package is the shared internal logic of the
'<https://hackage.haskell.org/package/generic-lens generic-lens>' and
'<https://hackage.haskell.org/package/generic-optics generic-optics>'
libraries.

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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-generic-lens-core-devel -f %{oreon_filedir}/ghc-generic-lens-core-devel.list
%files -n ghc-generic-lens-core-doc -f %{oreon_filedir}/ghc-generic-lens-core-doc.list
%files -n ghc-generic-lens-core-prof -f %{oreon_filedir}/ghc-generic-lens-core-prof.list

%changelog

%autochangelog
