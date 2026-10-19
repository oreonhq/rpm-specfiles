%global source0_hash 5199390c545270fd3e458084714f05e95c76a88d54d92d07fda2c24ef7bdeef9
%global pkg_name deepseq-generics
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.0.1
Release:        1%{?dist}
Summary:        Generics-based normal form reduction for deepseq
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/deepseq-generics
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
This package provides a "GHC.Generics"-based
'Control.DeepSeq.Generics.genericRnf' function which can be used for providing
a 'rnf' implementation. See the documentation for the 'genericRnf' function in
the "Control.DeepSeq.Generics" module to get started.

The original idea was pioneered in the 'generic-deepseq' package (see
<http://www.haskell.org/pipermail/haskell-cafe/2012-February/099551.html> for
more information).

This package differs from the 'generic-deepseq' package by working in
combination with the existing 'deepseq' package as opposed to defining a
conflicting drop-in replacement for 'deepseq's 'Control.Deepseq' module.

Note: The ability to auto-derive via "GHC.Generics" has been merged into
'deepseq-1.4.0.0'. This package is now still useful for writing code that's
also compatible with older 'deepseq' versions not yet providing
"GHC.Generics"-support.

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

%files -f %{oreon_filedir}/main.list
%files -n ghc-deepseq-generics-devel -f %{oreon_filedir}/ghc-deepseq-generics-devel.list
%files -n ghc-deepseq-generics-doc -f %{oreon_filedir}/ghc-deepseq-generics-doc.list
%files -n ghc-deepseq-generics-prof -f %{oreon_filedir}/ghc-deepseq-generics-prof.list

%changelog

%autochangelog
