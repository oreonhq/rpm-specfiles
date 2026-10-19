%global source0_hash 6deda0788c73d33e723d203d02926c213de7b24e2b8960eeb5e58c85b8b06853
%global pkg_name deriving-compat
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.6.8
Release:        1%{?dist}
Summary:        Backports of GHC deriving extensions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/deriving-compat
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-ghc-boot-th-devel
BuildRequires:  ghc-ghc-boot-th-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-th-abstraction-devel
BuildRequires:  ghc-th-abstraction-prof
# /oreon:deps
%description
'deriving-compat' provides Template Haskell functions that mimic 'deriving'
extensions that were introduced or modified in recent versions of GHC.
Currently, the following typeclasses/extensions are covered:

* Deriving 'Bounded'

* Deriving 'Enum'

* Deriving 'Ix'

* Deriving 'Eq'

* Deriving 'Ord'

* Deriving 'Read'

* Deriving 'Show'

* 'DeriveFoldable'

* 'DeriveFunctor'

* 'DeriveTraversable'

* 'GeneralizedNewtypeDeriving' (with GHC 8.2 or later)

* 'DerivingVia' (with GHC 8.2 or later)

See the "Data.Deriving" module for a full list of backported changes.

In addition, 'deriving-compat' also provides some additional 'deriving'
functionality that has not yet been merged into upstream GHC. Aside from the
GHC 'deriving' extensions mentioned above, 'deriving-compat' also permits
deriving instances of classes in the 'Data.Functor.Classes' module, covering
the 'Eq1', 'Eq2', 'Ord1', 'Ord2', 'Read1', 'Read2', 'Show1', and 'Show2'
classes. This extra functionality is outside of the main scope of
'deriving-compat', as it does not backport extensions that exist in today's
GHC. Nevertheless, the underlying Template Haskell machinery needed to derive
'Eq' and friends extends very naturally to 'Eq1' and friends, so this extra
functionality is included in 'deriving-compat' as a convenience.

Note that some recent GHC typeclasses/extensions are not covered by this
package:

* 'DeriveDataTypeable'

* 'DeriveGeneric', which was introducted in GHC 7.2 for deriving 'Generic'
instances, and modified in GHC 7.6 to allow derivation of 'Generic1' instances.
Use 'Generics.Deriving.TH' from
'<http://hackage.haskell.org/package/generic-deriving generic-deriving>' to
derive 'Generic(1)' using Template Haskell.

* 'DeriveLift', which was introduced in GHC 8.0 for deriving 'Lift' instances.
Use 'Language.Haskell.TH.Lift' from
'<http://hackage.haskell.org/package/th-lift th-lift>' to derive 'Lift' using
Template Haskell.

* The 'Bifunctor' typeclass, which was introduced in GHC 7.10, as well as the
'Bifoldable' and 'Bitraversable' typeclasses, which were introduced in GHC 8.2.
Use 'Data.Bifunctor.TH' from '<http://hackage.haskell.org/package/bifunctors
bifunctors>' to derive these typeclasses using Template Haskell.

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
%files -n ghc-deriving-compat-devel -f %{oreon_filedir}/ghc-deriving-compat-devel.list
%files -n ghc-deriving-compat-doc -f %{oreon_filedir}/ghc-deriving-compat-doc.list
%files -n ghc-deriving-compat-prof -f %{oreon_filedir}/ghc-deriving-compat-prof.list

%changelog

%autochangelog
