%global source0_hash cb7f4cb1ac219ba188d69d01eb7a6103dc53d147c534b86752c6f7fdd9facf63

%{?mingw_package_header}

%global qt_module qtactiveqt
#global pre rc

#global commit 435fac3bc7d12771a3c80556e748a2388e914cf7
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
Summary:        Qt5 for Windows - QtActiveQt component

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

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}

# Don't try to build stuff which requires windows.h with the native Linux gcc
Patch0:         qtactiveqt-fix-host-build.patch

# dumpcpp and MetaObjectGenerator::readClassInfo do not handle win64
# https://bugreports.qt.io/browse/QTBUG-46827
Patch1:         qtactiveqt-win64.patch

# qt_sendSpontaneousEvent is not part of libQt5Core.a?!
Patch2:         qtactiveqt-spontaneous-event.patch

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtActiveQt component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtActiveQt component

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
find %{buildroot} -name "*.prl" -delete

# Win32
%files -n mingw32-qt5-%{qt_module}
%license LICENSE.GPL3-EXCEPT
%{mingw32_bindir}/dumpcpp.exe
%{mingw32_bindir}/dumpdoc.exe
%{mingw32_bindir}/idc.exe
%{mingw32_bindir}/testcon.exe
%{mingw32_includedir}/qt5/ActiveQt/
%{mingw32_libdir}/libQt5AxBase.a
%{mingw32_libdir}/libQt5AxContainer.a
%{mingw32_libdir}/libQt5AxServer.a
%{mingw32_libdir}/cmake/Qt5AxBase/
%{mingw32_libdir}/cmake/Qt5AxContainer/
%{mingw32_libdir}/cmake/Qt5AxServer/
%{mingw32_libdir}/pkgconfig/Qt5AxBase.pc
%{mingw32_libdir}/pkgconfig/Qt5AxContainer.pc
%{mingw32_libdir}/pkgconfig/Qt5AxServer.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axbase.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axbase_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axserver.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_axserver_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.GPL3-EXCEPT
%{mingw64_bindir}/dumpcpp.exe
%{mingw64_bindir}/dumpdoc.exe
%{mingw64_bindir}/idc.exe
%{mingw64_bindir}/testcon.exe
%{mingw64_includedir}/qt5/ActiveQt/
%{mingw64_libdir}/libQt5AxBase.a
%{mingw64_libdir}/libQt5AxContainer.a
%{mingw64_libdir}/libQt5AxServer.a
%{mingw64_libdir}/cmake/Qt5AxBase/
%{mingw64_libdir}/cmake/Qt5AxContainer/
%{mingw64_libdir}/cmake/Qt5AxServer/
%{mingw64_libdir}/pkgconfig/Qt5AxBase.pc
%{mingw64_libdir}/pkgconfig/Qt5AxContainer.pc
%{mingw64_libdir}/pkgconfig/Qt5AxServer.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axbase.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axbase_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axcontainer_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axserver.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_axserver_private.pri

%changelog
%autochangelog
