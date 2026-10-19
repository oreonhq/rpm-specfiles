%global source1_hash e7a8c6412ffa14debd61c16b77eb416a3e0bbce0418ae682e86e1575c84b6258
%global source0_hash 4ea6ae36d093d31d29611cf9f77b7582ba24d09e5fa136dc3bf99e7772e46281
%global pkg_name monad-par
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.3.6
Release:        1%{?dist}
Summary:        A library for parallel programming based on a monad
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/monad-par
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-abstract-deque-devel
BuildRequires:  ghc-abstract-deque-prof
BuildRequires:  ghc-abstract-par-devel
BuildRequires:  ghc-abstract-par-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-monad-par-extras-devel
BuildRequires:  ghc-monad-par-extras-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-mwc-random-prof
BuildRequires:  ghc-parallel-devel
BuildRequires:  ghc-parallel-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
The 'Par' monad offers a simple API for parallel programming. The library works
for parallelising both pure and 'IO' computations, although only the pure
version is deterministic. The default implementation provides a work-stealing
scheduler and supports forking tasks that are much lighter weight than
IO-threads.

For complete documentation see "Control.Monad.Par".

Some examples of use can be found in the 'examples/' directory of the source
package.

Other related packages:

* 'abstract-par' provides the type classes that abstract over different
implementations of the 'Par' monad.

* 'monad-par-extras' provides extra combinators and monad transformers layered
on top of the 'Par' monad.

Changes in 0.3.4 relative to 0.3:

* Fix bugs that cause "thread blocked indefinitely on MVar" crashes.

* Added "Control.Monad.Par.IO".

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

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-monad-par-devel -f %{oreon_filedir}/ghc-monad-par-devel.list
%files -n ghc-monad-par-doc -f %{oreon_filedir}/ghc-monad-par-doc.list
%files -n ghc-monad-par-prof -f %{oreon_filedir}/ghc-monad-par-prof.list

%changelog

%autochangelog
