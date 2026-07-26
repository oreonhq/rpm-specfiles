%global source0_hash f40d88ff792512af3500563b05f37b7b83591135b9413454fd308857594d89e9

%{?mingw_package_header}

%global qt_module qtsvg
#global pre rc

#global commit 45483bfae4f59ab92be22007cf49d9d7eee8a16c
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
Summary:        Qt5 for Windows - QtSvg component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif
# Backport patch for CVE-2025-10729
# https://code.qt.io/cgit/qt/qtsvg.git/diff/src/svg/qsvghandler.cpp?id=7e8898903265d931df0aa54b3913f2c49d4d7bf2
Patch0:         CVE-2025-10729.patch

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtSvg component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtSvg component

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

# .prl files aren't interesting for us

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt5Svg.dll
%{mingw32_includedir}/qt5/QtSvg/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Svg.dll.a
%{mingw32_libdir}/cmake/Qt5Svg/
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QSvg*.cmake
%{mingw32_libdir}/pkgconfig/Qt5Svg.pc
%dir %{mingw32_libdir}/qt5/plugins/iconengines/
%{mingw32_libdir}/qt5/plugins/iconengines/qsvgicon.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qsvg.dll
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_svg.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_svg_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Svg.dll
%{mingw64_includedir}/qt5/QtSvg/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Svg.dll.a
%{mingw64_libdir}/cmake/Qt5Svg/
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QSvg*.cmake
%{mingw64_libdir}/pkgconfig/Qt5Svg.pc
%dir %{mingw64_libdir}/qt5/plugins/iconengines/
%{mingw64_libdir}/qt5/plugins/iconengines/qsvgicon.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qsvg.dll
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_svg.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_svg_private.pri

%changelog
%autochangelog
