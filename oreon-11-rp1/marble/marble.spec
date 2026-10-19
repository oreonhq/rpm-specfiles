%global source0_hash a8d5fbfb6b8cc4a8517df6e75143afcdaebcd7995f88f7a459d6b17c9bae1a98
%global stable_kf6 stable
Name:    marble
Summary:        Virtual globe and world atlas
Epoch:   1
Version: 26.08.1
Release:        1%{?dist}
License: Apache-2.0 AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-only AND LGPL-2.1-or-later AND LGPL-3.0-only AND MIT AND (LGPL-2.1-only WITH Qt-LGPL-exception-1.1)
URL:     http://edu.kde.org/marble/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz
%ifarch %{?qt6_qtwebengine_arches}
%endif
Requires: %{name}-widget-qt6%{?_isa} = %{epoch}:%{version}-%{release}
Recommends: (%{name}-plasma%{?_isa} = %{epoch}:%{version}-%{release} if plasmashell)
%global __provides_exclude_from ^(%{_libdir}/marble/plugins/.*\\.so)$
# oreon:deps
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Parts)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(Phonon4Qt6)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(Qt6Concurrent)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Core5Compat)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Positioning)
BuildRequires:  cmake(Qt6PrintSupport)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6SerialPort)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6SvgWidgets)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(absl)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(protobuf)
BuildRequires:  pkgconfig(shapelib)
BuildRequires:  pkgconfig(shared-mime-info)
BuildRequires:  zlib-devel
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
     -DBUILD_MARBLE_TOOLS=ON \
     -DBUILD_DOC:BOOL=OFF
cmake --build "%{_vpath_builddir}" -j${RPM_BUILD_NCPUS}
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%find_lang_kf6 marble_qt
cat marble_qt.lang >> %{name}.lang
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.behaim.appdata.xml
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.marble.maps.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.marble-qt.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/{marble_geojson,marble_gpx,marble_kml,marble_kmz,marble_shp}.desktop
%files -f %{oreon_filedir}/main.list
%files -n marble-plasma -f %{oreon_filedir}/marble-plasma.list
%files -n marble-qt -f %{oreon_filedir}/marble-qt.list
%files -n marble-common -f %{oreon_filedir}/marble-common.list
%files -n marble-astro -f %{oreon_filedir}/marble-astro.list
%files -n marble-astro-devel -f %{oreon_filedir}/marble-astro-devel.list
%files -n marble-widget-data -f %{oreon_filedir}/marble-widget-data.list
%files -n marble-widget-qt6 -f %{oreon_filedir}/marble-widget-qt6.list
%files -n marble-widget-qt6-devel -f %{oreon_filedir}/marble-widget-qt6-devel.list

%changelog

%autochangelog
