%global source1_hash 8bb7261bd54bd58acfcb154be6a161fb6d0d31a1852aadc8e927d2ad2d7651d1
%global source0_hash 3c51d8d50c9b60ff8bf94f942fd92e3bea9e62c5afa778dfc9f707b79da41ef6
%global pkg_name safe-exceptions
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.1.7.4
Release:        1%{?dist}
Summary:        Safe, consistent, and easy exception handling
License:        MIT
URL:            https://hackage.haskell.org/package/safe-exceptions
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-deepseq-devel
BuildRequires:  ghc-deepseq-prof
BuildRequires:  ghc-exceptions-devel
BuildRequires:  ghc-exceptions-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-prof
# /oreon:deps
%description
This package provides additional safety and simplicity versus
`Control.Exception` by having its functions recognize the difference between
synchronous and asynchronous exceptions. As described below, synchronous
exceptions are treated as _recoverable_, allowing you to catch and handle them
as well as clean up after them, whereas asynchronous exceptions can only be
cleaned up after. In particular, this library prevents you from making the
following mistakes:

* Catching and swallowing an asynchronous exception
* Throwing an asynchronous exception synchronously
* Throwing a synchronous exception asynchronously
* Swallowing asynchronous exceptions via failing cleanup handlers

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
%files -n ghc-safe-exceptions-devel -f %{oreon_filedir}/ghc-safe-exceptions-devel.list
%files -n ghc-safe-exceptions-doc -f %{oreon_filedir}/ghc-safe-exceptions-doc.list
%files -n ghc-safe-exceptions-prof -f %{oreon_filedir}/ghc-safe-exceptions-prof.list

%changelog

%autochangelog
