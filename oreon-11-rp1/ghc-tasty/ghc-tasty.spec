%global source2_hash 2065ef38e061551c7e3a997c4a4eac1b68dbf0553cc6177f01c8f7982f4cd375
%global source0_hash c76120141bd61c4418b3ed5efc5fe3094186d47cfe12d7be552320139f52c6c7
%global source1_hash ffc68736a3bbde3e8157710f29f4a99c0ca593c41194579c54a92c62f6c12ed8
%global pkg_name tasty
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global wcwidth wcwidth-0.0.2
%global subpkgs %{wcwidth}
Name:           ghc-%{pkg_name}
Version:        1.5.4
Release:        1%{?dist}
Summary:        Modern and extensible testing framework
License:        MIT
URL:            https://hackage.haskell.org/package/tasty
Source0:        https://hackage.haskell.org/package/tasty-%{version}/tasty-%{version}.tar.gz
Source1:        https://hackage.haskell.org/package/wcwidth-0.0.2/wcwidth-0.0.2.tar.gz
Source2:        https://hackage.haskell.org/package/tasty-%{version}/tasty.cabal#/tasty-%{version}.cabal
%ifarch %{ix86}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-ansi-terminal-devel
BuildRequires:  ghc-ansi-terminal-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
Tasty is a modern testing framework for Haskell. It lets you combine your unit
tests, golden tests, QuickCheck/SmallCheck properties, and any other types of
tests into a single test suite.

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
%ghc_lib_subpackage -l BSD-3-Clause %{wcwidth}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
dos2unix -k -n %{SOURCE2} %{pkg_name}.cabal
%autopatch -p1
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-tasty-devel -f %{oreon_filedir}/ghc-tasty-devel.list
%files -n ghc-tasty-doc -f %{oreon_filedir}/ghc-tasty-doc.list
%files -n ghc-tasty-prof -f %{oreon_filedir}/ghc-tasty-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.3-28
- Prepare for Oreon 11 (RP1)
