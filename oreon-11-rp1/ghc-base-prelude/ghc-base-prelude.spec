%global source0_hash 8108af03f2c9d6dc4fe9e7033afc53f0472d1e520261cef0ec3e420b29521dd3
%global pkg_name base-prelude
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.6.1.1
Release:        1%{?dist}
Summary:        Featureful preludes formed solely from the "base" package
License:        MIT
URL:            https://hackage.haskell.org/package/base-prelude
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
A library which aims to reexport all the non-conflicting and most general
definitions from the "base" package. This includes APIs for applicatives,
arrows, monoids, foldables, traversables, exceptions, generics, ST, MVars and
STM. This package will never have any dependencies other than "base".
Besides a rich prelude it provides limited ones like "BasePrelude.DataTypes",
which only exports the data-types defined across the "base" package, and
"BasePrelude.Operators", which only exports the common operators.
/Versioning policy/ The versioning policy of this package deviates from PVP in
the sense that its exports in part are transitively determined by the version
of "base". Therefore it's recommended for the users of "base-prelude" to
specify the bounds of "base" as well.

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
%files -n ghc-base-prelude-devel -f %{oreon_filedir}/ghc-base-prelude-devel.list
%files -n ghc-base-prelude-doc -f %{oreon_filedir}/ghc-base-prelude-doc.list
%files -n ghc-base-prelude-prof -f %{oreon_filedir}/ghc-base-prelude-prof.list

%changelog

%autochangelog
