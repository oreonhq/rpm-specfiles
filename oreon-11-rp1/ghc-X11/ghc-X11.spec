%global source1_hash 0d1dfe1034a3bbed5cd5657b7d825b07e4a01d6efe75e118e082f5650a46af00
%global source0_hash d84ad1b8f5cdb65a0de17f84d765ebbb7aeeab9608c3740804da28100616d242
%global pkg_name X11
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        1.10.3
Release:        1%{?dist}
Summary:        Haskell binding to the X11 graphics library
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/X11
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
Source1:        https://hackage.haskell.org/package/%{pkgver}/%{pkg_name}.cabal#/%{pkgver}.cabal
Patch0:         X11.buildinfo.patch
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-data-default-class-devel
BuildRequires:  ghc-data-default-class-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  libX11-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  libXext-devel
BuildRequires:  libXinerama-devel
BuildRequires:  libXrandr-devel
# /oreon:deps
%description
A Haskell binding to the X11 graphics library. The binding is a direct
translation of the C binding; for documentation of these calls, refer to "The
Xlib Programming Manual", available online at <http://tronche.com/gui/x/xlib/>.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libX11-devel%{?_isa}
Requires:       libXext-devel%{?_isa}
Requires:       libXrandr-devel%{?_isa}
Requires:       libXinerama-devel%{?_isa}
Requires:       libXScrnSaver-devel%{?_isa}
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
%autopatch -p1
# End cabal-rpm setup

%build

%ghc_lib_build
%install
%ghc_lib_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-X11-devel -f %{oreon_filedir}/ghc-X11-devel.list
%files -n ghc-X11-doc -f %{oreon_filedir}/ghc-X11-doc.list
%files -n ghc-X11-prof -f %{oreon_filedir}/ghc-X11-prof.list

%changelog

%autochangelog
