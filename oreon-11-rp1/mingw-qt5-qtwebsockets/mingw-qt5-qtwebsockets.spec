%global source0_hash 8cfc13d6465ab43717c508a90b6be15c5cec4952afb3b8c6e5192dabe83ec610

%{?mingw_package_header}

%global qt_module qtwebsockets
#global pre beta

#global commit e5133f4f0bb7c01d7bd7fc499d8c148c03a5b500
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
Summary:        Qt5 for Windows - QtWebsockets component

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebsockets component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtWebsockets component

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
%{mingw32_bindir}/Qt5WebSockets.dll
%{mingw32_includedir}/qt5/QtWebSockets/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/cmake/Qt5WebSockets/
%{mingw32_libdir}/libQt5WebSockets.dll.a
%{mingw32_libdir}/pkgconfig/Qt5WebSockets.pc
%dir %{mingw32_libdir}/qt5/qml/Qt/
%{mingw32_libdir}/qt5/qml/Qt/WebSockets/
%{mingw32_libdir}/qt5/qml/QtWebSockets/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_websockets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_websockets_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5WebSockets.dll
%{mingw64_includedir}/qt5/QtWebSockets/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/cmake/Qt5WebSockets/
%{mingw64_libdir}/libQt5WebSockets.dll.a
%{mingw64_libdir}/pkgconfig/Qt5WebSockets.pc
%dir %{mingw64_libdir}/qt5/qml/Qt/
%{mingw64_libdir}/qt5/qml/Qt/WebSockets/
%{mingw64_libdir}/qt5/qml/QtWebSockets/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_websockets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_websockets_private.pri

%changelog
%autochangelog
