%global source0_hash 09ba8a0756b26628126ab8edc6598e1c8c55fdb8ad56772605ad7079662454af
%global pkg_name gtk3
%global pkgver %{pkg_name}-%{version}
%{?haskell_setup}
Name:           ghc-%{pkg_name}
Version:        0.15.10
Release:        1%{?dist}
Summary:        Binding to the Gtk+ 3 graphical user interface library
License:        LGPL-2.1-or-later
URL:            https://hackage.haskell.org/package/gtk3
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
BuildRequires:  ghc-cairo-devel
BuildRequires:  ghc-cairo-prof
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-containers-prof
BuildRequires:  ghc-gio-devel
BuildRequires:  ghc-gio-prof
BuildRequires:  ghc-glib-devel
BuildRequires:  ghc-glib-prof
BuildRequires:  ghc-gtk2hs-buildtools-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-pango-devel
BuildRequires:  ghc-pango-prof
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-text-prof
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
# /oreon:deps
%description
This is the core library of the Gtk2Hs suite of libraries for Haskell based on
Gtk+. Gtk+ is an extensive and mature multi-platform toolkit for creating
graphical user interfaces.

%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(gthread-2.0)
Requires:       pkgconfig(gtk+-3.0)
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
%files -n ghc-gtk3-devel -f %{oreon_filedir}/ghc-gtk3-devel.list
%files -n ghc-gtk3-doc -f %{oreon_filedir}/ghc-gtk3-doc.list
%files -n ghc-gtk3-prof -f %{oreon_filedir}/ghc-gtk3-prof.list

%changelog

%autochangelog
