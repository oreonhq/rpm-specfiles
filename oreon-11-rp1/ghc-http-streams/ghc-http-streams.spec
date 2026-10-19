%global source0_hash 1bf34ab439eb5d2bdf540e8d77ced5ea8baa2ee2ca6048e7ba651db8405e6afb
%global pkg_name http-streams
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%ifnarch i686 armv7hl s390x
%bcond tests 1
%endif
Name:           ghc-%{pkg_name}
Version:        0.8.9.9
Release:        1%{?dist}
Summary:        An HTTP client using io-streams
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/http-streams
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Patch0:         http-streams-update-certs-ca-bundle.patch
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-HUnit-devel
BuildRequires:  ghc-HsOpenSSL-devel
BuildRequires:  ghc-HsOpenSSL-prof
BuildRequires:  ghc-aeson-devel
BuildRequires:  ghc-aeson-pretty-devel
BuildRequires:  ghc-aeson-prof
BuildRequires:  ghc-attoparsec-aeson-devel
BuildRequires:  ghc-attoparsec-aeson-prof
BuildRequires:  ghc-attoparsec-devel
BuildRequires:  ghc-attoparsec-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base64-bytestring-devel
BuildRequires:  ghc-base64-bytestring-prof
BuildRequires:  ghc-blaze-builder-devel
BuildRequires:  ghc-blaze-builder-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-case-insensitive-devel
BuildRequires:  ghc-case-insensitive-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-hspec-devel
BuildRequires:  ghc-hspec-expectations-devel
BuildRequires:  ghc-http-common-devel
BuildRequires:  ghc-http-common-prof
BuildRequires:  ghc-io-streams-devel
BuildRequires:  ghc-io-streams-prof
BuildRequires:  ghc-lifted-base-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-network-devel
BuildRequires:  ghc-network-prof
BuildRequires:  ghc-network-uri-devel
BuildRequires:  ghc-network-uri-prof
BuildRequires:  ghc-openssl-streams-devel
BuildRequires:  ghc-openssl-streams-prof
BuildRequires:  ghc-random-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-snap-core-devel
BuildRequires:  ghc-snap-server-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-unordered-containers-prof
# /oreon:deps
%description
An HTTP client, using the Snap Framework's 'io-streams' library to handle the
streaming IO. The API is optimized for ease of use for the rather common case
of code needing to query web services and deal with the result.

The library is exported in a single module; see "Network.Http.Client" for full
documentation.

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
%patch -P0 -p1 -b .orig

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
%files -n ghc-http-streams-devel -f %{oreon_filedir}/ghc-http-streams-devel.list
%files -n ghc-http-streams-doc -f %{oreon_filedir}/ghc-http-streams-doc.list
%files -n ghc-http-streams-prof -f %{oreon_filedir}/ghc-http-streams-prof.list

%changelog

%autochangelog
