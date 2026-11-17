# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 41c32680160addf5a8dd7a830e4869c01e9f6bee1abb91e44fabd1ba9d7828fb
%global source1_hash 2e355a9de298e5ced4245258193c126e16ea5cfb0c937aeb276754e9fff249ac
%global poppler_test 0ef006dca68d2206387eca1d36ae06733812e387

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: poppler
Version: 26.11.0
Release: 1%{?dist}
Summary: PDF rendering library
License: GPL-2.0-or-later
URL: https://poppler.freedesktop.org/
Source0: https://poppler.freedesktop.org/poppler-%{version}.tar.xz
Source1: https://gitlab.freedesktop.org/poppler/test/-/archive/%{poppler_test}/test-%{poppler_test}.tar.gz

BuildRequires: oreon-rpm-macros >= 1-14
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: gettext
BuildRequires: gobject-introspection-devel
BuildRequires: gtk-doc
BuildRequires: pkgconf
BuildRequires: python3
BuildRequires: pkgconfig(cairo) >= 1.18.0
BuildRequires: pkgconfig(fontconfig) >= 2.15
BuildRequires: pkgconfig(freetype2) >= 2.13
BuildRequires: pkgconfig(gio-2.0) >= 2.80
BuildRequires: pkgconfig(glib-2.0) >= 2.80
BuildRequires: pkgconfig(gobject-2.0) >= 2.80
BuildRequires: pkgconfig(gobject-introspection-1.0) >= 1.80
BuildRequires: pkgconfig(harfbuzz)
BuildRequires: pkgconfig(harfbuzz-subset)
BuildRequires: pkgconfig(lcms2) >= 2.14
BuildRequires: pkgconfig(libbrotlidec) >= 1.1
BuildRequires: pkgconfig(libcurl) >= 8.5
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(libopenjp2)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libtiff-4) >= 4.5
BuildRequires: pkgconfig(nss) >= 3.98
BuildRequires: pkgconfig(poppler-data)
BuildRequires: pkgconfig(Qt6Core) >= 6.4
BuildRequires: pkgconfig(Qt6Gui) >= 6.4
BuildRequires: pkgconfig(Qt6Test) >= 6.4
BuildRequires: pkgconfig(Qt6Widgets) >= 6.4
BuildRequires: pkgconfig(zlib)

%description
Poppler is a PDF rendering library.

%package devel
Summary: Development files for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig(freetype2)
Requires: pkgconfig(fontconfig)
Provides: pkgconfig(poppler) = %{version}

%description devel
Headers and the pkg-config file for the poppler library.

%package glib
Summary: GLib wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}

%description glib
GLib bindings for poppler. Cairo tests render PDF pages through this library.

%package glib-devel
Summary: Development files for the poppler GLib wrapper
Requires: %{name}-glib%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig(cairo)
Requires: pkgconfig(glib-2.0)
Provides: pkgconfig(poppler-glib) = %{version}

%description glib-devel
Headers, the pkg-config file and the introspection data for poppler-glib.

%package cpp
Summary: C++ wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}

%description cpp
C++ bindings for poppler.

%package cpp-devel
Summary: Development files for the poppler C++ wrapper
Requires: %{name}-cpp%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(poppler-cpp) = %{version}

%description cpp-devel
Headers and the pkg-config file for poppler-cpp.

%package qt6
Summary: Qt6 wrapper for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase%{?_isa}

%description qt6
Qt6 bindings for poppler.

%package qt6-devel
Summary: Development files for the poppler Qt6 wrapper
Requires: %{name}-qt6%{?_isa} = %{version}-%{release}
Requires: %{name}-devel%{?_isa} = %{version}-%{release}
Requires: pkgconfig(Qt6Core)
Requires: pkgconfig(Qt6Gui)
Provides: pkgconfig(poppler-qt6) = %{version}

%description qt6-devel
Headers and the pkg-config file for poppler-qt6.

%package utils
Summary: Command line tools for poppler
Requires: %{name}%{?_isa} = %{version}-%{release}

%description utils
pdfinfo, pdftotext, pdftoppm, pdftocairo and the other poppler tools.

%package doc
Summary: API documentation for poppler-glib
BuildArch: noarch

%description doc
gtk-doc documentation for the poppler GLib API.

%prep
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -
%autosetup
tar -C %{_builddir} -xf %{SOURCE1}

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DENABLE_BOOST=ON \
  -DENABLE_CPP=ON \
  -DENABLE_GLIB=ON \
  -DENABLE_GOBJECT_INTROSPECTION=ON \
  -DENABLE_GPGME=OFF \
  -DENABLE_GTK_DOC=ON \
  -DENABLE_LIBCURL=ON \
  -DENABLE_LIBJPEG=ON \
  -DENABLE_LIBOPENJPEG=ON \
  -DENABLE_LIBTIFF=ON \
  -DENABLE_LCMS=ON \
  -DENABLE_NSS3=ON \
  -DENABLE_QT5=OFF \
  -DENABLE_QT6=ON \
  -DENABLE_UNSTABLE_API_ABI_HEADERS=OFF \
  -DENABLE_UTILS=ON \
  -DENABLE_ZLIB_UNCOMPRESS=OFF \
  -DTESTDATADIR=%{_builddir}/test-%{poppler_test}
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets
%ldconfig_scriptlets glib
%ldconfig_scriptlets cpp
%ldconfig_scriptlets qt6

%files
%license COPYING COPYING3
%doc AUTHORS README.md
%{_libdir}/libpoppler.so.166*

%files devel
%{_includedir}/poppler/*.h
%{_libdir}/libpoppler.so
%{_libdir}/pkgconfig/poppler.pc

%files glib
%{_libdir}/libpoppler-glib.so.8*

%files glib-devel
%{_includedir}/poppler/glib/
%{_libdir}/libpoppler-glib.so
%{_libdir}/pkgconfig/poppler-glib.pc
%{_libdir}/girepository-1.0/Poppler-0.18.typelib
%{_datadir}/gir-1.0/Poppler-0.18.gir

%files cpp
%{_libdir}/libpoppler-cpp.so.3*

%files cpp-devel
%{_includedir}/poppler/cpp/
%{_libdir}/libpoppler-cpp.so
%{_libdir}/pkgconfig/poppler-cpp.pc

%files qt6
%{_libdir}/libpoppler-qt6.so.3*

%files qt6-devel
%{_includedir}/poppler/qt6/
%{_libdir}/libpoppler-qt6.so
%{_libdir}/pkgconfig/poppler-qt6.pc

%files utils
%{_bindir}/pdfattach
%{_bindir}/pdfdetach
%{_bindir}/pdffonts
%{_bindir}/pdfimages
%{_bindir}/pdfinfo
%{_bindir}/pdfseparate
%{_bindir}/pdfsig
%{_bindir}/pdftocairo
%{_bindir}/pdftohtml
%{_bindir}/pdftoppm
%{_bindir}/pdftops
%{_bindir}/pdftotext
%{_bindir}/pdfunite
%{_mandir}/man1/pdf*.1*
%{_datadir}/locale/ca/LC_MESSAGES/pdfsig.mo

%files doc
%{_datadir}/gtk-doc/html/poppler/

%changelog
%autochangelog
