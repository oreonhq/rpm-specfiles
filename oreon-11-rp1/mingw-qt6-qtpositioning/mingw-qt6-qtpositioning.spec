%global source0_hash 7051fa64477c66769840cad396fc3772a01ba5516363c8842a7a513fa0c4cdce

%{?mingw_package_header}

%global qt_module qtpositioning
#global pre rc

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{qt_version}%{?pre:-%{pre}}
%endif

# first two digits of version
%global release_version %(echo %{version} | awk -F. '{print $1"."$2}')
%define qt_version %(echo %{version} | cut -d~ -f1)

Name:           mingw-qt6-%{qt_module}
Version:        6.10.2
Release:        1%{?dist}
Summary:        Qt6 for Windows - Qt Positioning component

# Base license is LGPLv3 or GPLv2
# 3rdparty/clip2tri is MIT, see ./src/3rdparty/clip2tri/LICENSE
# 3rdparty/poly2tri is BSD, see ./src/3rdparty/poly2tri/LICENSE
# 3rdparty/clipper ist Boost, see ./src/3rdparty/clipper/LICENSE
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
BuildRequires:  mingw32-qt6-qtserialport = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}
BuildRequires:  mingw64-qt6-qtdeclarative = %{version}
BuildRequires:  mingw64-qt6-qtserialport = %{version}

Provides:       bundled(clip2tri)
Provides:       bundled(poly2tri)
Provides:       bundled(clipper)

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Positioning component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - Qt Positioning component

%description -n mingw64-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 64-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}

# Postfix licenses of bundled libraries with name of library
cp -a src/3rdparty/clip2tri/LICENSE LICENSE.clip2tri
cp -a src/3rdparty/poly2tri/LICENSE LICENSE.poly2tri
cp -a src/3rdparty/clipper/LICENSE LICENSE.clipper

%build
export MINGW32_CXXFLAGS="%{mingw32_cflags} -msse2"
export MINGW64_CXXFLAGS="%{mingw64_cflags} -msse2"
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Positioning.dll
%{mingw32_bindir}/Qt6PositioningQuick.dll
%{mingw32_includedir}/qt6/QtPositioning/
%{mingw32_includedir}/qt6/QtPositioningQuick/
%{mingw32_libdir}/Qt6Positioning.prl
%{mingw32_libdir}/Qt6PositioningQuick.prl
%{mingw32_libdir}/cmake/Qt6/FindGconf.cmake
%{mingw32_libdir}/cmake/Qt6/FindGypsy.cmake
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Positioning/
%{mingw32_libdir}/cmake/Qt6PositioningPrivate/
%{mingw32_libdir}/cmake/Qt6PositioningQuick/
%{mingw32_libdir}/cmake/Qt6PositioningQuickPrivate/
%{mingw32_libdir}/cmake/Qt6Qml/QmlPlugins/
%{mingw32_libdir}/pkgconfig/Qt6Positioning.pc
%{mingw32_libdir}/pkgconfig/Qt6PositioningQuick.pc
%{mingw32_libdir}/libQt6Positioning.dll.a
%{mingw32_libdir}/libQt6PositioningQuick.dll.a
%{mingw32_libdir}/qt6/metatypes/qt6positioning_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6positioningquick_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioning.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick_private.pri
%{mingw32_libdir}/qt6/plugins/position/
%{mingw32_libdir}/qt6/modules/Positioning.json
%{mingw32_libdir}/qt6/modules/PositioningQuick.json
%{mingw32_libdir}/qt6/qml/QtPositioning/
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Positioning.dll
%{mingw64_bindir}/Qt6PositioningQuick.dll
%{mingw64_includedir}/qt6/QtPositioning/
%{mingw64_includedir}/qt6/QtPositioningQuick/
%{mingw64_libdir}/Qt6Positioning.prl
%{mingw64_libdir}/Qt6PositioningQuick.prl
%{mingw64_libdir}/cmake/Qt6/FindGconf.cmake
%{mingw64_libdir}/cmake/Qt6/FindGypsy.cmake
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtPositioningTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Positioning/
%{mingw64_libdir}/cmake/Qt6PositioningPrivate/
%{mingw64_libdir}/cmake/Qt6PositioningQuick/
%{mingw64_libdir}/cmake/Qt6PositioningQuickPrivate/
%{mingw64_libdir}/cmake/Qt6Qml/QmlPlugins/
%{mingw64_libdir}/pkgconfig/Qt6Positioning.pc
%{mingw64_libdir}/pkgconfig/Qt6PositioningQuick.pc
%{mingw64_libdir}/libQt6Positioning.dll.a
%{mingw64_libdir}/libQt6PositioningQuick.dll.a
%{mingw64_libdir}/qt6/metatypes/qt6positioning_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6positioningquick_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioning.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_positioningquick_private.pri
%{mingw64_libdir}/qt6/plugins/position/
%{mingw64_libdir}/qt6/modules/Positioning.json
%{mingw64_libdir}/qt6/modules/PositioningQuick.json
%{mingw64_libdir}/qt6/qml/QtPositioning/
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

%changelog
%autochangelog
