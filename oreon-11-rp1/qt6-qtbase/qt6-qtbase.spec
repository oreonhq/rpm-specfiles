# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 5b2e00eccaf5a4d8c14134ffa0ea8dfd0a35ae1ffc7f8d87fa4305a1ed23cf22
%global qt_major 6
%global majmin 6.11

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name: qt6-qtbase
Version: 6.11.2
Release: 2%{?dist}
Summary: Qt6 - QtBase components
License: LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only
URL: https://www.qt.io/
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/qtbase-everywhere-src-%{version}.tar.xz

BuildRequires: oreon-rpm-macros
BuildRequires: qt6-srpm-macros
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: gcc
BuildRequires: gcc-c++
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(libpcre2-16)
BuildRequires: pkgconfig(icu-uc)
BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(libzstd)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-cursor)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-randr)
BuildRequires: pkgconfig(xcb-render)
BuildRequires: pkgconfig(xcb-renderutil)
BuildRequires: pkgconfig(xcb-shape)
BuildRequires: pkgconfig(xcb-shm)
BuildRequires: pkgconfig(xcb-sync)
BuildRequires: pkgconfig(xcb-xfixes)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xkbcommon)
BuildRequires: pkgconfig(xkbcommon-x11)
BuildRequires: vulkan-headers
%if %{without bootstrap}
BuildRequires: mesa-libGL-devel
%endif
BuildRequires: libX11-devel
BuildRequires: libXext-devel
BuildRequires: perl

%description
Qt6 QtBase module including Core Gui Widgets Network and related libraries.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Provides: qt6-qtbase-private-devel%{?_isa} = %{version}-%{release}
Provides: pkgconfig(Qt6Core) = %{version}
Provides: pkgconfig(Qt6Gui) = %{version}
Provides: pkgconfig(Qt6Widgets) = %{version}
Provides: pkgconfig(Qt6Network) = %{version}
Provides: pkgconfig(Qt6Test) = %{version}
Provides: pkgconfig(Qt6DBus) = %{version}
Provides: pkgconfig(Qt6Xml) = %{version}
Provides: pkgconfig(Qt6Concurrent) = %{version}
Provides: pkgconfig(Qt6OpenGL) = %{version}
Provides: pkgconfig(Qt6OpenGLWidgets) = %{version}
Provides: pkgconfig(Qt6PrintSupport) = %{version}
Provides: pkgconfig(Qt6Sql) = %{version}

%description devel
Header files and development tools for Qt6 QtBase.

%package gui
Summary: Qt6 GUI related libraries
Requires: %{name}%{?_isa} = %{version}-%{release}

%description gui
Qt6 GUI platform plugins and related libraries.

%prep
%oreon_sha256
%autosetup -n qtbase-everywhere-src-%{version}

%build
mkdir build
cd build
cmake .. -GNinja \
  -DCMAKE_INSTALL_PREFIX=%{_prefix} \
  -DCMAKE_BUILD_TYPE=Release \
  -DBUILD_SHARED_LIBS=ON \
  -DINSTALL_LIBDIR=%{_lib} \
  -DQT_FEATURE_system_zlib=ON \
  -DQT_FEATURE_system_png=ON \
  -DQT_FEATURE_system_jpeg=ON \
  -DQT_FEATURE_system_freetype=ON \
  -DQT_FEATURE_system_harfbuzz=OFF \
  -DQT_FEATURE_system_pcre2=ON \
  -DQT_FEATURE_icu=ON \
  -DQT_FEATURE_dbus=ON \
  -DQT_FEATURE_widgets=ON \
  -DQT_FEATURE_openssl_linked=ON \
  -DQT_BUILD_TESTS=ON \
  -DQT_BUILD_EXAMPLES=OFF \
  -DFEATURE_rpath=OFF \
%if %{with bootstrap}
  -DFEATURE_opengl=OFF \
  -DFEATURE_opengles2=OFF \
%endif
  %{nil}
%cmake_build

%install
cd build
%cmake_install

%check
cd build
export QT_QPA_PLATFORM=offscreen
export CTEST_OUTPUT_ON_FAILURE=1
%ctest

%files
%license LICENSES/*
%doc README.md
%{_libdir}/libQt6Core.so.*
%{_libdir}/libQt6Concurrent.so.*
%{_libdir}/libQt6DBus.so.*
%{_libdir}/libQt6Network.so.*
%{_libdir}/libQt6Sql.so.*
%{_libdir}/libQt6Test.so.*
%{_libdir}/libQt6Xml.so.*
%{_libdir}/libQt6Gui.so.*
%{_libdir}/libQt6Widgets.so.*
%{_libdir}/libQt6OpenGL.so.*
%{_libdir}/libQt6OpenGLWidgets.so.*
%{_libdir}/libQt6PrintSupport.so.*
%{_bindir}/qmake6
%{_bindir}/qtpaths6
%{_libdir}/qt6/

%files gui
%{_libdir}/qt6/plugins/

%files devel
%{_includedir}/qt6/
%{_libdir}/libQt6*.so
%{_libdir}/cmake/Qt6*/
%{_libdir}/pkgconfig/Qt6*.pc
%{_libdir}/pkgconfig/Qt6.pc

%changelog
%autochangelog
