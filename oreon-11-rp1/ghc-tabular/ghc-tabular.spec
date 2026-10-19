%global source1_hash 39809f48fe715825f05276aa37ed157ba834208dc78336f34bab6da641308bd2
%global source0_hash cb7d06eaec7945cd77db2380ed4a9b7a048c5f6abcfba766c328228be033237d
%global pkg_name tabular
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.2.8
Release:        1%{?dist}
Summary:        Two-dimensional data tables with rendering functions
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/tabular
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-csv-devel
BuildRequires:  ghc-csv-prof
BuildRequires:  ghc-html-devel
BuildRequires:  ghc-html-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Tabular provides a Haskell representation of two-dimensional data tables, the
kind that you might find in a spreadsheet or or a research report. It also
comes with some default rendering functions for turning those tables into ASCII
art, simple text with an arbitrary delimiter, CSV, HTML or LaTeX.

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
%files -n ghc-tabular-devel -f %{oreon_filedir}/ghc-tabular-devel.list
%files -n ghc-tabular-doc -f %{oreon_filedir}/ghc-tabular-doc.list
%files -n ghc-tabular-prof -f %{oreon_filedir}/ghc-tabular-prof.list

%changelog

%autochangelog
