%global source2_hash c97aa3bbf4a3660e8b39684b9136f20c3e15dc0e52e792e2daea34f2999e3467
%global source1_hash 87bffd2254b98ded822d449fcd1c33dbd74d2ce96bf35e7a6714abc5a2297265
%global source0_hash 616a1c2176097469f9514e76d979fffdbc12d569f44fd01deb14377c7888797e
%global pkg_name generics-sop
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global sopcore sop-core-0.5.0.2
%global subpkgs %{sopcore}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.5.1.4
Release:        24%{?dist}
Summary:        Generic Programming using True Sums of Products
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/generics-sop
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{sopcore}/%{sopcore}.tar.gz
Source2:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
# /oreon:deps
%description
A library to support the definition of generic functions. Datatypes are viewed
in a uniform, structured way: the choice between constructors is represented
using an n-ary sum, and the arguments of each constructor are represented using
an n-ary product.

The module "Generics.SOP" is the main module of this library and contains more
detailed documentation.

Since version 0.4.0.0, this package is now based on
'<https://hackage.haskell.org/package/sop-core sop-core>'. The core package
contains all the functionality of n-ary sums and products, whereas this package
provides the datatype-generic programming support on top.

Examples of using this library are provided by the following packages:

* '<https://hackage.haskell.org/package/basic-sop basic-sop>' basic examples,

* '<https://hackage.haskell.org/package/pretty-sop pretty-sop>' generic pretty
printing,

* '<https://hackage.haskell.org/package/lens-sop lens-sop>' generically
computed lenses,

* '<https://hackage.haskell.org/package/json-sop json-sop>' generic JSON
conversions.

A detailed description of the ideas behind this library is provided by the
paper:

* Edsko de Vries and Andres Löh.
<http://www.andres-loeh.de/TrueSumsOfProducts True Sums of Products>.
Workshop on Generic Programming (WGP) 2014.

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
%ghc_lib_subpackage -l BSD-3-Clause %{sopcore}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1
cp -bp %{SOURCE2} %{pkg_name}.cabal
# End cabal-rpm setup
(
cd %{sopcore}
cabal-tweak-dep-ver base '< 4.17' '< 4.21'
cabal-tweak-dep-ver deepseq '< 1.5' '< 1.6'
)

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-generics-sop-devel -f %{oreon_filedir}/ghc-generics-sop-devel.list
%files -n ghc-generics-sop-doc -f %{oreon_filedir}/ghc-generics-sop-doc.list
%files -n ghc-generics-sop-prof -f %{oreon_filedir}/ghc-generics-sop-prof.list

%changelog

%autochangelog
