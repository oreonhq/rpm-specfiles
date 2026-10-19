%global source1_hash f52626e8789a9918cb389383c6ecfbba898c94e1790b6fc7991a4e256350489b
%global source0_hash f4e16ecf010fd681a56e6216ab1bd429f3c9bc962ec032e32cfd23e374e97498
%global pkg_name pipes
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        4.3.16
Release:        1%{?dist}
Summary:        Compositional pipelines
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/pipes
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mmorph-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-void-devel
BuildRequires:  ghc-void-prof
# /oreon:deps
%description
Pipes is a clean and powerful stream processing library that lets you build
and connect reusable streaming components

Advantages over traditional streaming libraries:
* Concise API: Use simple commands like 'for', ('>->'), 'await', and 'yield'
* Blazing fast: Implementation tuned for speed, including shortcut fusion
* Lightweight Dependency: pipes is small and compiles very rapidly,
  including dependencies
* Elegant semantics: Use practical category theory
* ListT: Correct implementation of ListT that interconverts with pipes
* Bidirectionality: Implement duplex channels
* Extensive Documentation: Second to none!

Import "Pipes" to use the library.
Read "Pipes.Tutorial" for an extensive tutorial.

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
%files -n ghc-pipes-devel -f %{oreon_filedir}/ghc-pipes-devel.list
%files -n ghc-pipes-doc -f %{oreon_filedir}/ghc-pipes-doc.list
%files -n ghc-pipes-prof -f %{oreon_filedir}/ghc-pipes-prof.list

%changelog

%autochangelog
