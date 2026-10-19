%global source0_hash fa8b901651017b20a38996bbab2d205d244328ed11778b53224282e9884e6c91
%global         forgeurl0 https://gitlab.com/OpenMW/openmw
%global         forgeurl1 https://github.com/bulletphysics/bullet3/
%global         forgeurl2 https://github.com/OpenMW/osg/
%global         forgeurl3 https://github.com/recastnavigation/recastnavigation/
ExclusiveArch: %{x86_64} %{arm64}
Name:           openmw
Version:        0.50.0
Release:        1%{?dist}
Summary:        OpenMW is an open-source game engine
%global         tag0 %{name}-%{version}
%global         tag1 3.25
%global         commit2 43faf6fa88bd236e0911a5340bfbcbc25b3a98d9
%global         commit3 c393777d26d2ff6519ac23612abf8af42678c9dd
%forgemeta -a
License:        %{shrink:
                GPL-3.0-only AND 
                (Zlib AND MIT AND BSD-3-clause AND BSL-1.0 AND NTP) AND
                (GPL-2.0-only AND LGPL-2.0-or-later WITH WxWindows-exception-3.1) AND 
                MIT AND 
                OFL-1.1-RFN}
URL:            https://openmw.org/
Source0:        %{forgeurl0}/-/archive/%{tag0}/%{name}-%{tag0}.tar.bz2
Source1:        %{forgesource1}
Source2:        %{forgesource2}
Source3:        %{forgesource3}
Patch0:         csxcb.patch
Requires:       dejavu-lgc-sans-mono-fonts
Provides:       bundled(bullet) = 3.25
Provides:       bundled(OpenSceneGraph-OpenMW) = 3.6
Provides:       bundled(recastnavigation) = 1.6
Provides:       bundled(sol3)
Provides:       bundled(fonts(MysticCards))
Provides:       bundled(fonts(DemonicLetters))
# oreon:deps
BuildRequires:  asio-devel
BuildRequires:  boost-devel
BuildRequires:  boost-filesystem
BuildRequires:  boost-iostreams
BuildRequires:  boost-program-options
BuildRequires:  boost-thread
BuildRequires:  cmake
BuildRequires:  cmake(SDL2)
BuildRequires:  collada-dom-devel
BuildRequires:  dejavu-lgc-sans-mono-fonts
BuildRequires:  desktop-file-utils
BuildRequires:  ffmpeg-free-devel
BuildRequires:  fltk-devel
BuildRequires:  freeglut-devel
BuildRequires:  gcc
BuildRequires:  giflib-devel
BuildRequires:  gmock-devel
BuildRequires:  gtest-devel
BuildRequires:  libGL-devel
BuildRequires:  libGLU-devel
BuildRequires:  libICE-devel
BuildRequires:  libX11-devel
BuildRequires:  libXmu-devel
BuildRequires:  libXt-devel
BuildRequires:  libavcodec-free-devel
BuildRequires:  libcurl-devel
BuildRequires:  libglvnd-devel
BuildRequires:  libjpeg-devel
BuildRequires:  liblas-devel
BuildRequires:  libpng-devel
BuildRequires:  libstdc++-devel
BuildRequires:  libtiff-devel
BuildRequires:  libvncserver-devel
BuildRequires:  libxml2-devel
BuildRequires:  lua-devel
BuildRequires:  luajit-devel
BuildRequires:  lz4-devel
BuildRequires:  mygui-devel
BuildRequires:  ninja-build
BuildRequires:  openal-soft-devel
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gta)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtkglext-x11-1.0)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(poppler-glib)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  qt-x11
BuildRequires:  qt6-linguist
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  sqlite-devel
BuildRequires:  tinyxml-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  unshield-devel
BuildRequires:  yaml-cpp-devel
# /oreon:deps
%description
OpenMW is an open-source game engine focused on 3D role-playing games

%package        cs
Summary:        The OpenMW Construction Set
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    cs
OpenMW-CS is a construction kit for making games in the OpenMW engine

%package        tools
Summary:        Utility programs for OpenMW.
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    tools
Various utility tools for developing and debugging with OpenMW

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# Unpack the main source archive and the secondary sources
# into separate directories in %%{_builddir}.
# Then, switch into the unpacked Source0 directory.
%setup -q %{forgesetupargs0} -b1 -b2 -b3
%autopatch -p1

%conf
# Prepare the cmake
# Minimum CMake version is now 3.5, and bullet builds with this.
export CMAKE_POLICY_VERSION_MINIMUM=3.5
# topdir<number> is set for each source by %%forgemeta.
%cmake -G Ninja \
    -DBUILD_OPENMW_TESTS:BOOL=ON \
    -DBULLET_STATIC:BOOL=ON \
    -DFETCHCONTENT_FULLY_DISCONNECTED:BOOL=ON \
    -DFETCHCONTENT_SOURCE_DIR_BULLET:PATH=%{_builddir}/%{topdir1} \
    -DFETCHCONTENT_SOURCE_DIR_OSG:PATH:PATH=%{_builddir}/%{topdir2} \
    -DFETCHCONTENT_SOURCE_DIR_RECASTNAVIGATION:PATH=%{_builddir}/%{topdir3} \
    -DGLOBAL_DATA_PATH:PATH=%{_datadir} \
    -DOPENMW_USE_SYSTEM_BULLET:BOOL=OFF \
    -DOPENMW_USE_SYSTEM_GOOGLETEST:BOOL=ON \
    -DOPENMW_USE_SYSTEM_OSG:BOOL=OFF \
    -DOSG_STATIC:BOOL=ON

%build

%cmake_build
%install
%cmake_install
rm %{buildroot}%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf
ln -sr %{buildroot}%{_datadir}/fonts/dejavu-lgc-sans-mono-fonts/DejaVuLGCSansMono.ttf %{buildroot}%{_datadir}/openmw/resources/vfs/fonts/DejaVuLGCSansMono.ttf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/org.openmw.launcher.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.openmw.cs.desktop
./%{_vpath_builddir}/openmw-tests
%files -f %{oreon_filedir}/main.list
%files -n openmw-cs -f %{oreon_filedir}/openmw-cs.list
%files -n openmw-tools -f %{oreon_filedir}/openmw-tools.list

%changelog

%autochangelog
