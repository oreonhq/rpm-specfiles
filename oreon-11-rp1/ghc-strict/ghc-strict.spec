%global source1_hash 58c373b7c7748cbb4a5a6c8c15073f99a1c10a9a9bb6894ac33f43a5cdb901f2
%global source0_hash 77719280c2a86312e748227bfa732eeaae0e7df48d57acc3c2e5b7b07afe2f8b
%global pkg_name strict
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Strict data types and String IO
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/strict
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-assoc-devel
BuildRequires:  ghc-assoc-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-binary-devel
BuildRequires:  ghc-binary-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-these-devel
BuildRequires:  ghc-these-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
This package provides strict versions of some standard Haskell data types
(pairs, Maybe and Either). It also contains strict IO operations.

It is common knowledge that lazy datastructures can lead to space-leaks.
This problem is particularly prominent, when using lazy datastructures to store
the state of a long-running application in memory. One common solution to this
problem is to use 'seq' and its variants in every piece of code that updates
your state. However a much easier solution is to use fully strict types to
store such state values. By "fully strict types" we mean types for whose values
it holds that, if they are in weak-head normal form, then they are also in
normal form. Intuitively, this means that values of fully strict types cannot
contain unevaluated thunks.

To define a fully strict datatype, one typically uses the following recipe.

1. Make all fields of every constructor strict; i.e., add a bang to all fields.

2. Use only strict types for the fields of the constructors.

The second requirement is problematic as it rules out the use of the standard
Haskell 'Maybe', 'Either', and pair types. This library solves this problem by
providing strict variants of these types and their corresponding standard
support functions and type-class instances.

Note that this library does currently not provide fully strict lists.
They can be added if they are really required. However, in many cases one
probably wants to use unboxed or strict boxed vectors from the 'vector' library
(<http://hackage.haskell.org/package/vector>) instead of strict lists.
Moreover, instead of 'String's one probably wants to use strict 'Text' values
from the 'text' library (<http://hackage.haskell.org/package/text>).

This library comes with batteries included; i.e., mirror functions and
instances of the lazy versions in 'base'. It also includes instances for
type-classes from the 'deepseq', 'binary', and 'hashable' packages.

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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-strict-devel -f %{oreon_filedir}/ghc-strict-devel.list
%files -n ghc-strict-doc -f %{oreon_filedir}/ghc-strict-doc.list
%files -n ghc-strict-prof -f %{oreon_filedir}/ghc-strict-prof.list

%changelog

%autochangelog
