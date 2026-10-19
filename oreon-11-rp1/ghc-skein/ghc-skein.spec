%global source0_hash f882ca0cc5ed336ef898fb3c89579e392900259296b2320edf968b9fc16cb8c9
%global pkg_name skein
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.0.9.4
Release:        1%{?dist}
Summary:        Skein, a family of cryptographic hash functions.  Includes Skein-MAC as well
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/skein
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-cereal-devel
BuildRequires:  ghc-cereal-prof
BuildRequires:  ghc-crypto-api-devel
BuildRequires:  ghc-crypto-api-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tagged-devel
BuildRequires:  ghc-tagged-prof
# /oreon:deps
%description
Skein (<http://www.skein-hash.info/>) is a family of fast secure cryptographic
hash functions designed by Niels Ferguson, Stefan Lucks, Bruce Schneier, Doug
Whiting, Mihir Bellare, Tadayoshi Kohno, Jon Callas and Jesse Walker.

This package uses bindings to the optimized C implementation of Skein.
We provide a high-level interface (see module "Crypto.Skein") to some of the
Skein use cases. We also provide a low-level interface (see module
"Crypto.Skein.Internal") should you need to use Skein in a different way.

Currently we have support for Skein as cryptographic hash function as Skein as
a message authentication code (Skein-MAC). For examples of how to use this
package, see "Crypto.Skein" module documentation.

This package includes Skein v1.3. Versions of this package before 1.0.0
implemented Skein v1.1.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-skein-devel -f %{oreon_filedir}/ghc-skein-devel.list
%files -n ghc-skein-doc -f %{oreon_filedir}/ghc-skein-doc.list
%files -n ghc-skein-prof -f %{oreon_filedir}/ghc-skein-prof.list

%changelog

%autochangelog
