%global source2_hash 3ec12de580ee31ceac89b314fd00b5057ed40198c0b3d9e9dafa54c1941e6942
%global source0_hash 28f203c786cbf8ac6dc3fea3378ec36f34173d505fb4a1dd60fc8418ad91c423
%global source1_hash d0f507334bdea5431a2f07f525a97f29e76522c32210f5de6d5a2b4f1d42bf7c
%global pkg_name vector
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global vectorstream vector-stream-0.1.0.1
%global subpkgs %{vectorstream}
Name:           ghc-%{pkg_name}
Version:        0.13.2.0
Release:        7%{?dist}
Summary:        Efficient Arrays
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/vector
Source0:        https://hackage.haskell.org/package/vector-%{version}/vector-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/vector-stream-0.1.0.1/vector-stream-0.1.0.1.tar.gz
Source2:        https://hackage.haskell.org/package/vector-%{version}/vector.cabal#/vector-%{version}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-prof
# /oreon:deps
%description
An efficient implementation of Int-indexed arrays (both mutable
and immutable), with a powerful loop optimisation framework.

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
%ghc_lib_subpackage -l BSD-3-Clause %{vectorstream}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
( cd %{vectorstream}
  cabal-tweak-dep-ver base '< 4.20' '< 4.21'
  cabal-tweak-dep-ver ghc-prim '< 0.12' '< 0.13'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-vector-devel -f %{oreon_filedir}/ghc-vector-devel.list
%files -n ghc-vector-doc -f %{oreon_filedir}/ghc-vector-doc.list
%files -n ghc-vector-prof -f %{oreon_filedir}/ghc-vector-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.13.2.0-7
- Prepare for Oreon 11 (RP1)
