%global source0_hash ea2ed52b085989fe38d0e7f9080da4104d4707d60d8d3b5f5a478b9bec325a3c

%{?mingw_package_header}

%global qt_module qtlocation
#global pre beta

#global commit f28408346243cf090326f4738fd838219c21e00f
#global shortcommit %(c=%{commit}; echo ${c:0:7})

%if 0%{?commit:1}
%global source_folder %{qt_module}-%{commit}
%else
%global source_folder %{qt_module}-everywhere-src-%{version}%{?pre:-%{pre}}
%endif

# first two digits of version
%define release_version %(echo %{version} | awk -F. '{print $1"."$2}')

Name:           mingw-qt5-%{qt_module}
Version:        5.15.18
Release:        2%{?dist}
Summary:        Qt5 for Windows - QtLocation component

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        (LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0) AND ISC AND BSL-1.0 AND MIT
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif
# Fix int32_t not declared
Patch0:         qtlocation_cstdint.patch
# Fix rapidjson build
Patch1:         qtlocation-fix-rapidjson-build.patch

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-angleproject
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-angleproject
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtLocation component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtLocation component

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{source_folder}
%if 0%{?commit:1}
# Make sure the syncqt tool is run when using a git snapshot
mkdir .git
%endif

%build
%mingw_qmake_qt5 ../%{qt_module}.pro
%mingw_make_build

%install
%mingw_make install INSTALL_ROOT=%{buildroot}

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Location.dll
%{mingw32_bindir}/Qt5Positioning.dll
%{mingw32_bindir}/Qt5PositioningQuick.dll
%{mingw32_includedir}/qt5/QtLocation/
%{mingw32_includedir}/qt5/QtPositioning/
%{mingw32_includedir}/qt5/QtPositioningQuick/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Location.dll.a
%{mingw32_libdir}/libQt5Positioning.dll.a
%{mingw32_libdir}/libQt5PositioningQuick.dll.a
%{mingw32_libdir}/cmake/Qt5Location/
%{mingw32_libdir}/cmake/Qt5Positioning/
%{mingw32_libdir}/cmake/Qt5PositioningQuick/
%{mingw32_libdir}/pkgconfig/Qt5Location.pc
%{mingw32_libdir}/pkgconfig/Qt5Positioning.pc
%{mingw32_libdir}/pkgconfig/Qt5PositioningQuick.pc
%{mingw32_libdir}/qt5/plugins/geoservices/
%{mingw32_libdir}/qt5/plugins/position/
%{mingw32_libdir}/qt5/qml/QtLocation/
%{mingw32_libdir}/qt5/qml/QtPositioning/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_location.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_location_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_positioning.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_positioningquick_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Location.dll
%{mingw64_bindir}/Qt5Positioning.dll
%{mingw64_bindir}/Qt5PositioningQuick.dll
%{mingw64_includedir}/qt5/QtLocation/
%{mingw64_includedir}/qt5/QtPositioning/
%{mingw64_includedir}/qt5/QtPositioningQuick/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Location.dll.a
%{mingw64_libdir}/libQt5Positioning.dll.a
%{mingw64_libdir}/libQt5PositioningQuick.dll.a
%{mingw64_libdir}/cmake/Qt5Location/
%{mingw64_libdir}/cmake/Qt5Positioning/
%{mingw64_libdir}/cmake/Qt5PositioningQuick/
%{mingw64_libdir}/pkgconfig/Qt5Location.pc
%{mingw64_libdir}/pkgconfig/Qt5Positioning.pc
%{mingw64_libdir}/pkgconfig/Qt5PositioningQuick.pc
%{mingw64_libdir}/qt5/plugins/geoservices/
%{mingw64_libdir}/qt5/plugins/position/
%{mingw64_libdir}/qt5/qml/QtLocation/
%{mingw64_libdir}/qt5/qml/QtPositioning/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_location.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_location_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_positioning.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_positioning_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_positioningquick.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_positioningquick_private.pri

%changelog
%autochangelog
