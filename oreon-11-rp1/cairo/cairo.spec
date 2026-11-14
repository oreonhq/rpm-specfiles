# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 1c767308174337a74694da0f3ec069c271452163a1ef4540964c50c301f157d4

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

%global pixman_version 0.40.0
%global freetype_version 9.7.3
%global fontconfig_version 2.2.95

Name: cairo
Version: 1.18.6
Release: 2%{?dist}
Summary: A 2D graphics library
License: LGPL-2.1-only OR MPL-1.1
URL: https://cairographics.org
Source0: https://cairographics.org/releases/%{name}-%{version}.tar.xz

Patch0: cairo-multilib.patch

BuildRequires: oreon-rpm-macros
BuildRequires: gcc
BuildRequires: gcc-c++
%if %{without bootstrap}
BuildRequires: gtk-doc
%endif
BuildRequires: meson
BuildRequires: pkgconfig(expat)
BuildRequires: pkgconfig(pixman-1) >= %{pixman_version}
BuildRequires: pkgconfig(freetype2) >= %{freetype_version}
BuildRequires: pkgconfig(fontconfig) >= %{fontconfig_version}
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(lzo2)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(zlib)

%description
Cairo is a 2D graphics library designed to provide high-quality display
and print output. Currently supported output targets include the X Window
System, in-memory image buffers, and image files (PDF, PostScript, and SVG).

Cairo is designed to produce consistent output on all output media while
taking advantage of display hardware acceleration when available.

%package devel
Summary: Development files for cairo
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Provides: pkgconfig(cairo) = %{version}

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
Provides: pkgconfig(cairo-gobject) = %{version}

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
%oreon_sha256

%autosetup -p1

%build
%meson \
  -Dfreetype=enabled \
  -Dfontconfig=enabled \
  -Dglib=enabled \
%if %{with bootstrap}
  -Dgtk_doc=false \
%else
  -Dgtk_doc=true \
%endif
  -Dspectre=disabled \
  -Dsymbol-lookup=disabled \
  -Dtee=enabled \
  -Dtests=enabled \
  -Dxcb=enabled \
  -Dxlib=enabled \
  %{nil}
%meson_build

%install
%meson_install

%check
%meson_test

%ldconfig_post
%ldconfig_postun

%files
%license COPYING COPYING-LGPL-2.1 COPYING-MPL-1.1
%doc AUTHORS BUGS NEWS README.md
%{_libdir}/libcairo.so.2*
%{_libdir}/libcairo-script-interpreter.so.2*

%files devel
%dir %{_includedir}/cairo/
%{_includedir}/cairo/cairo-deprecated.h
%{_includedir}/cairo/cairo-features.h
%{_includedir}/cairo/cairo-ft.h
%{_includedir}/cairo/cairo.h
%{_includedir}/cairo/cairo-pdf.h
%{_includedir}/cairo/cairo-ps.h
%{_includedir}/cairo/cairo-script-interpreter.h
%{_includedir}/cairo/cairo-svg.h
%{_includedir}/cairo/cairo-tee.h
%{_includedir}/cairo/cairo-version.h
%{_includedir}/cairo/cairo-xlib-xrender.h
%{_includedir}/cairo/cairo-xlib.h
%{_includedir}/cairo/cairo-script.h
%{_includedir}/cairo/cairo-xcb.h
%{_libdir}/libcairo.so
%{_libdir}/libcairo-script-interpreter.so
%{_libdir}/pkgconfig/cairo-fc.pc
%{_libdir}/pkgconfig/cairo-ft.pc
%{_libdir}/pkgconfig/cairo.pc
%{_libdir}/pkgconfig/cairo-pdf.pc
%{_libdir}/pkgconfig/cairo-png.pc
%{_libdir}/pkgconfig/cairo-ps.pc
%{_libdir}/pkgconfig/cairo-script-interpreter.pc
%{_libdir}/pkgconfig/cairo-svg.pc
%{_libdir}/pkgconfig/cairo-tee.pc
%{_libdir}/pkgconfig/cairo-xlib.pc
%{_libdir}/pkgconfig/cairo-xlib-xrender.pc
%{_libdir}/pkgconfig/cairo-script.pc
%{_libdir}/pkgconfig/cairo-xcb-shm.pc
%{_libdir}/pkgconfig/cairo-xcb.pc
%if %{without bootstrap}
%{_datadir}/gtk-doc/html/cairo
%endif

%files gobject
%{_libdir}/libcairo-gobject.so.2*

%files gobject-devel
%{_includedir}/cairo/cairo-gobject.h
%{_libdir}/libcairo-gobject.so
%{_libdir}/pkgconfig/cairo-gobject.pc

%files tools
%{_bindir}/cairo-trace
%{_libdir}/cairo/

%changelog
%autochangelog
