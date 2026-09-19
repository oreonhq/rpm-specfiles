%global source0_hash f07ff80f38caf235187200345392ca7479445ddf49a36c3694cd52a735dad6e1

%{?mingw_package_header}

%global qt_module qtsvg
#global pre rc

#global commit 45483bfae4f59ab92be22007cf49d9d7eee8a16c
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
Summary:        Qt6 for Windows - QtSvg component

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

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt6-qtbase = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSvg component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtSvg component

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
%mingw_cmake -G Ninja -DCMAKE_BUILD_TYPE=RelWithDebInfo
%mingw_ninja

%install
%mingw_ninja_install

# Win32
%files -n mingw32-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw32_bindir}/Qt6Svg.dll
%{mingw32_bindir}/Qt6SvgWidgets.dll
%{mingw32_includedir}/qt6/QtSvg/
%{mingw32_includedir}/qt6/QtSvgWidgets/
%{mingw32_libdir}/libQt6Svg.dll.a
%{mingw32_libdir}/libQt6SvgWidgets.dll.a
%{mingw32_libdir}/Qt6Svg.prl
%{mingw32_libdir}/Qt6SvgWidgets.prl
%{mingw32_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QSvgPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QSvgIconPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Svg/
%{mingw32_libdir}/cmake/Qt6SvgPrivate/
%{mingw32_libdir}/cmake/Qt6SvgWidgets/
%{mingw32_libdir}/pkgconfig/Qt6Svg.pc
%{mingw32_libdir}/pkgconfig/Qt6SvgWidgets.pc
%{mingw32_libdir}/qt6/metatypes/qt6svg_metatypes.json
%{mingw32_libdir}/qt6/metatypes/qt6svgwidgets_metatypes.json
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svg.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svg_private.pri
%{mingw32_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets.pri
%dir %{mingw32_libdir}/qt6/plugins/iconengines/
%{mingw32_libdir}/qt6/plugins/iconengines/qsvgicon.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qsvg.dll
%{mingw32_libdir}/qt6/modules/Svg.json
%{mingw32_libdir}/qt6/modules/SvgWidgets.json
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_bindir}/Qt6Svg.dll
%{mingw64_bindir}/Qt6SvgWidgets.dll
%{mingw64_includedir}/qt6/QtSvg/
%{mingw64_includedir}/qt6/QtSvgWidgets/
%{mingw64_libdir}/libQt6Svg.dll.a
%{mingw64_libdir}/libQt6SvgWidgets.dll.a
%{mingw64_libdir}/Qt6Svg.prl
%{mingw64_libdir}/Qt6SvgWidgets.prl
%{mingw64_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtSvgTestsConfig.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QSvgPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QSvgIconPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Svg/
%{mingw64_libdir}/cmake/Qt6SvgPrivate/
%{mingw64_libdir}/cmake/Qt6SvgWidgets/
%{mingw64_libdir}/pkgconfig/Qt6Svg.pc
%{mingw64_libdir}/pkgconfig/Qt6SvgWidgets.pc
%{mingw64_libdir}/qt6/metatypes/qt6svg_metatypes.json
%{mingw64_libdir}/qt6/metatypes/qt6svgwidgets_metatypes.json
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svg.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svg_private.pri
%{mingw64_libdir}/qt6/mkspecs/modules/qt_lib_svgwidgets.pri
%dir %{mingw64_libdir}/qt6/plugins/iconengines/
%{mingw64_libdir}/qt6/plugins/iconengines/qsvgicon.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qsvg.dll
%{mingw64_libdir}/qt6/modules/Svg.json
%{mingw64_libdir}/qt6/modules/SvgWidgets.json
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx

%changelog
%autochangelog
