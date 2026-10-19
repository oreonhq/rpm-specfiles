%global source2_hash a113c6dda580ab274ef1a7db2829b8804899f6b24ede622550e069e84ed2968c
%global source1_hash 6c65f29c7470e60b30a4dd4bdb4ed3506343cad05efca34985f2223e46bf83c4
%global source0_hash d3d42f8db94936847c53942ae0ed66f49a343095d761736dbaf9104690723e7a
%global pkg_name persistent
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%global lifttype lift-type-0.1.2.0
%global replacemegaparsec replace-megaparsec-1.5.0.1
%global subpkgs %{lifttype} %{replacemegaparsec}
Name:           ghc-%{pkg_name}
Version:        2.18.1.0
Release:        1%{?dist}
Summary:        Type-safe, multi-backend data serialization
License:        MIT
URL:            https://hackage.haskell.org/package/persistent
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{lifttype}/%{lifttype}.tar.gz
Source2:        https://hackage.haskell.org/package/%{replacemegaparsec}/%{replacemegaparsec}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-html-devel
BuildRequires:  ghc-blaze-html-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-conduit-devel
BuildRequires:  ghc-conduit-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-fast-logger-devel
BuildRequires:  ghc-fast-logger-prof
BuildRequires:  ghc-http-api-data-devel
BuildRequires:  ghc-http-api-data-prof
BuildRequires:  ghc-megaparsec-devel
BuildRequires:  ghc-megaparsec-prof
BuildRequires:  ghc-monad-logger-devel
BuildRequires:  ghc-monad-logger-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-parser-combinators-devel
BuildRequires:  ghc-parser-combinators-prof
BuildRequires:  ghc-path-pieces-devel
BuildRequires:  ghc-path-pieces-prof
BuildRequires:  ghc-resource-pool-devel
BuildRequires:  ghc-resource-pool-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros-extra
BuildRequires:  ghc-scientific-devel
BuildRequires:  ghc-scientific-prof
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-semigroupoids-prof
BuildRequires:  ghc-silently-devel
BuildRequires:  ghc-silently-prof
BuildRequires:  ghc-template-haskell-devel
BuildRequires:  ghc-template-haskell-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-th-lift-instances-devel
BuildRequires:  ghc-th-lift-instances-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-core-devel
BuildRequires:  ghc-unliftio-core-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
BuildRequires:  ghc-vault-devel
BuildRequires:  ghc-vault-prof
BuildRequires:  ghc-vector-devel
BuildRequires:  ghc-vector-prof
# /oreon:deps
%description
Persistent allows us to choose among existing databases that are highly tuned
for different data storage use cases, interoperate with other programming
languages, and to use a safe and productive query interface, while still
keeping the type safety of Haskell datatypes.

Persistent follows the guiding principles of type safety and concise,
declarative syntax. Other nice features are database-independence, convenient
data modeling, and automatic database migrations.

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

%global main_version %{version}

%if %{defined ghclibdir}
%ghc_lib_subpackage -l BSD-3-Clause %{lifttype}
%ghc_lib_subpackage -l BSD-2-Clause %{replacemegaparsec}
%endif

%global version %{main_version}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver} -a1 -a2
# End cabal-rpm setup

%build

%ghc_libs_build %{subpkgs}
%ghc_lib_build
%install
%ghc_libs_install %{subpkgs}
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-persistent-devel -f %{oreon_filedir}/ghc-persistent-devel.list
%files -n ghc-persistent-doc -f %{oreon_filedir}/ghc-persistent-doc.list
%files -n ghc-persistent-prof -f %{oreon_filedir}/ghc-persistent-prof.list

%changelog

%autochangelog
