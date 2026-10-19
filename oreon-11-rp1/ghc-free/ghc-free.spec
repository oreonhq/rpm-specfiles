%global source1_hash 39ca01645f7c2f08ffd64226891c514bdc924a87da48f815f9fe77c2e0ac1164
%global source0_hash 72867f7c89173263765736e8d395e94291f1aaea626ecb1d673d72ce90b94f89
%global pkg_name free
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        5.2
Release:        1%{?dist}
Summary:        Monads for free
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/free
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-distributive-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-indexed-traversable-devel
BuildRequires:  ghc-indexed-traversable-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Free monads are useful for many tree-like structures and domain specific
languages.

If 'f' is a 'Functor' then the free 'Monad' on 'f' is the type of trees whose
nodes are labeled with the constructors of 'f'. The word "free" is used in the
sense of "unrestricted" rather than "zero-cost": 'Free f' makes no constraining
assumptions beyond those given by 'f' and the definition of 'Monad'.
As used here it is a standard term from the mathematical theory of adjoint
functors.

Cofree comonads are dual to free monads. They provide convenient ways to talk
about branching streams and rose-trees, and can be used to annotate syntax
trees. The cofree comonad can be seen as a stream parameterized by a 'Functor'
that controls its branching factor.

More information on free monads, including examples, can be found in the
following blog posts: <https://ekmett.github.io/reader/2008/monads-for-free/>
<https://ekmett.github.io/reader/2011/free-monads-for-less/>.

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
%files -n ghc-free-devel -f %{oreon_filedir}/ghc-free-devel.list
%files -n ghc-free-doc -f %{oreon_filedir}/ghc-free-doc.list
%files -n ghc-free-prof -f %{oreon_filedir}/ghc-free-prof.list

%changelog

%autochangelog
