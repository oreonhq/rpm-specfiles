%global source0_hash 405116b4c5eded981484c4c154eb392d44b69b587342f1193181175e309f2c00

%{?mingw_package_header}

%global qt_module qtcharts
#global pre rc

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

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
Summary:        Qt6 for Windows - QtCharts component

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
Summary:        Qt6 for Windows - QtCharts component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtCharts component

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
%{mingw32_bindir}/Qt6Charts.dll
%{mingw32_bindir}/Qt6ChartsQml.dll
%{mingw32_includedir}/qt6/QtCharts/
%{mingw32_includedir}/qt6/QtChartsQml/
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Charts/
%{mingw32_libdir}/cmake/Qt6ChartsPrivate/
%{mingw32_libdir}/cmake/Qt6ChartsQml/
%{mingw32_libdir}/cmake/Qt6ChartsQmlPrivate/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml*
%{mingw32_libdir}/pkgconfig/Qt6Charts.pc
%{mingw32_libdir}/pkgconfig/Qt6ChartsQml.pc
%{mingw32_libdir}/libQt6Charts.dll.a
%{mingw32_libdir}/libQt6ChartsQml.dll.a
%{mingw32_libdir}/Qt6Charts.prl
%{mingw32_libdir}/Qt6ChartsQml.prl
%{mingw32_libdir}/qt6/metatypes/qt6charts_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6chartsqml_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_charts.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_charts_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_chartsqml.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_chartsqml_private.pri
%{mingw32_libdir}/qt6/qml/QtCharts/
%{mingw32_libdir}/qt6/modules/Charts.json
%{mingw32_libdir}/qt6/modules/ChartsQml.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Charts.dll
%{mingw64_bindir}/Qt6ChartsQml.dll
%{mingw64_includedir}/qt6/QtCharts/
%{mingw64_includedir}/qt6/QtChartsQml/
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtChartsTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Charts/
%{mingw64_libdir}/cmake/Qt6ChartsPrivate/
%{mingw64_libdir}/cmake/Qt6ChartsQml/
%{mingw64_libdir}/cmake/Qt6ChartsQmlPrivate/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/Qt6qtchartsqml*
%{mingw64_libdir}/pkgconfig/Qt6Charts.pc
%{mingw64_libdir}/pkgconfig/Qt6ChartsQml.pc
%{mingw64_libdir}/libQt6Charts.dll.a
%{mingw64_libdir}/libQt6ChartsQml.dll.a
%{mingw64_libdir}/Qt6Charts.prl
%{mingw64_libdir}/Qt6ChartsQml.prl
%{mingw64_libdir}/qt6/metatypes/qt6charts_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6chartsqml_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_charts.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_charts_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_chartsqml.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_chartsqml_private.pri
%{mingw64_libdir}/qt6/qml/QtCharts/
%{mingw64_libdir}/qt6/modules/Charts.json
%{mingw64_libdir}/qt6/modules/ChartsQml.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

%changelog
%autochangelog
