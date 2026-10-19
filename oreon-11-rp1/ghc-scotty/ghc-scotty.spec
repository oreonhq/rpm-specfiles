%global source1_hash bcd3436af3ac3959ec1d0b2c4a9ce189b129beebf190aa8c808a69b0f275f228
%global source0_hash df90a8842400708e1314caaf0a7f0a026e214f3d5f98b7722edecc2e14fa4c4b
%global pkg_name scotty
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.30
Release:        1%{?dist}
Summary:        Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/scotty
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-cookie-devel
BuildRequires:  ghc-cookie-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-monad-control-devel
BuildRequires:  ghc-monad-control-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-regex-compat-devel
BuildRequires:  ghc-regex-compat-prof
BuildRequires:  ghc-resourcet-devel
BuildRequires:  ghc-resourcet-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-stm-devel
BuildRequires:  ghc-stm-prof
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-base-devel
BuildRequires:  ghc-transformers-base-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unliftio-devel
BuildRequires:  ghc-unliftio-prof
BuildRequires:  ghc-wai-devel
BuildRequires:  ghc-wai-extra-devel
BuildRequires:  ghc-wai-extra-prof
BuildRequires:  ghc-wai-prof
BuildRequires:  ghc-warp-devel
BuildRequires:  ghc-warp-prof
# /oreon:deps
%description
A Haskell web framework inspired by Ruby's Sinatra, using WAI and Warp.

Scotty is the cheap and cheerful way to write RESTful, declarative web
applications.

* A page is as simple as defining the verb, url pattern, and Text content.
* It is template-language agnostic. Anything that returns a Text value will do.
* Conforms to WAI Application interface.
* Uses very fast Warp webserver by default.

As for the name: Sinatra + Warp = Scotty.

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
%files -n ghc-scotty-devel -f %{oreon_filedir}/ghc-scotty-devel.list
%files -n ghc-scotty-doc -f %{oreon_filedir}/ghc-scotty-doc.list
%files -n ghc-scotty-prof -f %{oreon_filedir}/ghc-scotty-prof.list

%changelog

%autochangelog
