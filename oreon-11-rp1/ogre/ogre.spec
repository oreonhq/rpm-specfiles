%global source0_hash none

%undefine __cmake_in_source_build

Name:           ogre
Version:        1.9.0
Release:        54%{?dist}
Epoch:          1
Summary:        Object-Oriented Graphics Rendering Engine
# MIT - main library
# CC-BY-SA-3.0 - devel docs
# MIT      - shaders for DeferredShadingMedia samples
# Public Domain - CMAKE file (ignored as they are not of build result)
#               - see https://gitlab.com/fedora/legal/fedora-license-data/-/merge_requests/691 for list of files
# Zlib - Samples/Media/*/DualQuaternion*
#      - Tools/XMLConverter/src/tiny*
# BSL-1.0 - Many of the maths/spatial routines (OgreMain/include/OgreAny.h, OgreMain/include/OgrePlane.h ...)
# LicenseRef-Callaway-dante-treglia - OgreMain/include/OgreSingleton.h
#         - temporary id, see https://gitlab.com/fedora/legal/fedora-license-data/-/issues/595
# NCSA - OgreMain/include/OgreSmallVector.h
# BSD-3-Clause - OgreMain/include/OgreUTFString.h
# MIT-Khronos-old - RenderSystems/GL/include/GL/glew.h, RenderSystems/GL/include/GL/glxew.h, RenderSystems/GL/include/GL/wglew.h
# GPL-2.0-or-later WITH Bison-exception-1.24 - RenderSystems/GL/src/nvparse/*_parser.cpp
# SGI-B-2.0 - RenderSystems/GLES2/include/GLES2/gl2.h
# LGPL-2.1-only - Tools/Common/setup/License.rtf
# LGPL-2.1-or-later - files in Tools/BlenderExport/
# GPLv2-or-later - Tools/LightwaveConverter
# HPND - Tools/MaterialEditor/wxscintilla_1.69.2/src/scintilla/License.txt
# LGPL-2.0-or-later WITH WxWindows-exception-3.1 - Tools/MaterialEditor/wxscintilla_1.69.2/src/ScintillaWX.h
License:        MIT AND LicenseRef-Fedora-Public-Domain AND CC-BY-SA-3.0 AND Zlib AND BSL-1.0 AND LicenseRef-Callaway-dante-treglia AND NCSA AND BSD-3-Clause AND MIT-Khronos-old AND GPL-2.0-or-later WITH Bison-exception-1.24 AND SGI-B-2.0 AND LGPL-2.1-only AND LGPL-2.1-or-later AND GPLv2-or-later AND HPND AND LGPL-2.0-or-later WITH WxWindows-exception-3.1
URL:            http://www.ogre3d.org/
# This is modified http://downloads.sourceforge.net/ogre/ogre-v%%(echo %%{version} | tr . -).tar.bz2
# with non-free files striped (see ogre-make-clean.sh):
# Update local glew copy
# - Non-free licensed headers under RenderSystems/GL/include/GL removed
# - Non-free chiropteraDM.pk3 under Samples/Media/packs removed
# - Non-free textures under Samples/Media/materials/textures/nvidia
Source0:        %{name}-%{version}-clean.tar.bz2
Patch0:         ogre-1.7.2-rpath.patch
Patch1:         ogre-1.9.0-glew.patch
Patch3:         ogre-1.7.2-fix-ppc-build.patch
Patch5:         ogre-1.9.0-build-rcapsdump.patch
Patch6:         ogre-thread.patch
Patch7:         ogre-1.9.0-dynlib-allow-no-so.patch
# FIXME: Patch is bogus on Fedora >= 24
Patch8:         ogre-1.9.0-cmake-freetype.patch
Patch9:         ogre-1.9.0-cmake_build-fix.patch
Patch10:        ogre-aarch64.patch
Patch11:        ogre-riscv64.patch
# Resolve link errors due to incorrect template creation
# https://bitbucket.org/sinbad/ogre/commits/a24ac4afbbb9dc5ff49a61634af50da11ba8fb97/
# https://bugzilla.redhat.com/show_bug.cgi?id=1223612
Patch12:        ogre-a24ac4afbbb9dc5ff49a61634af50da11ba8fb97.diff
# Remove unnecessary inclusion of <sys/sysctl.h>
# https://bugzilla.redhat.com/show_bug.cgi?id=1841324
Patch13:        ogre-1.9.0-sysctl.patch
Patch14:        %{name}-gcc11.patch
Patch15:        %{name}-gcc16.patch
BuildRequires:  gcc-c++
BuildRequires:  zziplib-devel freetype-devel
BuildRequires:  libXaw-devel libXrandr-devel libXxf86vm-devel libGLU-devel
BuildRequires:  ois-devel freeimage-devel openexr-devel
BuildRequires:  glew-devel
BuildRequires:  boost-devel
# BuildRequires:  poco-devel
BuildRequires:  tinyxml-devel
BuildRequires:  cmake
BuildRequires:  libatomic
BuildRequires:  cppunit-devel
Provides:       bundled(wxScintilla) = 1.69.2

%description
OGRE (Object-Oriented Graphics Rendering Engine) is a scene-oriented,
flexible 3D engine written in C++ designed to make it easier and more
intuitive for developers to produce applications utilizing
hardware-accelerated 3D graphics. The class library abstracts all the
details of using the underlying system libraries like Direct3D and
OpenGL and provides an interface based on world objects and other
intuitive classes.

%package paging
Summary:        OGRE component for terrain paging
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description paging
Provides paging functionality. In essence it allows worlds to be rendered
and loaded at the same time.

%package property
Summary:        OGRE component for property introspection
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description property
OGRE's property system allows you to associate values of arbitrary type with
names, and have those values exposed via a self-describing interface.

%package rtss
Summary:        OGRE RT Shader System component
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description rtss
The Real Time Shader System, or RTSS for short, is a component of Ogre. This
component is used to generate shaders on the fly based on object material
properties, scene setup and other user definitions.

%package terrain
Summary:        OGRE component for terrain rendering
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description terrain
OGRE's terrain component provides rendering of terrain represented by
heightmaps.

%package overlay
Summary:        OGRE overlay component
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description overlay
Overlays allow you to render 2D and 3D elements on top of the normal scene
contents to create effects like heads-up displays (HUDs), menu systems,
status panels etc.

%package volume
Summary:        OGRE component for volume rendering
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description volume
This component used to render volumes. It can handle any volume data but
featurewise has a tedency towards terrains.

%package utils
Summary:        OGRE production pipeline utilities
Requires:       %{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description utils
Contains OgreXMLConverter, it can take .mesh.xml files and convert them into
their binary variant.
Also provides OgreMeshUpgrader that can load old Ogre .mesh files and upgrade
them to the latest version.

%package devel
Summary:        Ogre header files and documentation
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-paging%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-property%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-rtss%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-terrain%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-overlay%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:       %{name}-volume%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Requires:       pkgconfig
# Requires:       poco-devel
Requires:       boost-devel
Requires:       glew-devel
Requires:       cmake
Obsoletes:      %{name}-devel-doc <= %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the header files for Ogre.
Install this package if you want to develop programs that use Ogre.

%package samples
Summary:        Ogre samples executables and media
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

%description samples
This package contains the compiled (not the source) sample applications coming
with Ogre.  It also contains some media (meshes, textures,...) needed by these
samples. The samples are installed in %{_libdir}/Samples/*.so and can be run
using SampleBrowser.

%prep
%setup -q
mkdir build
%patch -P0 -p1 -b .rpath
%patch -P1 -p1 -b .glew
%patch -P3 -p1 -b .ppc
%patch -P5 -p1 -b .build-rcapsdump
%patch -P6 -p0 -b .thread
%patch -P7 -p1 -b .dynlib-allow-no-so
%if (0%{?fedora} > 20) && (0%{?fedora} < 24)
# freetype header chaos:
# Fedora <= 20    headers in /usr/include/freetype2/freetype
# Fedora 21,22,23 headers in /usr/include/freetype2
# Fedora >= 24    headers in /usr/include/freetype2/freetype
%patch -P8 -p1 -b .cmake-freetype
%endif
%patch -P9 -p1 -b .cmake_build-fix
%patch -P10 -p1
%patch -P11 -p1
%patch -P12 -p1
%patch -P13 -p1
%patch -P14 -p1
%patch -P15 -p1

# remove execute bits from src-files for -debuginfo package
chmod -x `find RenderSystems/GL -type f` \
  `find Samples/DeferredShading -type f` Samples/DynTex/src/DynTex.cpp
#  Samples/Common/bin/resources.cfg
# Remove spurious execute bits from some Media files
chmod -x `find Samples/Media/DeferredShadingMedia -type f`
# Add mit.txt symlink for links in License.html
rm -r Docs/licenses/*
ln -s ../COPYING Docs/licenses/mit.txt
# remove included tinyxml headers to ensure use of system headers
rm Tools/XMLConverter/include/tiny*

%build
%cmake -DOGRE_FULL_RPATH=0 -DCMAKE_SKIP_RPATH=1 -DOGRE_LIB_DIRECTORY=%{_lib} -DOGRE_BUILD_RTSHADERSYSTEM_EXT_SHADERS=1 -DOGRE_BUILD_PLUGIN_CG=0
%cmake_build

%install
%cmake_install

# Create config for ldconfig
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d
echo "%{_libdir}/OGRE" > %{buildroot}%{_sysconfdir}/ld.so.conf.d/%{name}-%{_arch}.conf

# Install the samples
mkdir -p %{buildroot}%{_libdir}/OGRE/Samples
mkdir -p %{buildroot}%{_sysconfdir}/OGRE
for cfg in plugins.cfg quakemap.cfg resources.cfg samples.cfg; do
  mv %{buildroot}%{_datadir}/OGRE/$cfg %{buildroot}%{_sysconfdir}/OGRE/
done

# Swap out reference to non-free quake map that was removed
cat << EOF > %{buildroot}%{_sysconfdir}/OGRE/quakemap.cfg
Archive: /usr/share/OGRE/media/packs/ogretestmap.zip 
Map: ogretestmap.bsp
EOF

# Fixing bug with wrong case for media
mkdir -p %{buildroot}%{_datadir}/OGRE/
mv %{buildroot}%{_datadir}/OGRE/Media %{buildroot}%{_datadir}/OGRE/media
mv %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/ROOM_NY.mesh %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/room_ny.mesh
mv %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/ROOM_PY.mesh %{buildroot}%{_datadir}/OGRE/media/PCZAppMedia/room_py.mesh

rm -f %{buildroot}%{_datadir}/OGRE/docs/CMakeLists.txt

# cmake macros should be in the cmake directory, not an Ogre directory
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
mv %{buildroot}%{_libdir}/OGRE/cmake/* %{buildroot}%{_datadir}/cmake/Modules

%files
%doc AUTHORS BUGS COPYING
%doc Docs/ChangeLog.html Docs/License.html Docs/licenses Docs/ReadMe.html Docs/style.css Docs/ogre-logo*.gif
%{_libdir}/libOgreMain.so.*
%{_libdir}/OGRE

%{_datadir}/OGRE
%dir %{_sysconfdir}/OGRE
%exclude %{_bindir}/SampleBrowser
%exclude %{_libdir}/OGRE/Samples
%exclude %{_libdir}/OGRE/cmake
%exclude %{_datadir}/OGRE/media
%config(noreplace) %{_sysconfdir}/ld.so.conf.d/*

%files paging
%{_libdir}/libOgrePaging.so.*

%files property
%{_libdir}/libOgreProperty.so.*

%files rtss
%{_libdir}/libOgreRTShaderSystem.so.*

%files terrain
%{_libdir}/libOgreTerrain.so.*

%files overlay
%{_libdir}/libOgreOverlay.so.*

%files volume
%{_libdir}/libOgreVolume.so.*

%files utils
%{_bindir}/OgreMeshUpgrader
%{_bindir}/OgreXMLConverter
%{_bindir}/rcapsdump

%files devel
%{_libdir}/lib*Ogre*.so
%{_datadir}/cmake/Modules/*
%{_includedir}/OGRE
%{_libdir}/pkgconfig/*.pc

%files samples
%{_bindir}/SampleBrowser
%{_libdir}/OGRE/Samples
%{_datadir}/OGRE/media
%{_sysconfdir}/OGRE/plugins.cfg
%{_sysconfdir}/OGRE/quakemap.cfg
%{_sysconfdir}/OGRE/resources.cfg
%{_sysconfdir}/OGRE/samples.cfg

%changelog
%autochangelog
