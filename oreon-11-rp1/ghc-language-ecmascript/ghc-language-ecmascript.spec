%global source0_hash 5a08ec4323f9e4818983de3805624aa80e2009e788c348febc7b9a4cd3fc654e
%global pkg_name language-ecmascript
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.19.1.0
Release:        8%{?dist}
Summary:        JavaScript parser and pretty-printer library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/language-ecmascript
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         language-ecmascript-ghc9.6.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-Diff-devel
BuildRequires:  ghc-Diff-prof
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-ansi-wl-pprint-devel
BuildRequires:  ghc-ansi-wl-pprint-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-charset-devel
BuildRequires:  ghc-charset-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-uniplate-devel
BuildRequires:  ghc-uniplate-prof
# /oreon:deps
%description
Tools for working with ECMAScript 3 (popularly known as JavaScript).
Includes a parser, pretty-printer, tools for working with source tree
annotations and an arbitrary instance.

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
This package provides the Haskell %{pkg_name} library
documentation.
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
%autopatch -p1
# End cabal-rpm setup
cabal-tweak-dep-ver ansi-wl-pprint '< 1' '< 2'
cabal-tweak-dep-ver base '< 4.19' '< 4.21'
cabal-tweak-dep-ver data-default-class '< 0.2' '< 0.3'
cabal-tweak-dep-ver Diff '== 0.4.*' '== 1.0.*'

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-language-ecmascript-devel -f %{oreon_filedir}/ghc-language-ecmascript-devel.list
%files -n ghc-language-ecmascript-doc -f %{oreon_filedir}/ghc-language-ecmascript-doc.list
%files -n ghc-language-ecmascript-prof -f %{oreon_filedir}/ghc-language-ecmascript-prof.list

%changelog

%autochangelog
