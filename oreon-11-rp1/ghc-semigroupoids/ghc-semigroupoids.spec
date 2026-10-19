%global source1_hash 52c5a346fdf74380618f67ff784989ef9078498dbbdff09e4d8e2fed20202e2c
%global source0_hash e48258e49542245ef6c58d7f419a83d1d1ab91b013d92c3b5c8c7c048daaa12e
%global pkg_name semigroupoids
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        6.0.2
Release:        1%{?dist}
Summary:        Semigroupoids: Category sans id
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/semigroupoids
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-orphans-devel
BuildRequires:  ghc-base-orphans-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-comonad-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-contravariant-prof
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-hashable-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
# /oreon:deps
%description
Provides a wide array of (semi)groupoids and operations for working with them.

A 'Semigroupoid' is a 'Category' without the requirement of identity arrows for
every object in the category.

A 'Category' is any 'Semigroupoid' for which the Yoneda lemma holds.

When working with comonads you often have the '<*>' portion of an
'Applicative', but not the 'pure'. This was captured in Uustalu and Vene's
"Essence of Dataflow Programming" in the form of the 'ComonadZip' class in the
days before 'Applicative'. Apply provides a weaker invariant, but for the
comonads used for data flow programming (found in the streams package), this
invariant is preserved. Applicative function composition forms a semigroupoid.

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
%files -n ghc-semigroupoids-devel -f %{oreon_filedir}/ghc-semigroupoids-devel.list
%files -n ghc-semigroupoids-doc -f %{oreon_filedir}/ghc-semigroupoids-doc.list
%files -n ghc-semigroupoids-prof -f %{oreon_filedir}/ghc-semigroupoids-prof.list

%changelog

%autochangelog
