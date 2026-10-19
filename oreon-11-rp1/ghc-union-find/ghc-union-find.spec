%global source1_hash 1fb8f475073188ad8f9020740300bdc66ede077bbd952f9bd98035e43e9efc47
%global source0_hash e6c2682bb8c06e8c43e360f45658d0eea17209cce84953e2a7d2f0240591f0ec
%global pkg_name union-find
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2
Release:        1%{?dist}
Summary:        Efficient union and equivalence testing of sets
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/union-find
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
Patch0:         https://github.com/hs-monadfail-st-remove/union-find/commit/34b1ca63aac10adf9434bb60fd3c45a8f6b6669d.patch
Patch1:         union-find-0.2-cabal-1.8.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
The Union/Find algorithm implements these operations in (effectively)
constant-time:

1. Check whether two elements are in the same equivalence class.

2. Create a union of two equivalence classes.

3. Look up the descriptor of the equivalence class.

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
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-dep-ver base '< 4.17' '< 4.21'

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-union-find-devel -f %{oreon_filedir}/ghc-union-find-devel.list
%files -n ghc-union-find-doc -f %{oreon_filedir}/ghc-union-find-doc.list
%files -n ghc-union-find-prof -f %{oreon_filedir}/ghc-union-find-prof.list

%changelog

%autochangelog
