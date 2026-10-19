%global source0_hash dc488b567d373ebfbf5f3df8bba240e6203d1b13556872648d5f0d228fd02c31
%global pkg_name persistent-template
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        2.12.0.0
Release:        1%{?dist}
Summary:        Type-safe, non-relational, multi-backend persistence
License:        MIT
URL:            https://hackage.haskell.org/package/persistent-template
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
The library has been merged into the persistent package.

%package devel
Summary:        Haskell %{pkg_name} library development files
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Obsoletes:      ghc-persistent-template < %{version}-%{release}
Obsoletes:      ghc-persistent-template-prof < %{version}-%{release}
%description devel
This package provides the Haskell %{pkg_name} library development
files.

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
%files -n ghc-persistent-template-devel -f %{oreon_filedir}/ghc-persistent-template-devel.list

%changelog

%autochangelog
