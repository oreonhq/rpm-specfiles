%global source0_hash none

Name:           tiled
Summary:        Tiled Map Editor

Version:        1.12.0
Release:        1%{?dist}

# tiled itself is GPLv2+, libtiled and tmxviewer are BSD.
#
# Apart from the code, there are also some icons and other gfx,
# subject to various CC licenses or GPL3+. See the AUTHORS file.
License:        GPL-2.0-or-later AND BSD-2-Clause AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND CC0-1.0

URL:            https://www.mapeditor.org
Source0:        https://github.com/mapeditor/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  qbs
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  python3-devel
BuildRequires:  zlib-devel

# qbs.i386 is disabled in F39+
ExcludeArch:    %{ix86}

%description
Tiled is a general purpose tile map editor. It is built to be easy to use,
yet flexible enough to work with varying game engines, whether your game
is an RPG, platformer or Breakout clone. Tiled is free software and written
in C++, using the Qt application framework.

This package contains the tiled application and tmxviewer, a simple application
to view Tiled maps.

%package devel
Summary:        Development headers for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Development headers for the Tiled map editor.

%package plugin-python
Summary:        Python plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-python
A plugin for tiled which allows to write Python plugins.

%define pluginwarning Warning: This plugin does not offer full compatibility with Tileds features.

%package plugin-rpmap

Summary:        MapTool plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-rpmap
A plugin for tiled which allows to save maps as rpmap MapTool maps.

%{pluginwarning}

%package plugin-tbin
Summary:        tBIN plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-tbin
A plugin for tiled which allows support for the tBIN map format.

%{pluginwarning}

%package plugin-droidcraft
Summary:        Droidcraft plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-droidcraft
A plugin for tiled which allows to save maps as .dat droidcraft maps.

%{pluginwarning}

%package plugin-flare
Summary:        Flare plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-flare
A plugin for tiled which allows to save maps as .txt flare maps.

%{pluginwarning}

%package plugin-replica-island
Summary:        Replica Island plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-replica-island
A plugin for tiled which allows to save maps as .bin Replica Island maps.

%{pluginwarning}

%package plugin-t-engine4
Summary:        T-Engine4 plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-t-engine4
A plugin for tiled which allows to export maps as .lua T-Engine4 maps.

%{pluginwarning}

%package plugin-defold
Summary:        Defold plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-defold
A plugin for tiled which allows to export maps as .tilemap Defold maps.

%{pluginwarning}

%package plugin-gmx
Summary:        GameMaker Studio 1.4 plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-gmx
A plugin for tiled which allows to export maps
as GameMaker Studio 1.4 room files (.gmx).

%{pluginwarning}

%package plugin-yy
Summary:        GameMaker Studio 2.3 plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-yy
A plugin for tiled which allows to export maps
as GameMaker Studio 2.3 room files (.yy).

%{pluginwarning}

%package plugin-tscn
Summary:        Godot 4 scene plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-tscn
A plugin for tiled which allows to export maps
as Godot Engine 4 scene files (.tscn).

%{pluginwarning}

%package plugin-rpd
Summary:        Remixed Pixel Dungeon plugin for Tiled
License:        GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description plugin-rpd
A plugin for tiled which allows to export maps
as Remixed Pixel Dungeon levels (.json).

%{pluginwarning}

%prep
%autosetup -p1

# Remove copy of zlib
rm -rf src/zlib

%build
qbs setup-toolchains --detect
qbs setup-qt --detect

%global qbs_args config:release qbs.debugInformation:true qbs.installPrefix:"%{_prefix}" projects.Tiled.useRPaths:false projects.Tiled.installHeaders:true projects.Tiled.libDir:"%{_lib}"
qbs build %{qbs_args}

%install
qbs install --no-build --install-root %{buildroot} %{qbs_args}

# Clean build artefacts
find -name ".uic" -or -name ".moc" -or -name ".rcc" -delete

# locale files
%find_lang %{name} --with-qt

# Removed development file (this version does not install headers anyway)
# rm %{buildroot}/%{_libdir}/lib%{name}.so

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/org.mapeditor.Tiled.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml

%ldconfig_scriptlets

%files -f %{name}.lang
%doc AUTHORS NEWS.md README.md COPYING LICENSE.GPL LICENSE.BSD
%{_bindir}/%{name}
%{_bindir}/terraingenerator
%{_bindir}/tmxrasterizer
%{_bindir}/tmxviewer
%{_datadir}/icons/hicolor/*/apps/*%{name}*
%{_datadir}/icons/hicolor/*/mimetypes/*%{name}*
%{_datadir}/applications/org.mapeditor.Tiled.desktop
%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml
%{_datadir}/mime/packages/org.mapeditor.Tiled.xml
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/translations
%{_libdir}/lib%{name}*

%dir %{_libdir}/%{name}/
%dir %{_libdir}/%{name}/plugins/

# Core plugins
%{_libdir}/%{name}/plugins/libcsv.so
%{_libdir}/%{name}/plugins/libgmx.so
%{_libdir}/%{name}/plugins/libjson.so
%{_libdir}/%{name}/plugins/liblua.so
%{_libdir}/%{name}/plugins/libjson1.so
%{_libdir}/%{name}/plugins/libdefoldcollection.so

%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/tmxrasterizer.1*
%{_mandir}/man1/tmxviewer.1*
%dir %{_datadir}/thumbnailers
%{_datadir}/thumbnailers/%{name}.thumbnailer

%files devel
%{_includedir}/%{name}/

%files plugin-rpmap
%{_libdir}/%{name}/plugins/librpmap.so

%files plugin-python
%{_libdir}/%{name}/plugins/libpython.so

%files plugin-tbin
%{_libdir}/%{name}/plugins/libtbin.so

%files plugin-droidcraft
%{_libdir}/%{name}/plugins/libdroidcraft.so

%files plugin-flare
%{_libdir}/%{name}/plugins/libflare.so

%files plugin-replica-island
%{_libdir}/%{name}/plugins/libreplicaisland.so

%files plugin-t-engine4
%{_libdir}/%{name}/plugins/libtengine.so

%files plugin-defold
%{_libdir}/%{name}/plugins/libdefold.so

%files plugin-gmx
%{_libdir}/%{name}/plugins/libgmx.so

%files plugin-yy
%{_libdir}/%{name}/plugins/libyy.so

%files plugin-tscn
%{_libdir}/%{name}/plugins/libtscn.so

%files plugin-rpd
%{_libdir}/%{name}/plugins/librpd.so

%changelog
%autochangelog
