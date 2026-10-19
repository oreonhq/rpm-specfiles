%global source0_hash 3564bd1601b1b170dc894c7e66a2e5c61849b3fb8612e944c84fd97115cce248
Name:           tiled
Summary:        Tiled Map Editor
Version:        1.12.2
Release:        1%{?dist}
License:        GPL-2.0-or-later AND BSD-2-Clause AND CC-BY-SA-3.0 AND GPL-3.0-or-later AND CC0-1.0
URL:            https://www.mapeditor.org
Source0:        https://github.com/mapeditor/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libappstream-glib
BuildRequires:  libzstd-devel
BuildRequires:  make
BuildRequires:  pkgconfig(Qt6Core)
BuildRequires:  python3-devel
BuildRequires:  qbs
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  qt6-qtsvg-devel
BuildRequires:  qt6-qttools-devel
BuildRequires:  zlib-devel
# /oreon:deps
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
find -name ".uic" -or -name ".moc" -or -name ".rcc" -delete
%find_lang %{name} --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/org.mapeditor.Tiled.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/metainfo/org.mapeditor.Tiled.appdata.xml
%ldconfig_scriptlets
%files -f %{oreon_filedir}/main.list
%files -n tiled-devel -f %{oreon_filedir}/tiled-devel.list
%files -n tiled-plugin-python -f %{oreon_filedir}/tiled-plugin-python.list
%files -n tiled-plugin-rpmap -f %{oreon_filedir}/tiled-plugin-rpmap.list
%files -n tiled-plugin-tbin -f %{oreon_filedir}/tiled-plugin-tbin.list
%files -n tiled-plugin-droidcraft -f %{oreon_filedir}/tiled-plugin-droidcraft.list
%files -n tiled-plugin-flare -f %{oreon_filedir}/tiled-plugin-flare.list
%files -n tiled-plugin-replica-island -f %{oreon_filedir}/tiled-plugin-replica-island.list
%files -n tiled-plugin-t-engine4 -f %{oreon_filedir}/tiled-plugin-t-engine4.list
%files -n tiled-plugin-defold -f %{oreon_filedir}/tiled-plugin-defold.list
%files -n tiled-plugin-gmx -f %{oreon_filedir}/tiled-plugin-gmx.list
%files -n tiled-plugin-yy -f %{oreon_filedir}/tiled-plugin-yy.list
%files -n tiled-plugin-tscn -f %{oreon_filedir}/tiled-plugin-tscn.list
%files -n tiled-plugin-rpd -f %{oreon_filedir}/tiled-plugin-rpd.list

%changelog

%autochangelog
