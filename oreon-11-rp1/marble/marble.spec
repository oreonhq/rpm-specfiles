Name:    marble
Summary: Virtual globe and world atlas
Epoch:   1
Version: 25.12.3
Release: 1%{?dist}

License: Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1)
URL:     http://edu.kde.org/marble/
Source0:  http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches

BuildRequires: desktop-file-utils
BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Xml)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6SvgWidgets)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6PrintSupport)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6Test)
%ifarch %{?qt6_qtwebengine_arches}
BuildRequires: cmake(Qt6WebChannel)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6WebEngineQuick)
%endif
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6SerialPort)
BuildRequires: cmake(Qt6LinguistTools)
#BuildRequires: cmake(Qt6Designer)

BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6Parts)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Runner)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(Plasma)

BuildRequires: cmake(absl)
%if 0%{?fedora} && ! 0%{?flatpak}
BuildRequires: pkgconfig(libgps)
%endif
BuildRequires: pkgconfig(protobuf)
BuildRequires: pkgconfig(shapelib)
BuildRequires: pkgconfig(shared-mime-info)
BuildRequires: zlib-devel

Requires: %{name}-widget-qt6%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: (%{name}-plasma%{?_isa} = %{epoch}:%{version}-%{release} if plasmashell)

# filter plugin provides
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$

%description
Marble is a Virtual Globe and World Atlas that you can use to learn more
about Earth: You can pan and zoom around and you can look up places and
roads. A mouse click on a place label will provide the respective Wikipedia
article.

Of course it's also possible to measure distances between locations or watch
the current cloud cover. Marble offers different thematic maps: A classroom-
style topographic map, a satellite view, street map, earth at night and
temperature and precipitation maps. All maps include a custom map key, so it
can also be used as an educational tool for use in class-rooms. For
educational purposes you can also change date and time and watch how the
starry sky and the twilight zone on the map change.

In opposite to other virtual globes Marble also features multiple
projections: Choose between a Flat Map ("Plate carré"), Mercator or the Globe.

%package plasma
Summary: Marble Plasma applets
Requires: %{name}-widget-qt6%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description plasma
%{summary}.

%package qt
Summary: Marble qt-only interface
Requires: %{name}-widget-qt6%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description qt
%{summary}.

%package common
Summary:  Common files of %{name}
BuildArch: noarch
%if ! 0%{?mobile}
Obsoletes: marble-mobile < %{epoch}:%{version}-%{release}
%endif
%if ! 0%{?touch}
Obsoletes: marble-touch < %{epoch}:%{version}-%{release}
%endif
%description common
{summary}.

%package astro
Summary: Marble Astro Library
Requires: %{name}-common = %{epoch}:%{version}-%{release}
%description astro
%{summary}.

%package astro-devel
Summary: Development files for Marble Astro Library
Requires: %{name}-astro%{?_isa} = %{epoch}:%{version}-%{release}
%description astro-devel
%{summary}.

%package widget-data
Summary: Marble Widget data
Requires: %{name}-common = %{epoch}:%{version}-%{release}
BuildArch: noarch
%description widget-data
%{summary}.

%package widget-qt6
Summary: Marble Widget Library
Requires: %{name}-astro%{?_isa} = %{epoch}:%{version}-%{release}
Requires: %{name}-widget-data = %{epoch}:%{version}-%{release}
Obsoletes: %{name}-widget-qt5 < %{epoch}:%{version}-%{release}
Conflicts: %{name}-widget-qt5 < %{epoch}:%{version}-%{release}
%description widget-qt6
%{summary}.

%package widget-qt6-devel
Summary: Development files for Qt6 Marble Widget
Requires: %{name}-widget-qt6%{?_isa} = %{epoch}:%{version}-%{release}
Requires: cmake(Qt6Core5Compat)
Requires: cmake(Qt6Xml)
Requires: cmake(Qt6Widgets)
%ifarch %{?qt6_qtwebengine_arches}
Requires: cmake(Qt6WebEngineWidgets)
%endif
Obsoletes: %{name}-widget-qt5-devel < %{epoch}:%{version}-%{release}
Conflicts: %{name}-widget-qt5-devel < %{epoch}:%{version}-%{release}
%description widget-qt6-devel
%{summary}.


%prep
%autosetup -p1
# https://invent.kde.org/education/marble/-/merge_requests/143
sed -i -e '/^Exec=/s/Behaim/behaim/' src/apps/behaim/org.kde.marble.behaim.desktop

mv src/3rdparty/zlib src/3rdparty/zlib.UNUSED ||:


%build
%cmake_kf6 \
  -Wno-dev \
  -DBUILD_MARBLE_TESTS:BOOL=OFF \
  -DBUILD_QT_AND_KDE:BOOL=ON \
  -DMARBLE_DATA_PATH:PATH="%{_datadir}/marble/data" \
  -DMARBLE_PRI_INSTALL_DIR:PATH="%{_qt6_archdatadir}/mkspecs/modules" \
  -DWITH_DESIGNER_PLUGIN:BOOL=OFF \
  -DBUILD_MARBLE_TOOLS=ON

%cmake_build


%install
%cmake_install

%find_lang %{name} --all-name --with-html
# hack around buggy --with-qt ^^
%find_lang_kf6 marble_qt
cat marble_qt.lang >> %{name}.lang


%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.behaim.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.maps.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble-qt.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/{marble_geojson,marble_gpx,marble_kml,marble_kmz,marble_shp}.desktop

%files
%{_bindir}/marble
%{_bindir}/marble-behaim
%{_bindir}/marble-maps
%{_datadir}/kxmlgui5/marble/
%{_kf6_metainfodir}/org.kde.marble.appdata.xml
%{_kf6_metainfodir}/org.kde.marble.behaim.appdata.xml
%{_kf6_metainfodir}/org.kde.marble.maps.appdata.xml
%{_datadir}/applications/org.kde.marble.desktop
%{_datadir}/applications/org.kde.marble.behaim.desktop
%{_datadir}/applications/org.kde.marble.maps.desktop
%{_datadir}/applications/marble_geojson.desktop
%{_datadir}/applications/marble_gpx.desktop
%{_datadir}/applications/marble_kml.desktop
%{_datadir}/applications/marble_kmz.desktop
%{_datadir}/applications/marble_shp.desktop
%{_datadir}/config.kcfg/marble.kcfg
%{_datadir}/qlogging-categories6/marble.categories
%{_kf6_plugindir}/thumbcreator/marble_thumbnail_*.so

%files common -f %{name}.lang
%license LICENSE.txt
%doc CREDITS MANIFESTO.txt USECASES
%{_datadir}/icons/hicolor/*/apps/marble.*
%{_datadir}/icons/hicolor/*/apps/org.kde.marble.*
%{_datadir}/mime/packages/geo.xml
%dir %{_datadir}/marble/

%files plasma
%{_kf6_plugindir}/krunner/plasma_runner_marble.so
%{_datadir}/plasma/plasmoids/org.kde.plasma.worldclock/
%{_datadir}/plasma/wallpapers/org.kde.plasma.worldmap/

%files qt
%{_bindir}/marble-qt
%{_datadir}/applications/org.kde.marble-qt.desktop

%files astro
%{_libdir}/libastro.so.*

%files astro-devel
%{_includedir}/astro/
%{_libdir}/libastro.so
%dir %{_libdir}/cmake/
%{_libdir}/cmake/Astro/

%files widget-data
%{_datadir}/marble/data/

%files widget-qt6
%{_libdir}/libmarblewidget-qt6.so.*
%dir %{_libdir}/marble
%{_libdir}/marble/plugins/
# include part here too
%{_qt6_plugindir}/libmarble_part.so
%{_kf6_qmldir}/org/kde/marble/

%files widget-qt6-devel
%{_includedir}/marble/
%{_libdir}/libmarblewidget-qt6.so
%dir %{_libdir}/cmake/
%{_libdir}/cmake/Marble/
%{_qt6_archdatadir}/mkspecs/modules/qt_Marble.pri


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
