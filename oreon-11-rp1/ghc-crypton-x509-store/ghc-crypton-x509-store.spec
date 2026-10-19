%global source0_hash de9193403c11d1fb090083382646be6f6cf68ed984f475d1a0e142f77efb8766
%global pkg_name crypton-x509-store
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
%bcond tests 1
Name:           ghc-%{pkg_name}
Version:        1.9.0
Release:        1%{?dist}
Summary:        X.509 collection accessing and storing methods
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/crypton-x509-store
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
%if %{with tests}
%endif
Obsoletes:      ghc-x509-store < %{version}-%{release}
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-asn1-encoding-devel
BuildRequires:  ghc-asn1-encoding-prof
BuildRequires:  ghc-asn1-types-devel
BuildRequires:  ghc-asn1-types-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-devel
BuildRequires:  ghc-crypton-prof
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pem-devel
BuildRequires:  ghc-pem-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-tasty-devel
BuildRequires:  ghc-tasty-hunit-devel
BuildRequires:  ghc-unix-devel
BuildRequires:  ghc-unix-prof
# /oreon:deps
%description
X.509 collection accessing and storing methods for certificate, crl, exception
list.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      ghc-x509-store-devel < %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
Obsoletes:      ghc-x509-store-doc < %{version}-%{release}
%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
Obsoletes:      ghc-x509-store-prof < %{version}-%{release}
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
%files -n ghc-crypton-x509-store-devel -f %{oreon_filedir}/ghc-crypton-x509-store-devel.list
%files -n ghc-crypton-x509-store-doc -f %{oreon_filedir}/ghc-crypton-x509-store-doc.list
%files -n ghc-crypton-x509-store-prof -f %{oreon_filedir}/ghc-crypton-x509-store-prof.list

%changelog

%autochangelog
