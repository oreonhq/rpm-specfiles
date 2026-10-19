%global source0_hash 7346c5ad2172769e1e180f2b059b28c7003a7ce05c2850ba22f4377b3c8b103c
%global pkg_name gio
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.13.12.0
Release:        1%{?dist}
Summary:        Binding to GIO
License:        LGPL-2.1-or-later
URL:            https://hackage.haskell.org/package/gio
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
%if %{with ghc_prof}
%endif
# oreon:deps
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-array-prof
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-bytestring-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-glib-devel
BuildRequires:  ghc-glib-prof
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  pkgconfig(gio-2.0)
# /oreon:deps
%description
GIO is striving to provide a modern, easy-to-use VFS API that sits at the right
level in the library stack. The goal is to overcome the shortcomings of
GnomeVFS and provide an API that is so good that developers prefer it over raw
POSIX calls. Among other things that means using GObject. It also means not
cloning the POSIX API, but providing higher-level, document-centric interfaces.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gio-2.0)
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
rm -r %{buildroot}%{_datadir}/%{pkg_name}-%{version}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ghc-gio-devel -f %{oreon_filedir}/ghc-gio-devel.list
%files -n ghc-gio-doc -f %{oreon_filedir}/ghc-gio-doc.list
%files -n ghc-gio-prof -f %{oreon_filedir}/ghc-gio-prof.list

%changelog

%autochangelog
