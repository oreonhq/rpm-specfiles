%global source0_hash none

#global commit 2cee656cab3867e243483ec75e519012f14949be
#global shortcommit %(c=%{commit}; echo ${c:0:7})

Name: qmapshack
Version: 1.17.1
Release: 21%{?dist}
Summary: GPS mapping and management tool

# src/animation = WTFPL
License: GPL-2.0-or-later AND GPL-3.0-or-later AND WTFPL
URL: https://github.com/Maproom/qmapshack/wiki
%if 0%{?commit:1}
Source0: https://github.com/Maproom/qmapshack/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
%else
Source0: https://github.com/Maproom/qmapshack/archive/V_%{version}/%{name}-%{version}.tar.gz
%endif

Recommends: routino
Recommends: qmaptool

BuildRequires: gcc-c++
%if 0%{?rhel}
BuildRequires: cmake3
%else
BuildRequires: cmake
%endif
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Xml)
BuildRequires: cmake(Qt5Script)
BuildRequires: cmake(Qt5Sql)
BuildRequires: cmake(Qt5WebEngineWidgets)
BuildRequires: cmake(Qt5UiTools)
BuildRequires: cmake(Qt5Help)
BuildRequires: cmake(proj)
BuildRequires: cmake(QuaZip-Qt5)
BuildRequires: pkgconfig(gdal)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: routino-devel
BuildRequires: alglib-devel
BuildRequires: desktop-file-utils

# because new dependency on WebEngine
ExclusiveArch: %{qt5_qtwebengine_arches}

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

%files
%license LICENSE
%doc changelog.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/QMapShack.*
%{_datadir}/pixmaps/QMapShack.png
%{_datadir}/%{name}/
%{_datadir}/doc/HTML/QMSHelp.q??
%{_mandir}/man1/%{name}.*

%files -n qmaptool
%{_bindir}/qmaptool
%{_bindir}/qmt_*
%{_datadir}/applications/qmaptool.desktop
%{_datadir}/icons/hicolor/*/apps/QMapTool.*
%{_datadir}/pixmaps/QMapTool.png
%{_datadir}/qmaptool/
%{_datadir}/qmt_*/
%{_datadir}/doc/HTML/QMTHelp.q??
%{_mandir}/man1/qmaptool.*
%{_mandir}/man1/qmt_*.*

%changelog
%autochangelog
