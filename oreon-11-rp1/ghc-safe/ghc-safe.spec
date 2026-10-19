%global source1_hash b928ea1645876788155b38ce85c7e46d157a1bb41d2b05f5770b13d60bc6a3f7
%global source0_hash 2c81fea42bbe79ec488774043c1ec54f30efba059df9a4f3681ce83d85007f01
%global pkg_name safe
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 0
Name:           ghc-%{pkg_name}
Version:        0.3.21
Release:        1%{?dist}
Summary:        Library of safe (exception free) functions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/safe
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
A library wrapping 'Prelude'/'Data.List' functions that can throw exceptions,
such as 'head' and '!!'. Each unsafe function has up to four variants, e.g.
with 'tail':

* 'tail :: [a] -> [a]', raises an error on 'tail []'.

* 'tailMay :: [a] -> /Maybe/ [a]', turns errors into 'Nothing'.

* 'tailDef :: /[a]/ -> [a] -> [a]', takes a default to return on errors.

* 'tailNote :: /String/ -> [a] -> [a]', takes an extra argument which
supplements the error message.

* 'tailSafe :: [a] -> [a]', returns some sensible default if possible, '[]' in
the case of 'tail'.

This package is divided into three modules:

* "Safe" contains safe variants of 'Prelude' and 'Data.List' functions.

* "Safe.Foldable" contains safe variants of 'Foldable' functions.

* "Safe.Exact" creates crashing versions of functions like 'zip' (errors if the
lists are not equal) and 'take' (errors if there are not enough elements), then
wraps them to provide safe variants.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-safe-devel -f %{oreon_filedir}/ghc-safe-devel.list
%files -n ghc-safe-doc -f %{oreon_filedir}/ghc-safe-doc.list
%files -n ghc-safe-prof -f %{oreon_filedir}/ghc-safe-prof.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.21-1
- Prepare for Oreon 11 (RP1)
