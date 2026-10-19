%global source1_hash 06d9df549d268b593db8eceafe54c29832f0b857b24ac6a936c50bc5211c0bce
%global source0_hash c784ddf43eca1d228aeef587008394918543b2c7ce18a71ee1453af0f5e0c1aa
%global pkg_name language-bluespec
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1
Release:        1%{?dist}
Summary:        An implementation of the Bluespec Haskell AST
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/language-bluespec
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-pretty-devel
BuildRequires:  ghc-pretty-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
# /oreon:deps
%description
This package contains an implementation of the <http://wiki.bluespec.com/
Bluespec> language's AST. In particular, this implements the Bluespec Haskell
(BH) syntax, also known as Bluespec Classic. We may add support for the
Bluespec SystemVerilog (BSV) syntax at a later date. To our knowledge, there is
no formal grammar that describes the syntax of BH or BSV, so this package is
based off of the code in the <https://github.com/B-Lang-org/bsc Bluespec
compiler>. Although the Bluespec compiler is written in Haskell, it is not
particularly simple to depend on the compiler as a library, so this package
exists to extract out the relevant compiler code into a simple-to-use library.

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
dos2unix -k -n %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-language-bluespec-devel -f %{oreon_filedir}/ghc-language-bluespec-devel.list
%files -n ghc-language-bluespec-doc -f %{oreon_filedir}/ghc-language-bluespec-doc.list
%files -n ghc-language-bluespec-prof -f %{oreon_filedir}/ghc-language-bluespec-prof.list

%changelog

%autochangelog
