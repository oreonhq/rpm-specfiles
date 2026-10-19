%global source0_hash 3ed797f8dd8d3535640b1ca99851bbc5968817c25a80fc499af42715d371682a
%global pkg_name haskell-gi-overloading
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.0
Release:        1%{?dist}
Epoch:          1
Summary:        Overloading support for haskell-gi
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/haskell-gi-overloading
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
Control overloading support in haskell-gi generated bindings.

%package devel
Summary:        Haskell %{pkg_name} library development files
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
%description devel
This package provides the Haskell %{pkg_name} library
development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup

%build

%ghc_lib_build_without_haddock
%install
%ghc_lib_install -m
mv %{buildroot}%{_ghcdocdir}{,-devel}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-haskell-gi-overloading-devel -f %{oreon_filedir}/ghc-haskell-gi-overloading-devel.list

%changelog

%autochangelog
