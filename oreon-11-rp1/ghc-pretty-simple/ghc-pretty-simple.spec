%global source0_hash 3a51aa5c987bba79c2bc75b14b28b2bcba7862f18162431811476512be2dae1f
%global pkg_name pretty-simple
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch s390x
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        4.1.4.0
Release:        1%{?dist}
Summary:        Pretty printer for data types with a 'Show' instance
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/pretty-simple
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-optparse-applicative-devel
BuildRequires:  ghc-optparse-applicative-prof
BuildRequires:  ghc-prettyprinter-ansi-terminal-devel
BuildRequires:  ghc-prettyprinter-ansi-terminal-prof
BuildRequires:  ghc-prettyprinter-devel
BuildRequires:  ghc-prettyprinter-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Please see <https://github.com/cdepillabout/pretty-simple#readme README.md>.

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
%ifarch ppc64le
sed -i -e "s/ -rtsopts -with-rtsopts=-N//" %{pkg_name}.cabal
%endif

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-pretty-simple-devel -f %{oreon_filedir}/ghc-pretty-simple-devel.list
%files -n ghc-pretty-simple-doc -f %{oreon_filedir}/ghc-pretty-simple-doc.list
%files -n ghc-pretty-simple-prof -f %{oreon_filedir}/ghc-pretty-simple-prof.list

%changelog

%autochangelog
