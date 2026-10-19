%global source0_hash 6623446cd42aa1f58a9e21f4abc18cfff13b8991d6ac852d9352d0ffea125010
%global pkg_name monad-logger
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.3.42
Release:        1%{?dist}
Summary:        Class of monads which can log messages
License:        MIT
URL:            https://hackage.haskell.org/package/monad-logger
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-extra-devel
BuildRequires:  ghc-conduit-extra-prof
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-lifted-base-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-monad-loops-devel
BuildRequires:  ghc-monad-loops-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-chans-devel
BuildRequires:  ghc-stm-chans-prof
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-core-prof
# /oreon:deps
%description
See README and Haddocks at <https://www.stackage.org/package/monad-logger>.

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
%files -n ghc-monad-logger-devel -f %{oreon_filedir}/ghc-monad-logger-devel.list
%files -n ghc-monad-logger-doc -f %{oreon_filedir}/ghc-monad-logger-doc.list
%files -n ghc-monad-logger-prof -f %{oreon_filedir}/ghc-monad-logger-prof.list

%changelog

%autochangelog
