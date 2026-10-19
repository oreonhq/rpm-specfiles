%global source2_hash 94988e14281fa9c70714fbae5e32031f7008919c13b060ee16c714edb62858c0
%global source1_hash f7a606ad5df4a07459986364f7d739eb653495fbbe1d7158582fb29a4584bfb9
%global source0_hash 261bf3d2b93b519a7901266af43d7d454b65aac4ac8fb4e113c68de4db131473
%global pkg_name singleton-bool
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global some some-1.0.6
%global subpkgs %{some}
Name:           ghc-%{pkg_name}
Version:        0.1.8
Release:        7%{?dist}
Summary:        Type level booleans
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/singleton-bool
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{some}/%{some}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-boring-devel
BuildRequires:  ghc-boring-prof
BuildRequires:  ghc-dec-devel
BuildRequires:  ghc-dec-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros-extra
# /oreon:deps
%description
Type level booleans.

'singletons' package provides similar functionality, but it has tight
dependency constraints.

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
%ghc_lib_subpackage -l BSD-3-Clause %{some}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
cp -bp %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
( cd %{some}
  cabal-tweak-dep-ver base '<4.20' '<4.21'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-singleton-bool-devel -f %{oreon_filedir}/ghc-singleton-bool-devel.list
%files -n ghc-singleton-bool-doc -f %{oreon_filedir}/ghc-singleton-bool-doc.list
%files -n ghc-singleton-bool-prof -f %{oreon_filedir}/ghc-singleton-bool-prof.list

%changelog

%autochangelog
