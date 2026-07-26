%global source0_hash aea196550f02974d6d09291c5d83b51ca6a03b3767e234a8c0e21322927d1e12

# Copyright (c) 2005 - 2020 Ralf Corsepius, Ulm, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.

# GStreamer support: Default on
%bcond_without  gstreamer

# GDal support: Default on
%bcond_without  gdal

# Inventor support: Default to Coin4
# These are mutually exclusive
%if 0%{?fedora}
%bcond_with     Inventor
%bcond_without  Coin4
%else
%bcond_with  Inventor
%bcond_with  Coin4
%endif

# Jasper support: Default on
%bcond_without  jasper

# OpenEXR support: Default on
%bcond_without  OpenEXR

# Collada support: Default on
%bcond_without  Collada

# Build wxWidgets example: Default on
%if 0%{?fedora}
%bcond_without wxWidgets
%else
%bcond_with wxWidgets
%endif

%if 0%{?fedora}
%bcond_without mingw
%else
%bcond_with mingw
%endif

Name:           OpenSceneGraph
Version:        3.6.5
Release:        45%{?dist}
Summary:        High performance real-time graphics toolkit

# The OSGPL is just the wxWidgets license.
License:        LGPL-2.1-only WITH WxWindows-exception-3.1
URL:            http://www.openscenegraph.org/
Source0:        https://github.com/openscenegraph/%{name}/archive/%{name}-%{version}/%{name}-%{version}.tar.gz

Patch1:         0001-Cmake-fixes.patch
# Upstream deactivated building osgviewerWX for obscure reasons
# Reactivate for now.
Patch2:         0002-Activate-osgviewerWX.patch
# Unset DOT_FONTNAME
Patch3:         0003-Unset-DOT_FONTNAME.patch
# Re-add osgframerenderer
Patch4:         0004-Re-add-osgframerenderer.patch
# Force osgviewerWX to always use X11 backend (wxGLCanvas is broken on Wayland)
Patch5:         force-x11-backend.patch
# Minimal port to OpenEXR 3
# https://github.com/openscenegraph/OpenSceneGraph/issues/1075
Patch6:         OpenSceneGraph-openexr3.patch
# Fix build against recent asio
Patch7:         OpenSceneGraph_asio.patch
# Fix mingw build (symbol collision due to namespace ordering, narrowing conversion error)
Patch8:         OpenSceneGraph_mingw.patch
# Fix linking against gta
Patch9:         OpenSceneGraph_gta.patch
# Increase minimum required cmake version
Patch10:        OpenSceneGraph_cmakever.patch
# Drop bogous extern C when including librsvg2
Patch11:        OpenSceneGraph_externc.patch

BuildRequires:  asio-devel
BuildRequires:  cmake
BuildRequires:  doxygen graphviz
BuildRequires:  fltk-devel
BuildRequires:  gcc-c++
BuildRequires:  giflib-devel
BuildRequires:  gnuplot
BuildRequires:  libcurl-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvncserver-devel
BuildRequires:  libxml2-devel
BuildRequires:  libXmu-devel
BuildRequires:  libX11-devel
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gta)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-x11-1.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(librsvg-2.0) >= 2.35
BuildRequires:  pkgconfig(xrandr)

# Used by osgmovie
BuildRequires:  SDL2-devel
# Used by SDL-examples
BuildRequires:  SDL-devel

# Optional
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
BuildRequires: mingw32-cairo
BuildRequires: mingw32-curl
BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-libjpeg-turbo
BuildRequires: mingw32-libpng
BuildRequires: mingw32-librsvg2
BuildRequires: mingw32-libtiff
BuildRequires: mingw32-libxml2
BuildRequires: mingw32-openal-soft
BuildRequires: mingw32-poppler-glib

# Optional
%{?with_OpenEXR:BuildRequires:    mingw32-openexr}
%{?with_jasper:BuildRequires:     mingw32-jasper}
%{?with_gstreamer:BuildRequires:  mingw32-gstreamer1}
%{?with_gdal:BuildRequires:       mingw32-gdal}

BuildRequires: mingw64-cairo
BuildRequires: mingw64-curl
BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-libjpeg-turbo
BuildRequires: mingw64-libpng
BuildRequires: mingw64-librsvg2
BuildRequires: mingw64-libtiff
BuildRequires: mingw64-libxml2
BuildRequires: mingw64-openal-soft
BuildRequires: mingw64-poppler-glib

# Optional
%{?with_OpenEXR:BuildRequires:    mingw64-openexr}
%{?with_jasper:BuildRequires:     mingw64-jasper}
%{?with_gstreamer:BuildRequires:  mingw64-gstreamer1}
%{?with_gdal:BuildRequires:       mingw64-gdal}
%endif

Requires:       OpenSceneGraph-libs%{?_isa} = %{version}-%{release}

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
# Native build
%cmake -G Ninja -DBUILD_OSG_EXAMPLES=ON -DBUILD_DOCUMENTATION=ON \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DLIB_POSTFIX=%(l=%{_lib}; echo ${l:3}) \
  %{?with_Collada:-DCOLLADA_INCLUDE_DIR=$(pkg-config collada-dom --variable=includedir)}
%cmake_build

%cmake_build --target doc_openscenegraph
%cmake_build --target doc_openthreads

# MinGW build
# We are cross-compiling and TryRun fails
%if %{with mingw}
%mingw_cmake -G Ninja \
  -DOSG_AGGRESSIVE_WARNING_FLAGS=OFF \
  -DOSG_DETERMINE_WIN_VERSION=OFF
%mingw_ninja
%endif

%install
%cmake_install
# Supposed to take OpenSceneGraph data
mkdir -p %{buildroot}%{_datadir}/OpenSceneGraph

%if %{with mingw}
%mingw_ninja_install

%mingw_debug_install_post

%endif

%files
%{_bindir}/osgarchive
%{_bindir}/osgconv
%{_bindir}/osgversion
%{_bindir}/osgviewer
%{_bindir}/osgfilecache
%{_bindir}/present3D

%files libs
%doc AUTHORS.txt NEWS.txt README.md
%license LICENSE.txt
%dir %{_libdir}/osgPlugins-%{version}
%{_libdir}/osgPlugins-%{version}/osgdb_3dc.so
%{_libdir}/osgPlugins-%{version}/osgdb_3ds.so
%{_libdir}/osgPlugins-%{version}/osgdb_ac.so
%{_libdir}/osgPlugins-%{version}/osgdb_bmp.so
%{_libdir}/osgPlugins-%{version}/osgdb_bsp.so
%{_libdir}/osgPlugins-%{version}/osgdb_bvh.so
%{_libdir}/osgPlugins-%{version}/osgdb_cfg.so
%{_libdir}/osgPlugins-%{version}/osgdb_curl.so
%{_libdir}/osgPlugins-%{version}/osgdb_dds.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osganimation.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgfx.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgparticle.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgsim.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgtext.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgvolume.so
%{_libdir}/osgPlugins-%{version}/osgdb_deprecated_osgwidget.so
%{_libdir}/osgPlugins-%{version}/osgdb_dot.so
%{_libdir}/osgPlugins-%{version}/osgdb_dxf.so
%{_libdir}/osgPlugins-%{version}/osgdb_freetype.so
%{_libdir}/osgPlugins-%{version}/osgdb_gif.so
%{_libdir}/osgPlugins-%{version}/osgdb_gles.so
%{_libdir}/osgPlugins-%{version}/osgdb_glsl.so
%{_libdir}/osgPlugins-%{version}/osgdb_gta.so
%{_libdir}/osgPlugins-%{version}/osgdb_gz.so
%{_libdir}/osgPlugins-%{version}/osgdb_hdr.so
%{_libdir}/osgPlugins-%{version}/osgdb_ive.so
%{?with_jasper:%{_libdir}/osgPlugins-%{version}/osgdb_jp2.so}
%{_libdir}/osgPlugins-%{version}/osgdb_jpeg.so
%{_libdir}/osgPlugins-%{version}/osgdb_ktx.so
%{_libdir}/osgPlugins-%{version}/osgdb_las.so
%{_libdir}/osgPlugins-%{version}/osgdb_logo.so
%{_libdir}/osgPlugins-%{version}/osgdb_lua.so
%{_libdir}/osgPlugins-%{version}/osgdb_lwo.so
%{_libdir}/osgPlugins-%{version}/osgdb_lws.so
%{_libdir}/osgPlugins-%{version}/osgdb_md2.so
%{_libdir}/osgPlugins-%{version}/osgdb_mdl.so
%{_libdir}/osgPlugins-%{version}/osgdb_normals.so
%{_libdir}/osgPlugins-%{version}/osgdb_obj.so
%{_libdir}/osgPlugins-%{version}/osgdb_openflight.so
%{_libdir}/osgPlugins-%{version}/osgdb_osc.so
%{_libdir}/osgPlugins-%{version}/osgdb_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_osga.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgjs.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgtgz.so
%{_libdir}/osgPlugins-%{version}/osgdb_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_p3d.so
%{_libdir}/osgPlugins-%{version}/osgdb_pdf.so
%{_libdir}/osgPlugins-%{version}/osgdb_pic.so
%{_libdir}/osgPlugins-%{version}/osgdb_ply.so
%{_libdir}/osgPlugins-%{version}/osgdb_png.so
%{_libdir}/osgPlugins-%{version}/osgdb_pnm.so
%{_libdir}/osgPlugins-%{version}/osgdb_pov.so
%{_libdir}/osgPlugins-%{version}/osgdb_pvr.so
%{_libdir}/osgPlugins-%{version}/osgdb_resthttp.so
%{_libdir}/osgPlugins-%{version}/osgdb_revisions.so
%{_libdir}/osgPlugins-%{version}/osgdb_rgb.so
%{_libdir}/osgPlugins-%{version}/osgdb_rot.so
%{_libdir}/osgPlugins-%{version}/osgdb_scale.so
%{_libdir}/osgPlugins-%{version}/osgdb_sdl.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osg.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osganimation.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgfx.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgga.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgmanipulator.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgparticle.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgshadow.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgsim.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgterrain.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgtext.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgui.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgutil.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgviewer.so
%{_libdir}/osgPlugins-%{version}/osgdb_serializers_osgvolume.so
%{_libdir}/osgPlugins-%{version}/osgdb_shp.so
%{_libdir}/osgPlugins-%{version}/osgdb_stl.so
%{_libdir}/osgPlugins-%{version}/osgdb_svg.so
%{_libdir}/osgPlugins-%{version}/osgdb_tf.so
%{_libdir}/osgPlugins-%{version}/osgdb_tga.so
%{_libdir}/osgPlugins-%{version}/osgdb_tgz.so
%{_libdir}/osgPlugins-%{version}/osgdb_tiff.so
%{_libdir}/osgPlugins-%{version}/osgdb_trans.so
%{_libdir}/osgPlugins-%{version}/osgdb_trk.so
%{_libdir}/osgPlugins-%{version}/osgdb_txf.so
%{_libdir}/osgPlugins-%{version}/osgdb_txp.so
%{_libdir}/osgPlugins-%{version}/osgdb_vnc.so
%{_libdir}/osgPlugins-%{version}/osgdb_vtf.so
%{_libdir}/osgPlugins-%{version}/osgdb_x.so
%exclude %{_libdir}/osgPlugins-%{version}/osgdb_zip.so
%{_libdir}/libosgAnimation.so.*
%{_libdir}/libosgDB.so.*
%{_libdir}/libosgFX.so.*
%{_libdir}/libosgGA.so.*
%{_libdir}/libosgManipulator.so.*
%{_libdir}/libosgParticle.so.*
%{_libdir}/libosgPresentation.so.*
%{_libdir}/libosgShadow.so.*
%{_libdir}/libosgSim.so.*
%{_libdir}/libosg.so.*
%{_libdir}/libosgTerrain.so.*
%{_libdir}/libosgText.so.*
%{_libdir}/libosgUI.so.*
%{_libdir}/libosgUtil.so.*
%{_libdir}/libosgViewer.so.*
%{_libdir}/libosgVolume.so.*
%{_libdir}/libosgWidget.so.*

%if %{with gdal}
%files gdal
%{_libdir}/osgPlugins-%{version}/osgdb_gdal.so
%{_libdir}/osgPlugins-%{version}/osgdb_ogr.so
%endif

%if %{with Collada}
%files Collada
%{_libdir}/osgPlugins-%{version}/osgdb_dae.so
%endif

%if %{with OpenEXR}
%files OpenEXR
%{_libdir}/osgPlugins-%{version}/osgdb_exr.so
%endif

%if %{with gstreamer}
%files gstreamer
%{_libdir}/osgPlugins-%{version}/osgdb_gstreamer.so
%endif

%if %{with Inventor}
%files inventor
%{_libdir}/osgPlugins-%{version}/osgdb_iv.so
%endif

%files devel
%doc %{_vpath_builddir}/doc/OpenSceneGraphReferenceDocs
%{_includedir}/osg
%{_includedir}/osgAnimation
%{_includedir}/osgDB
%{_includedir}/osgFX
%{_includedir}/osgGA
%{_includedir}/osgManipulator
%{_includedir}/osgParticle
%{_includedir}/osgPresentation
%{_includedir}/osgShadow
%{_includedir}/osgSim
%{_includedir}/osgTerrain
%{_includedir}/osgText
%{_includedir}/osgUI
%{_includedir}/osgUtil
%{_includedir}/osgViewer
%{_includedir}/osgVolume
%{_includedir}/osgWidget
%{_libdir}/libosgAnimation.so
%{_libdir}/libosgDB.so
%{_libdir}/libosgFX.so
%{_libdir}/libosgGA.so
%{_libdir}/libosgManipulator.so
%{_libdir}/libosgParticle.so
%{_libdir}/libosgPresentation.so
%{_libdir}/libosgShadow.so
%{_libdir}/libosgSim.so
%{_libdir}/libosg.so
%{_libdir}/libosgTerrain.so
%{_libdir}/libosgText.so
%{_libdir}/libosgUI.so
%{_libdir}/libosgUtil.so
%{_libdir}/libosgViewer.so
%{_libdir}/libosgVolume.so
%{_libdir}/libosgWidget.so
%{_libdir}/pkgconfig/openscenegraph-osgAnimation.pc
%{_libdir}/pkgconfig/openscenegraph-osgDB.pc
%{_libdir}/pkgconfig/openscenegraph-osgFX.pc
%{_libdir}/pkgconfig/openscenegraph-osgGA.pc
%{_libdir}/pkgconfig/openscenegraph-osgManipulator.pc
%{_libdir}/pkgconfig/openscenegraph-osgParticle.pc
%{_libdir}/pkgconfig/openscenegraph-osg.pc
%{_libdir}/pkgconfig/openscenegraph-osgShadow.pc
%{_libdir}/pkgconfig/openscenegraph-osgSim.pc
%{_libdir}/pkgconfig/openscenegraph-osgTerrain.pc
%{_libdir}/pkgconfig/openscenegraph-osgText.pc
%{_libdir}/pkgconfig/openscenegraph-osgUtil.pc
%{_libdir}/pkgconfig/openscenegraph-osgViewer.pc
%{_libdir}/pkgconfig/openscenegraph-osgVolume.pc
%{_libdir}/pkgconfig/openscenegraph-osgWidget.pc
%{_libdir}/pkgconfig/openscenegraph.pc

%files examples
%{_bindir}/osg2cpp
%{_bindir}/osganalysis
%{_bindir}/osganimate
%{_bindir}/osganimationeasemotion
%{_bindir}/osganimationhardware
%{_bindir}/osganimationmakepath
%{_bindir}/osganimationmorph
%{_bindir}/osganimationnode
%{_bindir}/osganimationskinning
%{_bindir}/osganimationsolid
%{_bindir}/osganimationtimeline
%{_bindir}/osganimationviewer
%{_bindir}/osgatomiccounter
%{_bindir}/osgautocapture
%{_bindir}/osgautotransform
%{_bindir}/osgbillboard
%{_bindir}/osgbindlesstext
%{_bindir}/osgblenddrawbuffers
%{_bindir}/osgblendequation
%{_bindir}/osgcallback
%{_bindir}/osgcamera
%{_bindir}/osgcatch
%{_bindir}/osgclip
%{_bindir}/osgcluster
%{_bindir}/osgcompositeviewer
%{_bindir}/osgcomputeshaders
%{_bindir}/osgcopy
%{_bindir}/osgcubemap
%{_bindir}/osgdatabaserevisions
%{_bindir}/osgdeferred
%{_bindir}/osgdepthpartition
%{_bindir}/osgdepthpeeling
%{_bindir}/osgdistortion
%{_bindir}/osgdrawinstanced
%{_bindir}/osgfadetext
%{_bindir}/osgfont
%{_bindir}/osgforest
%{_bindir}/osgfpdepth
%{_bindir}/osgframerenderer
%{_bindir}/osgfxbrowser
%{_bindir}/osggameoflife
%{_bindir}/osggeometry
%{_bindir}/osggeometryshaders
%{_bindir}/osggpucull
%{_bindir}/osggpx
%{_bindir}/osggraphicscost
%{_bindir}/osghangglide
%{_bindir}/osghud
%{_bindir}/osgimagesequence
%{_bindir}/osgimpostor
%{_bindir}/osgintersection
%{_bindir}/osgkdtree
%{_bindir}/osgkeyboard
%{_bindir}/osgkeyboardmouse
%{_bindir}/osgkeystone
%{_bindir}/osglauncher
%{_bindir}/osglight
%{_bindir}/osglightpoint
%{_bindir}/osglogicop
%{_bindir}/osglogo
%{_bindir}/osgmanipulator
%{_bindir}/osgmemorytest
%{_bindir}/osgmotionblur
%{_bindir}/osgmovie
%{_bindir}/osgmultiplemovies
%{_bindir}/osgmultiplerendertargets
%{_bindir}/osgmultitexture
%{_bindir}/osgmultitexturecontrol
%{_bindir}/osgmultitouch
%{_bindir}/osgmultiviewpaging
%{_bindir}/osgobjectcache
%{_bindir}/osgoccluder
%{_bindir}/osgocclusionquery
%{_bindir}/osgoit
%{_bindir}/osgoscdevice
%{_bindir}/osgoutline
%{_bindir}/osgpackeddepthstencil
%{_bindir}/osgpagedlod
%{_bindir}/osgparametric
%{_bindir}/osgparticle
%{_bindir}/osgparticleeffects
%{_bindir}/osgparticleshader
%{_bindir}/osgpdf
%{_bindir}/osgphotoalbum
%{_bindir}/osgpick
%{_bindir}/osgplanets
%{_bindir}/osgpoints
%{_bindir}/osgpointsprite
%{_bindir}/osgposter
%{_bindir}/osgprecipitation
%{_bindir}/osgprerender
%{_bindir}/osgprerendercubemap
%{_bindir}/osgreflect
%{_bindir}/osgrobot
%{_bindir}/osgSSBO
%{_bindir}/osgsampler
%{_bindir}/osgscalarbar
%{_bindir}/osgscreencapture
%{_bindir}/osgscribe
%{_bindir}/osgsequence
%{_bindir}/osgshadercomposition
%{_bindir}/osgshadergen
%{_bindir}/osgshadermultiviewport
%{_bindir}/osgshaderpipeline
%{_bindir}/osgshaders
%{_bindir}/osgshaderterrain
%{_bindir}/osgshadow
%{_bindir}/osgshape
%{_bindir}/osgsharedarray
%{_bindir}/osgsidebyside
%{_bindir}/osgsimpleshaders
%{_bindir}/osgsimplegl3
%{_bindir}/osgsimpleMDI
%{_bindir}/osgsimplifier
%{_bindir}/osgsimulation
%{_bindir}/osgslice
%{_bindir}/osgspacewarp
%{_bindir}/osgspheresegment
%{_bindir}/osgspotlight
%{_bindir}/osgstereoimage
%{_bindir}/osgstereomatch
%{_bindir}/osgteapot
%{_bindir}/osgterrain
%{_bindir}/osgtessellate
%{_bindir}/osgtessellationshaders
%{_bindir}/osgtext
%{_bindir}/osgtext3D
%{_bindir}/osgtexture1D
%{_bindir}/osgtexture2D
%{_bindir}/osgtexture3D
%{_bindir}/osgtexture2DArray
%{_bindir}/osgtexturecompression
%{_bindir}/osgtexturerectangle
%{_bindir}/osgthirdpersonview
%{_bindir}/osgthreadedterrain
%{_bindir}/osgtransferfunction
%{_bindir}/osgtransformfeedback
%{_bindir}/osguniformbuffer
%{_bindir}/osgunittests
%{_bindir}/osguserdata
%{_bindir}/osguserstats
%{_bindir}/osgvertexattributes
%{_bindir}/osgvertexprogram
%{?with_wxWidgets:%{_bindir}/osgviewerWX}
%{_bindir}/osgvirtualprogram
%{_bindir}/osgvnc
%{_bindir}/osgvolume
%{_bindir}/osgwidgetaddremove
%{_bindir}/osgwidgetbox
%{_bindir}/osgwidgetcanvas
%{_bindir}/osgwidgetframe
%{_bindir}/osgwidgetinput
%{_bindir}/osgwidgetlabel
%{_bindir}/osgwidgetmenu
%{_bindir}/osgwidgetmessagebox
%{_bindir}/osgwidgetnotebook
%{_bindir}/osgwidgetperformance
%{_bindir}/osgwidgetscrolled
%{_bindir}/osgwidgetshader
%{_bindir}/osgwidgetstyled
%{_bindir}/osgwidgettable
%{_bindir}/osgwidgetwindow
%{_bindir}/osgwindows
%{_datadir}/OpenSceneGraph

%files examples-SDL
%{_bindir}/osgviewerSDL

%files examples-fltk
%{_bindir}/osgviewerFLTK

%files examples-gtk
%{_bindir}/osgviewerGTK

%files -n OpenThreads
%doc AUTHORS.txt NEWS.txt README.md
%license LICENSE.txt
%{_libdir}/libOpenThreads.so.*

%files -n OpenThreads-devel
%doc %{_vpath_builddir}/doc/OpenThreadsReferenceDocs
%{_libdir}/pkgconfig/openthreads.pc
%{_libdir}/libOpenThreads.so
%{_includedir}/OpenThreads

%if %{with mingw}
%files -n mingw32-%{name}
%license LICENSE.txt
%{mingw32_bindir}/libOpenThreads.dll
%{mingw32_bindir}/libosg*.dll
%dir %{mingw32_bindir}/osgPlugins-%{version}/
%{mingw32_bindir}/osgPlugins-%{version}/*.dll
%{mingw32_libdir}/libOpenThreads.dll.a
%{mingw32_libdir}/libosg*.dll.a
%{mingw32_libdir}/pkgconfig/openscenegraph*.pc
%{mingw32_libdir}/pkgconfig/openthreads.pc
%{mingw32_includedir}/OpenThreads/
%{mingw32_includedir}/osg*/

%files -n mingw32-%{name}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{name}
%license LICENSE.txt
%{mingw64_bindir}/libOpenThreads.dll
%{mingw64_bindir}/libosg*.dll
%dir %{mingw64_bindir}/osgPlugins-%{version}/
%{mingw64_bindir}/osgPlugins-%{version}/*.dll
%{mingw64_libdir}/libOpenThreads.dll.a
%{mingw64_libdir}/libosg*.dll.a
%{mingw64_libdir}/pkgconfig/openscenegraph*.pc
%{mingw64_libdir}/pkgconfig/openthreads.pc
%{mingw64_includedir}/OpenThreads/
%{mingw64_includedir}/osg*/

%files -n mingw64-%{name}-tools
%{mingw64_bindir}/*.exe
%endif

%changelog
%autochangelog
