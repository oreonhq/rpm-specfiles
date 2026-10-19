%global source0_hash aea196550f02974d6d09291c5d83b51ca6a03b3767e234a8c0e21322927d1e12
%bcond_without  gstreamer
%bcond_without  gdal
%bcond_with  Inventor
%bcond_with  Coin4
%bcond_without  jasper
%bcond_without  OpenEXR
%bcond_without  Collada
%bcond_with wxWidgets
%bcond_with mingw
Name:           OpenSceneGraph
Version:        3.6.5
Release:        1%{?dist}
Summary:        High performance real-time graphics toolkit
License:        LGPL-2.1-only WITH WxWindows-exception-3.1
URL:            http://www.openscenegraph.org/
Source0:        https://github.com/openscenegraph/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
Patch1:         0001-Cmake-fixes.patch
Patch2:         0002-Activate-osgviewerWX.patch
Patch3:         0003-Unset-DOT_FONTNAME.patch
Patch4:         0004-Re-add-osgframerenderer.patch
Patch5:         force-x11-backend.patch
Patch6:         OpenSceneGraph-openexr3.patch
Patch7:         OpenSceneGraph_asio.patch
Patch8:         OpenSceneGraph_mingw.patch
Patch9:         OpenSceneGraph_gta.patch
Patch10:        OpenSceneGraph_cmakever.patch
Patch11:        OpenSceneGraph_externc.patch
%{?with_OpenEXR:BuildRequires:    cmake(OpenEXR)}
%{?with_Collada:BuildRequires:    pkgconfig(collada-dom)}
%{?with_jasper:BuildRequires:     jasper-devel}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-base-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-app-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-audio-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-fft-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)}
%{?with_gstreamer:BuildRequires:  pkgconfig(gstreamer-video-1.0)}
%{?with_gdal:BuildRequires:       gdal-devel}
%{?with_Inventor:BuildRequires:   Inventor-devel}
%{?with_Coin4:BuildRequires:      Coin4-devel}
%{?with_wxWidgets:BuildRequires:  wxGTK-devel}
%if %{with mingw}
%{?with_OpenEXR:BuildRequires:    mingw32-openexr}
%{?with_jasper:BuildRequires:     mingw32-jasper}
%{?with_gstreamer:BuildRequires:  mingw32-gstreamer1}
%{?with_gdal:BuildRequires:       mingw32-gdal}
%{?with_OpenEXR:BuildRequires:    mingw64-openexr}
%{?with_jasper:BuildRequires:     mingw64-jasper}
%{?with_gstreamer:BuildRequires:  mingw64-gstreamer1}
%{?with_gdal:BuildRequires:       mingw64-gdal}
%endif
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  Coin4-devel
BuildRequires:  SDL-devel
BuildRequires:  SDL2-devel
BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  cmake(OpenEXR)
BuildRequires:  doxygen
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  gdal-devel
BuildRequires:  giflib-devel
BuildRequires:  gnuplot
BuildRequires:  graphviz
BuildRequires:  jasper-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libcurl-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvncserver-devel
BuildRequires:  libxml2-devel
BuildRequires:  mingw32-cairo
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-gdal
BuildRequires:  mingw32-gstreamer1
BuildRequires:  mingw32-jasper
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-librsvg2
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-openal-soft
BuildRequires:  mingw32-openexr
BuildRequires:  mingw32-poppler-glib
BuildRequires:  mingw64-cairo
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-gdal
BuildRequires:  mingw64-gstreamer1
BuildRequires:  mingw64-jasper
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-librsvg2
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-openal-soft
BuildRequires:  mingw64-openexr
BuildRequires:  mingw64-poppler-glib
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(collada-dom)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-app-1.0)
BuildRequires:  pkgconfig(gstreamer-audio-1.0)
BuildRequires:  pkgconfig(gstreamer-base-1.0)
BuildRequires:  pkgconfig(gstreamer-fft-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gta)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-x11-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  wxGTK-devel
# /oreon:deps
%description
The OpenSceneGraph is an OpenSource, cross platform graphics toolkit for the
development of high performance graphics applications such as flight
simulators, games, virtual reality and scientific visualization.
Based around the concept of a SceneGraph, it provides an object oriented
framework on top of OpenGL freeing the developer from implementing and
optimizing low level graphics calls, and provides many additional utilities
for rapid development of graphics applications.

%package libs
Summary:        Runtime libraries for OpenSceneGraph
%description libs
Runtime libraries files for OpenSceneGraph.

%if %{with gdal}
%package gdal
Summary:        OSG Gdal plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
%description gdal
OSG Gdal plugin.
%endif

%if %{with Collada}
%package Collada
Summary:        OSG Collada plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
%description Collada
OSG Collada plugin.
%endif

%if %{with OpenEXR}
%package OpenEXR
Summary:        OSG OpenEXR plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
%description OpenEXR
OSG OpenEXR plugin.
%endif

%if %{with gstreamer}
%package gstreamer
Summary:        OSG gstreamer plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
%description gstreamer
OSG gstreamer plugin.
%endif

%if %{with Inventor}
%package inventor
Summary:        OSG inventor plugin
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
%description inventor
OSG inventor plugin.
%endif

%package devel
Summary:        Development files for OpenSceneGraph
Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}
Requires:       OpenThreads-devel%{?_isa} = %{version}-%{release}
%description devel
Development files for OpenSceneGraph.

%package examples
Summary:        Sample applications for OpenSceneGraph
%description examples
Sample applications for OpenSceneGraph

%package examples-SDL
Summary:        OSG sample applications using SDL
%description examples-SDL
OSG sample applications using SDL.

%package examples-fltk
Summary:        OSG sample applications using FLTK
%description examples-fltk
OSG sample applications using FLTK.

%package examples-gtk
Summary:        OSG sample applications using gtk
%description examples-gtk
OSG sample applications using gtk

%package -n OpenThreads
Summary:        OpenThreads
%description -n OpenThreads
OpenThreads is intended to provide a minimal & complete Object-Oriented (OO)
thread interface for C++ programmers.  It is loosely modeled on the Java
thread API, and the POSIX Threads standards.  The architecture of the
library is designed around "swappable" thread models which are defined at
compile-time in a shared object library.

%package -n OpenThreads-devel
Summary:        Devel files for OpenThreads
Requires:       OpenThreads%{?_isa} = %{version}-%{release}
%description -n OpenThreads-devel
Development files for OpenThreads.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw64-%{name}
MinGW Windows %{name} library.

%package -n mingw32-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw32-%{name}-tools
Tools for the MinGW Windows %{name} library.

%package -n mingw64-%{name}-tools
Summary:       Tools for the MinGW Windows %{name} library
BuildArch:     noarch
%description -n mingw64-%{name}-tools
Tools for the MinGW Windows %{name} library.
%endif

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{name}-%{version}%{?pre:-%pre}

# Also look in /usr/share/fonts for fonts
sed -i -e 's,\.:/usr/share/fonts/ttf:,.:%{_datadir}/fonts:/usr/share/fonts/ttf:,' \
src/osgText/Font.cpp

iconv -f ISO-8859-1 -t utf-8 AUTHORS.txt > AUTHORS.txt~
mv AUTHORS.txt~ AUTHORS.txt

# Update doxygen
doxygen -u doc/Doxyfiles/doxyfile.cmake
doxygen -u doc/Doxyfiles/openthreads.doxyfile.cmake

%build

%cmake -G Ninja -DBUILD_OSG_EXAMPLES=ON -DBUILD_DOCUMENTATION=ON \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DLIB_POSTFIX=%(l=%{_lib}; echo ${l:3}) \
  %{?with_Collada:-DCOLLADA_INCLUDE_DIR=$(pkg-config collada-dom --variable=includedir)}
%cmake_build
%cmake_build --target doc_openscenegraph
%cmake_build --target doc_openthreads
%if %{with mingw}
%mingw_cmake -G Ninja \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DOSG_DETERMINE_WIN_VERSION=OFF
%mingw_ninja
%endif
%install
%cmake_install
mkdir -p %{buildroot}%{_datadir}/OpenSceneGraph
%if %{with mingw}
%mingw_ninja_install
%mingw_debug_install_post
%oreon_autofiles OpenThreads usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles OpenThreads-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%endif
%files -f %{oreon_filedir}/main.list
%files -n OpenThreads -f %{oreon_filedir}/OpenThreads.list
%files -n OpenThreads-devel -f %{oreon_filedir}/OpenThreads-devel.list

%changelog

%autochangelog
