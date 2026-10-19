%global source0_hash 8ffc0fa59e01de47f9802ed1ca486c6d000babb51d7da7cd17c85ef068d7b382
%global pkg_name graphviz
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2999.20.2.1
Release:        1%{?dist}
Summary:        Bindings to Graphviz for graph visualization
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/graphviz
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-colour-devel
BuildRequires:  ghc-colour-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-dlist-devel
BuildRequires:  ghc-dlist-prof
BuildRequires:  ghc-fgl-devel
BuildRequires:  ghc-fgl-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-polyparse-devel
BuildRequires:  ghc-polyparse-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-wl-pprint-text-devel
BuildRequires:  ghc-wl-pprint-text-prof
# /oreon:deps
%description
This library provides bindings for the Dot language used by the Graphviz
(<http://graphviz.org/>) suite of programs for visualizing graphs, as well as
functions to call those programs.

Main features of the graphviz library include:

* Almost complete coverage of all Graphviz attributes and syntax.

* Support for specifying clusters.

* The ability to use a custom node type.

* Functions for running a Graphviz layout tool with all specified output types.

* The ability to not only generate but also parse Dot code with two options:
strict and liberal (in terms of ordering of statements).

* Functions to convert FGL graphs and other graph-like data structures to Dot
code - including support to group them into clusters - with a high degree of
customization by specifying which attributes to use and limited support for the
inverse operation.

* Round-trip support for passing an FGL graph through Graphviz to augment node
and edge labels with positional information, etc.

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
%files -n ghc-graphviz-devel -f %{oreon_filedir}/ghc-graphviz-devel.list
%files -n ghc-graphviz-doc -f %{oreon_filedir}/ghc-graphviz-doc.list
%files -n ghc-graphviz-prof -f %{oreon_filedir}/ghc-graphviz-prof.list

%changelog

%autochangelog
