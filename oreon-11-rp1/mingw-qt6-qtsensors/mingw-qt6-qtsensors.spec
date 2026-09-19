%global source0_hash 91e6515b7cebbfae3696861933f5359cc303dfe82f7849cf5a10df378c8ef581

%{?mingw_package_header}

%global qt_module qtsensors
#global pre rc

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %%(c=%%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{qt_version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define qt_version %(echo %{version} | cut -d~ -f1)

Name:           mingw-qt6-%{qt_module}
Version:        6.10.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - QtSensors component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{qt_version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{qt_version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt6-qtbase = %{version}
BuildRequires:  mingw32-qt6-qtdeclarative = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSensors component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSensors component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -GNinja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Sensors.dll
%{mingw32_bindir}/Qt6SensorsQuick.dll
%{mingw32_includedir}/qt6/QtSensors/
%{mingw32_includedir}/qt6/QtSensorsQuick/
%{mingw32_libdir}/cmake/Qt6/FindSensorfw.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Sensors/
%{mingw32_libdir}/cmake/Qt6SensorsPrivate/
%{mingw32_libdir}/cmake/Qt6SensorsQuick/
%{mingw32_libdir}/cmake/Qt6SensorsQuickPrivate/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6SensorsQuickplugin*
%{mingw32_libdir}/pkgconfig/Qt6Sensors.pc
%{mingw32_libdir}/pkgconfig/Qt6SensorsQuick.pc
%{mingw32_libdir}/libQt6Sensors.dll.a
%{mingw32_libdir}/libQt6SensorsQuick.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6sensors_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6sensorsquick_metatypes.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw32_libdir}/Qt6Sensors.prl
%{mingw32_libdir}/Qt6SensorsQuick.prl
%dir %{mingw32_libdir}/qt6/plugins/sensors/
%{mingw32_libdir}/qt6/plugins/sensors/qtsensors_generic.dll
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensors.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensors_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick_private.pri
%{mingw32_libdir}/qt6/qml/QtSensors/
%{mingw32_libdir}/qt6/modules/Sensors.json
%{mingw32_libdir}/qt6/modules/SensorsQuick.json

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Sensors.dll
%{mingw64_bindir}/Qt6SensorsQuick.dll
%{mingw64_includedir}/qt6/QtSensors/
%{mingw64_includedir}/qt6/QtSensorsQuick/
%{mingw64_libdir}/cmake/Qt6/FindSensorfw.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSensorsTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Sensors/
%{mingw64_libdir}/cmake/Qt6SensorsPrivate/
%{mingw64_libdir}/cmake/Qt6SensorsQuick/
%{mingw64_libdir}/cmake/Qt6SensorsQuickPrivate/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6SensorsQuickplugin*
%{mingw64_libdir}/pkgconfig/Qt6Sensors.pc
%{mingw64_libdir}/pkgconfig/Qt6SensorsQuick.pc
%{mingw64_libdir}/libQt6Sensors.dll.a
%{mingw64_libdir}/libQt6SensorsQuick.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6sensors_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6sensorsquick_metatypes.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw64_libdir}/Qt6Sensors.prl
%{mingw64_libdir}/Qt6SensorsQuick.prl
%dir %{mingw64_libdir}/qt6/plugins/sensors/
%{mingw64_libdir}/qt6/plugins/sensors/qtsensors_generic.dll
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensors.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensors_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_sensorsquick_private.pri
%{mingw64_libdir}/qt6/qml/QtSensors/
%{mingw64_libdir}/qt6/modules/Sensors.json
%{mingw64_libdir}/qt6/modules/SensorsQuick.json

%changelog
%autochangelog
