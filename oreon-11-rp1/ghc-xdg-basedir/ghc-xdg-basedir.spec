%global source0_hash e461c3a5c6007c55ceaea03be3be0ef3a92aa0ea1aea936da0c43671bbfaf42b
%global pkg_name xdg-basedir
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        Haskell implementation of XDG base directory spec
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/xdg-basedir
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-directory-devel
BuildRequires:  ghc-directory-prof
BuildRequires:  ghc-filepath-devel
BuildRequires:  ghc-filepath-prof
BuildRequires:  ghc-rpm-macros
# /oreon:deps
%description
A basic implementation of the XDG Base Directory specification.
On Unix platforms, this should be a very straightforward implementation
of the XDG Base Directory spec. On Windows, it will attempt to do the
right thing with regards to choosing appropriate directories.

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

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-xdg-basedir-devel -f %{oreon_filedir}/ghc-xdg-basedir-devel.list
%files -n ghc-xdg-basedir-doc -f %{oreon_filedir}/ghc-xdg-basedir-doc.list
%files -n ghc-xdg-basedir-prof -f %{oreon_filedir}/ghc-xdg-basedir-prof.list

%changelog

%autochangelog
