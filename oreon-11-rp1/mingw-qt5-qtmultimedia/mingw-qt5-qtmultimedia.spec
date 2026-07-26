%global source0_hash 4c77fb601d10fdffe4a4749f9008a969d778c3bb0e6734bda39e7f46cd11c38c

%{?mingw_package_header}

%global qt_module qtmultimedia
#global pre beta

#global commit a73dfa7c63b82e25f93e44ed6386664373aaca74
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
Summary:        Qt5 for Windows - QtMultimedia component

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}
BuildRequires:  mingw32-openal-soft

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-angleproject >= 0-0.16.git8613f49
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}
BuildRequires:  mingw64-openal-soft

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtMultimedia component

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - QtMultimedia component

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
%{mingw32_bindir}/Qt5Multimedia.dll
%{mingw32_bindir}/Qt5MultimediaQuick.dll
%{mingw32_bindir}/Qt5MultimediaWidgets.dll
%{mingw32_includedir}/qt5/QtMultimedia/
%{mingw32_includedir}/qt5/QtMultimediaQuick/
%{mingw32_includedir}/qt5/QtMultimediaWidgets/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt5Multimedia.dll.a
%{mingw32_libdir}/libQt5MultimediaQuick.dll.a
%{mingw32_libdir}/libQt5MultimediaWidgets.dll.a
%{mingw32_libdir}/cmake/Qt5Multimedia/
%{mingw32_libdir}/cmake/Qt5MultimediaQuick/
%{mingw32_libdir}/cmake/Qt5MultimediaWidgets/
%{mingw32_libdir}/pkgconfig/Qt5Multimedia.pc
%{mingw32_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{mingw32_libdir}/qt5/plugins/audio/
%{mingw32_libdir}/qt5/plugins/mediaservice/
%{mingw32_libdir}/qt5/plugins/playlistformats/
%{mingw32_libdir}/qt5/qml/QtMultimedia/
%{mingw32_libdir}/qt5/qml/QtAudioEngine/
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimedia.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

# Win64
%files -n mingw64-qt5-%{qt_module}
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt5Multimedia.dll
%{mingw64_bindir}/Qt5MultimediaQuick.dll
%{mingw64_bindir}/Qt5MultimediaWidgets.dll
%{mingw64_includedir}/qt5/QtMultimedia/
%{mingw64_includedir}/qt5/QtMultimediaQuick/
%{mingw64_includedir}/qt5/QtMultimediaWidgets/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt5Multimedia.dll.a
%{mingw64_libdir}/libQt5MultimediaQuick.dll.a
%{mingw64_libdir}/libQt5MultimediaWidgets.dll.a
%{mingw64_libdir}/cmake/Qt5Multimedia/
%{mingw64_libdir}/cmake/Qt5MultimediaQuick/
%{mingw64_libdir}/cmake/Qt5MultimediaWidgets/
%{mingw64_libdir}/pkgconfig/Qt5Multimedia.pc
%{mingw64_libdir}/pkgconfig/Qt5MultimediaWidgets.pc
%{mingw64_libdir}/qt5/plugins/audio/
%{mingw64_libdir}/qt5/plugins/mediaservice/
%{mingw64_libdir}/qt5/plugins/playlistformats/
%{mingw64_libdir}/qt5/qml/QtMultimedia/
%{mingw64_libdir}/qt5/qml/QtAudioEngine/
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimedia.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimedia_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_multimediawidgets_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_qtmultimediaquicktools_private.pri

%changelog
%autochangelog
