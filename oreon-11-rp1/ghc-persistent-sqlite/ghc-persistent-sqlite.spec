%global source0_hash a0b95e10fc8f441f65390693c4f89a22616e4b218276a3f559014b6c8b1ad693
%global pkg_name persistent-sqlite
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.13.3.1
Release:        1%{?dist}
Summary:        Backend for the persistent library using sqlite3
License:        MIT
URL:            https://hackage.haskell.org/package/persistent-sqlite
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-microlens-th-devel
BuildRequires:  ghc-microlens-th-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-persistent-devel
BuildRequires:  ghc-persistent-prof
BuildRequires:  ghc-resource-pool-devel
BuildRequires:  ghc-resource-pool-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-core-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  pkgconfig(sqlite3)
# /oreon:deps
%description
This package includes a thin sqlite3 wrapper based on the direct-sqlite
package.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(sqlite3)
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
cabal-tweak-flag systemlib True
cabal-tweak-flag use-pkgconfig True

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-persistent-sqlite-devel -f %{oreon_filedir}/ghc-persistent-sqlite-devel.list
%files -n ghc-persistent-sqlite-doc -f %{oreon_filedir}/ghc-persistent-sqlite-doc.list
%files -n ghc-persistent-sqlite-prof -f %{oreon_filedir}/ghc-persistent-sqlite-prof.list

%changelog

%autochangelog
