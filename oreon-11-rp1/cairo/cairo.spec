%global source0_hash 1c767308174337a74694da0f3ec069c271452163a1ef4540964c50c301f157d4
%define pixman_version 0.36.0
%define freetype_version 9.7.3
%define fontconfig_version 2.2.95
Name:           cairo
Version:        1.18.6
Release:        1%{?dist}
Summary:        A 2D graphics library
License:        LGPL-2.1-only OR MPL-1.1
URL:            https://cairographics.org
Source0:        https://cairographics.org/releases/%{name}-%{version}.tar.xz
Patch:          cairo-multilib.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(xcb-render)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
# /oreon:deps
%description
Cairo is a 2D graphics library designed to provide high-quality display
and print output. Currently supported output targets include the X Window
System, in-memory image buffers, and image files (PDF, PostScript, and SVG).

Cairo is designed to produce consistent output on all output media while
taking advantage of display hardware acceleration when available.

%package devel
Summary: Development files for cairo
Requires: %{name}%{?_isa} = %{version}-%{release}
%description devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo graphics library.

%package gobject
Summary: GObject bindings for cairo
Requires: %{name}%{?_isa} = %{version}-%{release}
%description gobject
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains functionality to make cairo graphics library
integrate well with the GObject object system used by GNOME.

%package gobject-devel
Summary: Development files for cairo-gobject
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: %{name}-gobject%{?_isa} = %{version}-%{release}
%description gobject-devel
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains libraries, header files and developer documentation
needed for developing software which uses the cairo Gobject library.

%package tools
Summary: Development tools for cairo
Requires: %{name}%{?_isa} = %{version}-%{release}
%description tools
Cairo is a 2D graphics library designed to provide high-quality display
and print output.

This package contains tools for working with the cairo graphics library.
 * cairo-trace: Record cairo library calls for later playback

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
  -Dfreetype=enabled \
  -Dfontconfig=enabled \
  -Dglib=enabled \
  -Dgtk_doc=true \
  -Dspectre=disabled \
  -Dsymbol-lookup=disabled \
  -Dtee=enabled \
  -Dtests=disabled \
  -Dxcb=enabled \
  -Dxlib=enabled \
  %{nil}
%meson_build
%install
%meson_install
%oreon_autofiles cairo-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cairo-gobject usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles cairo-gobject-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cairo-tools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cairo-devel -f %{oreon_filedir}/cairo-devel.list
%files -n cairo-gobject -f %{oreon_filedir}/cairo-gobject.list
%files -n cairo-gobject-devel -f %{oreon_filedir}/cairo-gobject-devel.list
%files -n cairo-tools -f %{oreon_filedir}/cairo-tools.list

%changelog

%autochangelog
