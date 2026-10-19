%global source0_hash fbeb0854c8e8072e2ad10aed5582f7772cf039ebfa4315269a00528a69691c1d
%global pkg_name what4
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.8
Release:        1%{?dist}
Summary:        Solver-agnostic symbolic values support for issuing queries
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/what4
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-BoundedChan-devel
BuildRequires:  ghc-BoundedChan-prof
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-bimap-devel
BuildRequires:  ghc-bimap-prof
BuildRequires:  ghc-bv-sized-devel
BuildRequires:  ghc-bv-sized-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-concurrent-extra-devel
BuildRequires:  ghc-concurrent-extra-prof
BuildRequires:  ghc-config-value-devel
BuildRequires:  ghc-config-value-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-deriving-compat-devel
BuildRequires:  ghc-deriving-compat-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-fingertree-devel
BuildRequires:  ghc-fingertree-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-hashtables-devel
BuildRequires:  ghc-hashtables-prof
BuildRequires:  ghc-io-streams-devel
BuildRequires:  ghc-io-streams-prof
BuildRequires:  ghc-lens-devel
BuildRequires:  ghc-lens-prof
BuildRequires:  ghc-libBF-devel
BuildRequires:  ghc-libBF-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-ordered-containers-devel
BuildRequires:  ghc-ordered-containers-prof
BuildRequires:  ghc-panic-devel
BuildRequires:  ghc-panic-prof
BuildRequires:  ghc-parameterized-utils-devel
BuildRequires:  ghc-parameterized-utils-prof
BuildRequires:  ghc-parsec-devel
BuildRequires:  ghc-parsec-prof
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-s-cargot-devel
BuildRequires:  ghc-s-cargot-prof
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-temporary-devel
BuildRequires:  ghc-temporary-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-devel
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-th-lift-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-utf8-string-devel
BuildRequires:  ghc-utf8-string-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
BuildRequires:  ghc-versions-devel
BuildRequires:  ghc-versions-prof
BuildRequires:  ghc-zenc-devel
BuildRequires:  ghc-zenc-prof
# /oreon:deps
%description
What4 is a generic library for representing values as symbolic formulae which
may contain references to symbolic values, representing unknown variables.
It provides support for communicating with a variety of SAT and SMT solvers,
including Z3, CVC4, CVC5, Yices, Bitwuzla, Boolector, STP, and dReal.
The data representation types make heavy use of GADT-style type indices to
ensure type-correct manipulation of symbolic values.

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
%files -n ghc-what4-devel -f %{oreon_filedir}/ghc-what4-devel.list
%files -n ghc-what4-doc -f %{oreon_filedir}/ghc-what4-doc.list
%files -n ghc-what4-prof -f %{oreon_filedir}/ghc-what4-prof.list

%changelog

%autochangelog
