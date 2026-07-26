%global source0_hash 8b8f9c718638081e7b3c000e7f31910140b1202a98e98df5d1b496fe6f639d67

%{?mingw_package_header}

%global qt_module qtimageformats
#global pre rc

#global commit a0ec617b21d9ce0c562e8e7c0dc59bc4d08c509b
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
Summary:        Qt6 for Windows - QtImageFormats component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        http://download.qt.io/%{?pre:development}%{?!pre:official}_releases/qt/%{release_version}/%{qt_version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-src-%{qt_version}%{?pre:-%pre}.tar.xz
%endif

# Fix build: search for Threads ourself instead of promoting imported target
Patch0:         qtimageformats-fix-build.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  ninja-build

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-jasper
BuildRequires:  mingw32-libmng
BuildRequires:  mingw32-libtiff
BuildRequires:  mingw32-libwebp
BuildRequires:  mingw32-qt6-qtbase = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-jasper
BuildRequires:  mingw64-libmng
BuildRequires:  mingw64-libtiff
BuildRequires:  mingw64-libwebp
BuildRequires:  mingw64-qt6-qtbase = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtImageFormats component

%description -n mingw32-qt6-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the 32-bit Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt6-%{qt_module}
Summary:        Qt6 for Windows - QtImageFormats component

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
%{mingw32_libdir}/qt6/plugins/imageformats/qicns.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qjp2.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qmng.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qtga.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qtiff.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qwbmp.dll
%{mingw32_libdir}/qt6/plugins/imageformats/qwebp.dll
%{mingw32_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw32_libdir}/cmake/Qt6/FindLibmng.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapJasper.cmake
%{mingw32_libdir}/cmake/Qt6/FindWrapWebP.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QICNSPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QJp2Plugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QMngPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QTgaPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QTiffPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QWbmpPlugin*.cmake
%{mingw32_libdir}/cmake/Qt6Gui/Qt6QWebpPlugin*.cmake

# Win64
%files -n mingw64-qt6-%{qt_module}
%license LICENSES/*GPL*
%{mingw64_libdir}/qt6/plugins/imageformats/qicns.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qjp2.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qmng.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qtga.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qtiff.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qwbmp.dll
%{mingw64_libdir}/qt6/plugins/imageformats/qwebp.dll
%{mingw64_libdir}/qt6/sbom/%{qt_module}-%{qt_version}.spdx
%{mingw64_libdir}/cmake/Qt6/FindLibmng.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapJasper.cmake
%{mingw64_libdir}/cmake/Qt6/FindWrapWebP.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QICNSPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QJp2Plugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QMngPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QTgaPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QTiffPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QWbmpPlugin*.cmake
%{mingw64_libdir}/cmake/Qt6Gui/Qt6QWebpPlugin*.cmake

%changelog
%autochangelog
