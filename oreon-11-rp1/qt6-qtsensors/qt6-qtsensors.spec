%global source0_hash none

%global qt_module qtsensors

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1

Summary: Qt6 - Sensors component
Name:    qt6-%{qt_module}
Version: 6.11.1
Release: 1%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io/
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
%else
Source0:        https://download.qt.io/official_releases/qt/%{qt_version}/submodules/qtsensors-everywhere-src-%{qt_version}.tar.xz
%endif

# filter qml/plugin provides
%global __provides_exclude_from ^(%{_qt6_archdatadir}/qml/.*\\.so|%{_qt6_plugindir}/.*\\.so)$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel >= %{version}
BuildRequires: qt6-qtsvg-devel >= %{version}

BuildRequires: pkgconfig(xkbcommon) >= 0.5.0

# provides a plugin that can use iio-sensor-proxy
Recommends: iio-sensor-proxy

%description
The Qt Sensors API provides access to sensor hardware via QML and C++
interfaces.  The Qt Sensors API also provides a motion gesture recognition
API for devices.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtsensors-devel >= %{version}
%description examples
%{summary}.
%endif

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
  -DQT_BUILD_EXAMPLES:BOOL=%{?examples:ON}%{!?examples:OFF} \
  -DQT_INSTALL_EXAMPLES_SOURCES=%{?examples:ON}%{!?examples:OFF}

%cmake_build


%install
%cmake_install

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6Sensors.so.6*
%{_qt6_libdir}/libQt6SensorsQuick.so.6*
%{_qt6_plugindir}/sensors/
%{_qt6_archdatadir}/qml/QtSensors/

%files devel
%{_qt6_headerdir}/QtSensors/
%{_qt6_headerdir}/QtSensorsQuick/
%{_qt6_libdir}/libQt6Sensors.so
%{_qt6_libdir}/libQt6Sensors.prl
%{_qt6_libdir}/libQt6SensorsQuick.prl
%{_qt6_libdir}/libQt6SensorsQuick.so
%{_qt6_libdir}/cmake/Qt6/FindSensorfw.cmake
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6Sensors/
%{_qt6_libdir}/cmake/Qt6Sensors/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6SensorsPrivate/
%{_qt6_libdir}/cmake/Qt6SensorsPrivate/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6SensorsQuick/
%{_qt6_libdir}/cmake/Qt6SensorsQuick/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6SensorsQuickPrivate/
%{_qt6_libdir}/cmake/Qt6SensorsQuickPrivate/*.cmake
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_sensors*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.11.1-1
- Import
