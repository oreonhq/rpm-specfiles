%global source1_hash 98d6c78c8811b84e6c518cf3c87ad754eaae272aabea82ca057ec4f7dee329a3
%global source0_hash ba009b2af9827399d4a48720cd3a803da3b5d3f33a7145fa5b81b9db6d914d8d
%global pkg_name HsYAML
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.2.1.6
Release:        1%{?dist}
Summary:        Pure Haskell YAML 1.2 processor
License:        GPL-2.0-or-later
URL:            https://hackage.haskell.org/package/HsYAML
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-quickcheck-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
'HsYAML' is a [YAML 1.2](http://yaml.org/spec/1.2/spec.html) processor, i.e.
a library for parsing and serializing YAML documents.

Features of 'HsYAML' include:

* Pure Haskell implementation with small dependency footprint and emphasis on
strict compliance with the <http://yaml.org/spec/1.2/spec.html>.
* Direct decoding to native Haskell types via ('aeson'-inspired) typeclass-based
API (see "Data.YAML").
* Allows round-tripping while preserving ordering, anchors, and comments at
Event-level.
* Support for constructing custom YAML node graph representation (including
support for cyclic YAML data structures).
* Support for the standard (untyped) /Failsafe/, (strict) /JSON/, and
(flexible) /Core/ "schemas" providing implicit typing rules as defined in
the YAML 1.2 specification (including support for user-defined custom schemas).
* Support for emitting YAML using /Failsafe/, (strict) /JSON/, and (flexible)
/Core/ "schemas" (including support for user-defined custom encoding schemas
* Event-based API resembling LibYAML's Event-based API (see "Data.YAML.Event").
* Low-level API access to lexical token-based scanner (see "Data.YAML.Token").

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-HsYAML-devel -f %{oreon_filedir}/ghc-HsYAML-devel.list
%files -n ghc-HsYAML-doc -f %{oreon_filedir}/ghc-HsYAML-doc.list
%files -n ghc-HsYAML-prof -f %{oreon_filedir}/ghc-HsYAML-prof.list

%changelog

%autochangelog
