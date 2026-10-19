%global source0_hash c91620a5c9159bbd7adde183520eac22c2d06f4e076dffe4e0b8650191e5d8ca
%global pkg_name generic-deriving
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.14.7
Release:        1%{?dist}
Summary:        Generic programming library for generalised deriving
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/generic-deriving
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
# /oreon:deps
%description
This package provides functionality for generalising the deriving mechanism in
Haskell to arbitrary classes. It was first described in the paper:

* /A generic deriving mechanism for Haskell/. Jose Pedro Magalhaes, Atze
Dijkstra, Johan Jeuring, and Andres Loeh. Haskell'10.

The current implementation integrates with the new GHC Generics. See
<http://www.haskell.org/haskellwiki/GHC.Generics> for more information.
Template Haskell code is provided for supporting older GHCs.

This library is organized as follows:

* "Generics.Deriving.Base" defines the core functionality for GHC generics,
including the 'Generic(1)' classes and representation data types. On modern
versions of GHC, this simply re-exports "GHC.Generics" from 'base'. On older
versions of GHC, this module backports parts of "GHC.Generics" that were not
included at the time, including 'Generic(1)' instances.

* "Generics.Deriving.TH" implements Template Haskell functionality for deriving
instances of 'Generic(1)'.

* Educational code: in order to provide examples of how to define and use
"GHC.Generics"-based defaults, this library offers a number of modules which
define examples of type classes along with default implementations for the
classes' methods. Currently, the following modules are provided:
"Generics.Deriving.Copoint", "Generics.Deriving.ConNames",
"Generics.Deriving.Enum", "Generics.Deriving.Eq", "Generics.Deriving.Foldable",
"Generics.Deriving.Functor", "Generics.Deriving.Monoid",
"Generics.Deriving.Semigroup", "Generics.Deriving.Show",
"Generics.Deriving.Traversable", and "Generics.Deriving.Uniplate".

It is worth emphasizing that these modules are primarly intended for
educational purposes. Many of the classes in these modules resemble other
commonly used classes—for example, 'GShow' from "Generics.Deriving.Show"
resembles 'Show' from 'base'—but in general, the classes that
'generic-deriving' defines are not drop-in replacements. Moreover, the generic
defaults that 'generic-deriving' provide often make simplifying assumptions
that may violate expectations of how these classes might work elsewhere.
For example, the generic default for 'GShow' does not behave exactly like
'deriving Show' would.

If you are seeking "GHC.Generics"-based defaults for type classes in 'base',
consider using the '<http://hackage.haskell.org/package/generic-data
generic-data>' library.

* "Generics.Deriving.Default" provides newtypes that allow leveraging the
generic defaults in this library using the 'DerivingVia' GHC language
extension.

* "Generics.Deriving" re-exports "Generics.Deriving.Base",
"Generics.Deriving.Default", and a selection of educational modules.

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
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-generic-deriving-devel -f %{oreon_filedir}/ghc-generic-deriving-devel.list
%files -n ghc-generic-deriving-doc -f %{oreon_filedir}/ghc-generic-deriving-doc.list
%files -n ghc-generic-deriving-prof -f %{oreon_filedir}/ghc-generic-deriving-prof.list

%changelog

%autochangelog
