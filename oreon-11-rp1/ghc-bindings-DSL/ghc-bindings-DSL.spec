%global source0_hash d7eeb19d330d0a14479c226afa902df47a8b71b6a207f0dd145bd28e0427abe5
%global pkg_name bindings-DSL
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.1.0
Release:        1%{?dist}
Summary:        FFI domain specific language, on top of hsc2hs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/bindings-DSL
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This is a set of macros to be used when writing Haskell FFI. They were designed
to be able to fully describe C interfaces, so that hsc2hs can extract from them
all Haskell code needed to mimic such interfaces. All Haskell names used are
automatically derived from C names, structures are mapped to Haskell instances
of Storable, and there are also macros you can use with C code to help write
bindings to inline functions or macro functions. Documentation is available at
package homepage:

<https://github.com/jwiegley/bindings-dsl/wiki>

The extra module Bindings.Utilities will contain tools that may be convenient
when working with FFI.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-bindings-DSL-devel -f %{oreon_filedir}/ghc-bindings-DSL-devel.list
%files -n ghc-bindings-DSL-doc -f %{oreon_filedir}/ghc-bindings-DSL-doc.list
%files -n ghc-bindings-DSL-prof -f %{oreon_filedir}/ghc-bindings-DSL-prof.list

%changelog

%autochangelog
