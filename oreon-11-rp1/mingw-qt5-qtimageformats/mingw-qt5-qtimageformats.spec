%global source0_hash bf86000a21a1280f7a8aaf12dd9a10e59e778169653b53c86ad8f346fb39c066

%{?mingw_package_header}

%global qt_module qtimageformats
#global pre rc

#global commit a0ec617b21d9ce0c562e8e7c0dc59bc4d08c509b
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
Release:        3%{?dist}
Summary:        Qt5 for Windows - QtImageFormats component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif
# Fix pow not declared
Patch0:         qtimageformats_math.patch

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-jasper

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-jasper

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtImageFormats component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtImageFormats component

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
%{mingw32_libdir}/qt5/plugins/imageformats/qicns.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qjp2.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qtga.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qtiff.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qwbmp.dll
%{mingw32_libdir}/qt5/plugins/imageformats/qwebp.dll
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{mingw32_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_libdir}/qt5/plugins/imageformats/qicns.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qjp2.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qtga.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qtiff.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qwbmp.dll
%{mingw64_libdir}/qt5/plugins/imageformats/qwebp.dll
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QICNSPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QJp2Plugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QTgaPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QTiffPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QWbmpPlugin.cmake
%{mingw64_libdir}/cmake/Qt5Gui/Qt5Gui_QWebpPlugin.cmake

%changelog
%autochangelog
