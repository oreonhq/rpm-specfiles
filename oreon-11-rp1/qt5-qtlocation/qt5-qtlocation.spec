%global source0_hash none

%global qt_module qtlocation

Summary: Qt5 - Location component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: (LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND ISC AND BSL-1.0 AND MIT
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtlocation
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1:   0001-Fix-appendChildNode-call.patch
Patch5:   0005-Fix-build-of-Qt.labs.location-QML-plugin.patch
Patch6:   0006-Fix-HereMap-plugin-not-supporting-authentication-via.patch

Patch100: 0100-Add-some-missing-cstdint-inclusions-872.patch
Patch101: 0101-Add-missing-include.patch
Patch102: 0102-Removed-non-compiling-assignment-operator.-Fixed-718.patch
Patch103: 0103-Explicitly-disable-copy-assignment-operator.patch
Patch104: 0104-Fix-build-with-ICU-75.patch

Patch200: 0200-Bump-mapbox-gl-native-deps.patch
Patch201: 0201-mapbox-gl-fix-smart-ptr.patch

# filter plugin/qml provides
%global __provides_exclude_from ^(%{_qt5_archdatadir}/qml/.*\\.so|%{_qt5_plugindir}/.*\\.so)$

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= 5.9.0
# QtPositioning core-private
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= 5.9.0

BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(icu-i18n)
BuildRequires: pkgconfig(libssl)
BuildRequires: pkgconfig(libcrypto)

BuildRequires: boost-devel >= 1.65.1
BuildRequires: earcut-hpp-devel >= 0.12.4
BuildRequires: geometry-hpp-devel >= 0.9.3
BuildRequires: polylabel-devel >= 1.0.3
BuildRequires: protozero-devel >= 1.5.2
BuildRequires: rapidjson-devel >= 1.1.0
BuildRequires: mapbox-variant-devel >= 1.1.4
BuildRequires: wagyu-devel >= 0.4.3

# TODO: use upstream tarballs or unbundle
# geojson-cpp: https://github.com/mapbox/geojson-cpp, ISC
# geojson-vt-cpp: https://github.com/mapbox/geojson-vt-cpp, ISC
# kdbush-hpp: https://github.com/mourner/kdbush.hpp, ISC
# shelf-pack-cpp: https://github.com/mapbox/shelf-pack-cpp, ISC
# supercluster-hpp: https://github.com/mapbox/supercluster.hpp, ISC
# unique-resource: https://github.com/okdshin/unique_resource, BSL-1.0
# vector-tile: https://github.com/mapbox/vector-tile, ISC
# nunicode: https://bitbucket.org/alekseyt/nunicode, MIT
Provides: bundled(geojson-cpp) = 0.5.1
Provides: bundled(geojson-vt-cpp) = 6.6.5
Provides: bundled(kdbush-hpp) = 0.1.3
Provides: bundled(shelf-pack-cpp) = 2.1.1
Provides: bundled(supercluster-hpp) = 0.5.0
Provides: bundled(unique-resource) = 0~gcba309e
Provides: bundled(vector-tile) = 1.0.4
Provides: bundled(nunicode) = 1.11

%description
The Qt Location and Qt Positioning APIs gives developers the ability to
determine a position by using a variety of possible sources, including
satellite, or wifi, or text file, and so on.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1
rm -rf src/3rdparty/mapbox-gl-native/deps/{boost,earcut,geometry,optional,polylabel,protozero,rapidjson,wagyu,tao_tuple,variant}

%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

# no shadow builds until fixed: https://bugreports.qt.io/browse/QTBUG-37417
%{qmake_qt5}

%make_build

%install
make install INSTALL_ROOT=%{buildroot}

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.GPL* LICENSE.LGPL*
%{_qt5_libdir}/libQt5Location.so.5*
%{_qt5_archdatadir}/qml/QtLocation/
%{_qt5_libdir}/qt5/qml/Qt/labs/location/*
%{_qt5_plugindir}/geoservices/
%{_qt5_libdir}/libQt5Positioning.so.5*
%dir %{_qt5_archdatadir}/qml/QtPositioning
%{_qt5_archdatadir}/qml/QtPositioning/*
%{_qt5_plugindir}/position/
%{_qt5_libdir}/libQt5PositioningQuick.so.5*

%files devel
%{_qt5_headerdir}/QtLocation/
%{_qt5_libdir}/libQt5Location.so
%{_qt5_libdir}/libQt5Location.prl
%{_qt5_headerdir}/QtPositioning/
%{_qt5_libdir}/libQt5Positioning.so
%{_qt5_libdir}/libQt5Positioning.prl
%{_qt5_headerdir}/QtPositioningQuick/
%{_qt5_libdir}/libQt5PositioningQuick.so
%{_qt5_libdir}/libQt5PositioningQuick.prl
%{_qt5_libdir}/pkgconfig/Qt5Location.pc
%dir %{_qt5_libdir}/cmake/Qt5Location
%{_qt5_libdir}/cmake/Qt5Location/Qt5Location*.cmake
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_location*.pri
%{_qt5_libdir}/pkgconfig/Qt5Positioning.pc
%dir %{_qt5_libdir}/cmake/Qt5Positioning
%{_qt5_libdir}/cmake/Qt5Positioning/Qt5Positioning*.cmake
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_positioning*.pri
%{_qt5_libdir}/pkgconfig/Qt5PositioningQuick.pc
%dir %{_qt5_libdir}/cmake/Qt5PositioningQuick/
%{_qt5_libdir}/cmake/Qt5PositioningQuick/Qt5PositioningQuick*.cmake
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_positioning*.pri

%files examples
%{_qt5_examplesdir}/


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
