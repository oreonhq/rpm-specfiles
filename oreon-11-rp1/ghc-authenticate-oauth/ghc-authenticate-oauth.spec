%global source1_hash af2b03698756b2bbb42b8d30236b4d012e31db2b7ce63753158f63d5b0a81da5
%global source0_hash 746ff695fec1bd7c7b90f1952847ce3453fadf0f18a31db206753360b3219b78
%global pkg_name authenticate-oauth
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.7
Release:        1%{?dist}
Summary:        Library to authenticate with OAuth for Haskell web applications
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/authenticate-oauth
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-RSA-devel
BuildRequires:  ghc-RSA-prof
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-SHA-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-crypto-pubkey-types-devel
BuildRequires:  ghc-crypto-pubkey-types-prof
BuildRequires:  ghc-data-default-devel
BuildRequires:  ghc-data-default-prof
BuildRequires:  ghc-http-client-devel
BuildRequires:  ghc-http-client-prof
BuildRequires:  ghc-http-types-devel
BuildRequires:  ghc-http-types-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-random-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-time-devel
BuildRequires:  ghc-time-prof
BuildRequires:  ghc-transformers-compat-devel
BuildRequires:  ghc-transformers-compat-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
Authentication methods for Haskell web applications.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
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
cp -bp %{SOURCE1} %{pkg_name}.cabal
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-authenticate-oauth-devel -f %{oreon_filedir}/ghc-authenticate-oauth-devel.list
%files -n ghc-authenticate-oauth-doc -f %{oreon_filedir}/ghc-authenticate-oauth-doc.list
%files -n ghc-authenticate-oauth-prof -f %{oreon_filedir}/ghc-authenticate-oauth-prof.list

%changelog

%autochangelog
