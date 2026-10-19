%global source1_hash 626bdec7c925fb0f15896dcc776992cb00a5fcf99211528c13e7535e72396e3a
%global source0_hash f76daa44a80d423c849d5fb552e2a20b1e2f47b638c889a34cb1a5bd1ab08d21
%global pkg_name kan-extensions
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global invariant invariant-0.6.5
%global subpkgs %{invariant}
Name:           ghc-%{pkg_name}
Version:        5.2.8
Release:        6%{?dist}
Summary:        Kan extensions, Kan lifts, the Yoneda lemma, and (co)density (co)monads
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/kan-extensions
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{invariant}/%{invariant}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-StateVar-devel
BuildRequires:  ghc-StateVar-prof
BuildRequires:  ghc-adjunctions-devel
BuildRequires:  ghc-adjunctions-prof
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-distributive-devel
BuildRequires:  ghc-distributive-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-free-devel
BuildRequires:  ghc-free-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-profunctors-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
# /oreon:deps
%description
Kan extensions, Kan lifts, various forms of the Yoneda lemma, and (co)density
(co)monads.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-2-Clause %{invariant}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-kan-extensions-devel -f %{oreon_filedir}/ghc-kan-extensions-devel.list
%files -n ghc-kan-extensions-doc -f %{oreon_filedir}/ghc-kan-extensions-doc.list
%files -n ghc-kan-extensions-prof -f %{oreon_filedir}/ghc-kan-extensions-prof.list

%changelog

%autochangelog
