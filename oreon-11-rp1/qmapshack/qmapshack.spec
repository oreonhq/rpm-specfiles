%global source0_hash e6e18fc22a9d14ae774f67e2fce0e5f73b2d2617b10681aa77ee88ab580f92c2
Name: qmapshack
Version: 1.21.1
Release:        1%{?dist}
Summary:        GPS mapping and management tool
License: GPL-2.0-or-later AND GPL-3.0-or-later AND WTFPL
URL: https://github.com/Maproom/qmapshack/wiki
%if 0%{?commit:1}
Source0:        https://github.com/Maproom/%{name}/archive/V_%{version}/%{name}-%{version}.tar.gz
%else
%endif
Recommends: routino
Recommends: qmaptool
ExclusiveArch: %{qt5_qtwebengine_arches}
# oreon:deps
BuildRequires:  alglib-devel
BuildRequires:  cmake
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5Help)
BuildRequires:  cmake(Qt5Script)
BuildRequires:  cmake(Qt5Sql)
BuildRequires:  cmake(Qt5UiTools)
BuildRequires:  cmake(Qt5WebEngineWidgets)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  cmake(QuaZip-Qt5)
BuildRequires:  cmake(proj)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gdal)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  routino-devel
# /oreon:deps
%description
QMapShack provides a versatile tool for GPS maps in GeoTiff format as well as
Garmin's img vector map format. You can also view and edit your GPX tracks.
QMapShack is the successor of QLandkarteGT.

Main features:
- use of several work-spaces
- use several maps on a work-space
- handle data project-oriented
- exchange data with the device by drag-n-drop

%package -n qmaptool
Summary: Create raster maps from paper map scans
Recommends: gdal
%description -n qmaptool
This is a tool to create raster maps from paper map scans. QMapTool can be
considered as a front-end to the well-known GDAL package. It complements
QMapShack.

%prep

%if 0%{?commit:1}
%autosetup -p1 -n %{name}-%{commit}
%else
%autosetup -p1 -n %{name}-V_%{version}
%endif

%build

%cmake -DBUILD_SHARED_LIBS:BOOL=OFF
%cmake_build
%install
%cmake_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/qmaptool.desktop
%oreon_autofiles qmaptool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qmaptool -f %{oreon_filedir}/qmaptool.list

%changelog

%autochangelog
