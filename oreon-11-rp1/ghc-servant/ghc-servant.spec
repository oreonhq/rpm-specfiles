%global source1_hash 4fe47ef2b2939c018cb0f87f3cd8ede0ae5365a275ad33e3deca109319d42a6f
%global source0_hash f273e65c8f6cc6ddfa204c8d1d0bc5b7e258cec288ca5b2a2e57fadb31bf6602
%global pkg_name servant
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.20.3.0
Release:        1%{?dist}
Summary:        A family of combinators for defining webservices APIs
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/servant
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-QuickCheck-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bifunctors-devel
BuildRequires:  ghc-bifunctors-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-constraints-devel
BuildRequires:  ghc-constraints-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-generics-sop-devel
BuildRequires:  ghc-generics-sop-prof
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-api-data-prof
BuildRequires:  ghc-http-media-devel
BuildRequires:  ghc-http-media-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-mmorph-devel
BuildRequires:  ghc-mmorph-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-singleton-bool-devel
BuildRequires:  ghc-singleton-bool-prof
BuildRequires:  ghc-sop-core-devel
BuildRequires:  ghc-sop-core-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vault-prof
# /oreon:deps
%description
A family of combinators for defining webservices APIs and serving them

You can learn about the basics in the
<http://docs.servant.dev/en/stable/tutorial/index.html tutorial>.

<https://github.com/haskell-servant/servant/blob/master/servant/CHANGELOG.md
CHANGELOG>.

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
cabal-tweak-remove-upperbound QuickCheck

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-servant-devel -f %{oreon_filedir}/ghc-servant-devel.list
%files -n ghc-servant-doc -f %{oreon_filedir}/ghc-servant-doc.list
%files -n ghc-servant-prof -f %{oreon_filedir}/ghc-servant-prof.list

%changelog

%autochangelog
