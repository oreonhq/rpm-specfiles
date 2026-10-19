%global source1_hash e932b260dc50dd2a81c996f370798b19979acfd5cfa7bb6b685358e6846600bb
%global source0_hash 491f3e8e9408f5d10ff8d02bf4d0edb11821e2537e7c22edbd6d64bf91388222
%global pkg_name conduit-extra
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.3.8
Release:        1%{?dist}
Summary:        Batteries included conduit: adapters for common libraries
License:        MIT
URL:            https://hackage.haskell.org/package/conduit-extra
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
Obsoletes:      ghc-attoparsec-conduit < 1.2
Obsoletes:      ghc-blaze-builder-conduit < 1.2
Obsoletes:      ghc-network-conduit < 1.2
Obsoletes:      ghc-zlib-conduit < 1.2
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-async-devel
BuildRequires:  ghc-async-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-discover-devel
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-primitive-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-streaming-commons-devel
BuildRequires:  ghc-streaming-commons-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-typed-process-devel
BuildRequires:  ghc-typed-process-prof
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-core-prof
# /oreon:deps
%description
The conduit package itself maintains relative small dependencies. The purpose
of this package is to collect commonly used utility functions wrapping other
library dependencies, without depending on heavier-weight dependencies.
The basic idea is that this package should only depend on haskell-platform
packages and conduit.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      ghc-attoparsec-conduit-devel < 1.2
Obsoletes:      ghc-blaze-builder-conduit-devel < 1.2
Obsoletes:      ghc-network-conduit-devel < 1.2
Obsoletes:      ghc-zlib-conduit-devel < 1.2
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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-conduit-extra-devel -f %{oreon_filedir}/ghc-conduit-extra-devel.list
%files -n ghc-conduit-extra-doc -f %{oreon_filedir}/ghc-conduit-extra-doc.list
%files -n ghc-conduit-extra-prof -f %{oreon_filedir}/ghc-conduit-extra-prof.list

%changelog

%autochangelog
