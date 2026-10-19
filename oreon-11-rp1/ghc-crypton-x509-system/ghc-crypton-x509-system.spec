%global source0_hash 89ee819b78963a5c925fdaad80e2e64be6c0fedf4f24fc2b95eddb649b86cefe
%global pkg_name crypton-x509-system
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.9.0
Release:        1%{?dist}
Summary:        Handle per-operating-system X.509 accessors and storage
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/crypton-x509-system
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
Obsoletes:      ghc-x509-system < %{version}-%{release}
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-crypton-x509-devel
BuildRequires:  ghc-crypton-x509-prof
BuildRequires:  ghc-crypton-x509-store-devel
BuildRequires:  ghc-crypton-x509-store-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pem-devel
BuildRequires:  ghc-pem-prof
BuildRequires:  ghc-process-devel
BuildRequires:  ghc-process-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
System X.509 handling for accessing operating system dependents store and other
storage methods.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Obsoletes:      ghc-x509-system-devel < %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem
Obsoletes:      ghc-x509-system-doc < %{version}-%{release}
%description doc
This package provides the Haskell %{pkg_name} library
documentation.
%endif

%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)
Obsoletes:      ghc-x509-system-prof < %{version}-%{release}
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
%files -n ghc-crypton-x509-system-devel -f %{oreon_filedir}/ghc-crypton-x509-system-devel.list
%files -n ghc-crypton-x509-system-doc -f %{oreon_filedir}/ghc-crypton-x509-system-doc.list
%files -n ghc-crypton-x509-system-prof -f %{oreon_filedir}/ghc-crypton-x509-system-prof.list

%changelog

%autochangelog
