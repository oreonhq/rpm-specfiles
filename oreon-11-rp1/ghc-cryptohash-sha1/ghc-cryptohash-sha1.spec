%global source1_hash 2bdf29dbd896bca86bf198c882fa8df1cb31843b71f2907e059b7c10bce0adb3
%global source0_hash a4042c97ad02eb68e766577ca35c01970c33e96cfd74ccb4dd403e3476a23241
%global pkg_name cryptohash-sha1
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        0.11.101.0
Release:        1%{?dist}
Summary:        Fast, pure and practical SHA-1 implementation
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/cryptohash-sha1
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-SHA-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-base16-bytestring-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-tasty-quickcheck-devel
# /oreon:deps
%description
A practical incremental and one-pass, pure API to the SHA-1 hash algorithm
(including HMAC support) with performance close to the fastest implementations
available in other languages.

NOTE: This package has been forked off 'cryptohash-0.11.7' because the
'cryptohash' package has been deprecated and so this package continues to
satisfy the need for a lightweight package providing the SHA1 hash algorithm
without any dependencies on packages other than 'base' and 'bytestring'.

Consequently, this package can be used as a drop-in replacement for
cryptohash's "Crypto.Hash.SHA1" module, though with a clearly smaller
footprint.

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

%check

%if %{with tests}
%cabal_test
%endif
%files -f %{oreon_filedir}/main.list
%files -n ghc-cryptohash-sha1-devel -f %{oreon_filedir}/ghc-cryptohash-sha1-devel.list
%files -n ghc-cryptohash-sha1-doc -f %{oreon_filedir}/ghc-cryptohash-sha1-doc.list
%files -n ghc-cryptohash-sha1-prof -f %{oreon_filedir}/ghc-cryptohash-sha1-prof.list

%changelog

%autochangelog
