%global source0_hash none

%{?mingw_package_header}

# Disable debuginfo subpackages and debugsource packages for now to use old logic
%undefine _debugsource_packages
%undefine _debuginfo_subpackages

# Override the __debug_install_post argument as this package
# contains both native as well as cross compiled binaries
%global __debug_install_post %%{mingw_debug_install_post}; %{_bindir}/find-debuginfo.sh %{?_missing_build_ids_terminate_build:--strict-build-id} %{?_find_debuginfo_opts} "%{_builddir}/%%{?buildsubdir}" %{nil}

%global qt_module qt3d
#global pre beta

#global commit bdb98baf8253c69949a8c259369203da9ffb269c
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
Summary:        Qt5 for Windows - Qt3d component

License:        LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
URL:            http://qt.io/

%if 0%{?commit:1}
Source0:        https://github.com/qt/%{qt_module}/archive/%{commit}/%{qt_module}-everywhere-src-%{commit}.tar.gz
%else
Source0:        https://download.qt.io/archive/qt/%{release_version}/%{version}%{?pre:-%pre}/submodules/%{qt_module}-everywhere-opensource-src-%{version}%{?pre:-%pre}.tar.xz
%endif

# Make sure -lz is added to the LDFLAGS
Patch0:         qt3d-fix-zlib-linker-flags.patch

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  zlib-devel

BuildRequires:  mingw32-filesystem >= 96
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-qt5-qtbase = %{version}
BuildRequires:  mingw32-qt5-qtbase-devel = %{version}
BuildRequires:  mingw32-qt5-qtdeclarative = %{version}

BuildRequires:  mingw64-filesystem >= 96
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-qt5-qtbase = %{version}
BuildRequires:  mingw64-qt5-qtbase-devel = %{version}
BuildRequires:  mingw64-qt5-qtdeclarative = %{version}

# This package depends on QtOpenGLExtensions which is only available as a static library
# See http://code.qt.io/cgit/qt/qtbase.git/commit/?id=a2ddf3dfe066bb4e58de1d11b1800efcd05fb3a0
BuildRequires:  mingw32-qt5-qtbase-static = %{version}
BuildRequires:  mingw64-qt5-qtbase-static = %{version}

%description
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win32
%package -n mingw32-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch

%description -n mingw32-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw32-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw32-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw32-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

# Win64
%package -n mingw64-qt5-%{qt_module}
Summary:        Qt5 for Windows - Qt3d component
BuildArch:      noarch

%description -n mingw64-qt5-%{qt_module}
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%package -n mingw64-qt5-%{qt_module}-tools
Summary:        Qt5 for Windows - Native tools for the Qt3d component
Requires:       mingw64-qt5-%{qt_module} = %{version}-%{release}

%description -n mingw64-qt5-%{qt_module}-tools
This package contains the Qt software toolkit for developing
cross-platform applications.

This is the Windows version of Qt, for use in conjunction with the
Fedora Windows cross-compiler.

%{?mingw_debug_package}

%prep
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

# Exclude debug files from the main files (note: the debug files are only created after %%install, so we can't search for them directly)
find %{buildroot}%{mingw32_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw32-qt5-%{qt_module}.debugfiles
find %{buildroot}%{mingw64_prefix} | grep -E '.(exe|dll|pyd)$' | sed 's|^%{buildroot}\(.*\)$|%%exclude \1.debug|' > mingw64-qt5-%{qt_module}.debugfiles

# Win32
%files -n mingw32-qt5-%{qt_module} -f mingw32-qt5-%{qt_module}.debugfiles
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw32_bindir}/Qt53DAnimation.dll
%{mingw32_bindir}/Qt53DCore.dll
%{mingw32_bindir}/Qt53DExtras.dll
%{mingw32_bindir}/Qt53DInput.dll
%{mingw32_bindir}/Qt53DLogic.dll
%{mingw32_bindir}/Qt53DQuick.dll
%{mingw32_bindir}/Qt53DQuickAnimation.dll
%{mingw32_bindir}/Qt53DQuickExtras.dll
%{mingw32_bindir}/Qt53DQuickInput.dll
%{mingw32_bindir}/Qt53DQuickRender.dll
%{mingw32_bindir}/Qt53DQuickScene2D.dll
%{mingw32_bindir}/Qt53DRender.dll
%{mingw32_includedir}/qt5/Qt3DAnimation/
%{mingw32_includedir}/qt5/Qt3DCore/
%{mingw32_includedir}/qt5/Qt3DExtras/
%{mingw32_includedir}/qt5/Qt3DInput/
%{mingw32_includedir}/qt5/Qt3DLogic/
%{mingw32_includedir}/qt5/Qt3DQuick/
%{mingw32_includedir}/qt5/Qt3DQuickAnimation/
%{mingw32_includedir}/qt5/Qt3DQuickExtras/
%{mingw32_includedir}/qt5/Qt3DQuickInput/
%{mingw32_includedir}/qt5/Qt3DQuickRender/
%{mingw32_includedir}/qt5/Qt3DQuickScene2D/
%{mingw32_includedir}/qt5/Qt3DRender/
%{mingw32_libdir}/*.prl
%{mingw32_libdir}/libQt53DAnimation.dll.a
%{mingw32_libdir}/libQt53DCore.dll.a
%{mingw32_libdir}/libQt53DExtras.dll.a
%{mingw32_libdir}/libQt53DInput.dll.a
%{mingw32_libdir}/libQt53DLogic.dll.a
%{mingw32_libdir}/libQt53DQuick.dll.a
%{mingw32_libdir}/libQt53DQuickAnimation.dll.a
%{mingw32_libdir}/libQt53DQuickExtras.dll.a
%{mingw32_libdir}/libQt53DQuickInput.dll.a
%{mingw32_libdir}/libQt53DQuickRender.dll.a
%{mingw32_libdir}/libQt53DQuickScene2D.dll.a
%{mingw32_libdir}/libQt53DRender.dll.a
%{mingw32_libdir}/qt5/plugins/geometryloaders/
%{mingw32_libdir}/qt5/plugins/renderers/
%{mingw32_libdir}/qt5/plugins/renderplugins/
%{mingw32_libdir}/qt5/plugins/sceneparsers/
%{mingw32_libdir}/cmake/Qt53DAnimation/
%{mingw32_libdir}/cmake/Qt53DCore/
%{mingw32_libdir}/cmake/Qt53DExtras/
%{mingw32_libdir}/cmake/Qt53DInput/
%{mingw32_libdir}/cmake/Qt53DLogic/
%{mingw32_libdir}/cmake/Qt53DQuick/
%{mingw32_libdir}/cmake/Qt53DQuickAnimation/
%{mingw32_libdir}/cmake/Qt53DQuickExtras/
%{mingw32_libdir}/cmake/Qt53DQuickInput/
%{mingw32_libdir}/cmake/Qt53DQuickRender/
%{mingw32_libdir}/cmake/Qt53DQuickScene2D/
%{mingw32_libdir}/cmake/Qt53DRender/
%{mingw32_libdir}/pkgconfig/Qt53DAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt53DCore.pc
%{mingw32_libdir}/pkgconfig/Qt53DExtras.pc
%{mingw32_libdir}/pkgconfig/Qt53DInput.pc
%{mingw32_libdir}/pkgconfig/Qt53DLogic.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuick.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickInput.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickRender.pc
%{mingw32_libdir}/pkgconfig/Qt53DQuickScene2D.pc
%{mingw32_libdir}/pkgconfig/Qt53DRender.pc
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3danimation.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dcore.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dextras.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dinput.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquick.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3drender.pri
%{mingw32_datadir}/qt5/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw32_libdir}/qt5/qml/Qt3D/
%dir %{mingw32_libdir}/qt5/qml/QtQuick/
%{mingw32_libdir}/qt5/qml/QtQuick/Scene2D/
%{mingw32_libdir}/qt5/qml/QtQuick/Scene3D/

%files -n mingw32-qt5-%{qt_module}-tools
%{_prefix}/%{mingw32_target}/bin/qt5/qgltf

# Win64
%files -n mingw64-qt5-%{qt_module} -f mingw64-qt5-%{qt_module}.debugfiles
%license LICENSE.LGPL* LICENSE.GPL*
%{mingw64_bindir}/Qt53DAnimation.dll
%{mingw64_bindir}/Qt53DCore.dll
%{mingw64_bindir}/Qt53DExtras.dll
%{mingw64_bindir}/Qt53DInput.dll
%{mingw64_bindir}/Qt53DLogic.dll
%{mingw64_bindir}/Qt53DQuick.dll
%{mingw64_bindir}/Qt53DQuickAnimation.dll
%{mingw64_bindir}/Qt53DQuickExtras.dll
%{mingw64_bindir}/Qt53DQuickInput.dll
%{mingw64_bindir}/Qt53DQuickRender.dll
%{mingw64_bindir}/Qt53DQuickScene2D.dll
%{mingw64_bindir}/Qt53DRender.dll
%{mingw64_includedir}/qt5/Qt3DAnimation/
%{mingw64_includedir}/qt5/Qt3DCore/
%{mingw64_includedir}/qt5/Qt3DExtras/
%{mingw64_includedir}/qt5/Qt3DInput/
%{mingw64_includedir}/qt5/Qt3DLogic/
%{mingw64_includedir}/qt5/Qt3DQuick/
%{mingw64_includedir}/qt5/Qt3DQuickAnimation/
%{mingw64_includedir}/qt5/Qt3DQuickExtras/
%{mingw64_includedir}/qt5/Qt3DQuickInput/
%{mingw64_includedir}/qt5/Qt3DQuickRender/
%{mingw64_includedir}/qt5/Qt3DQuickScene2D/
%{mingw64_includedir}/qt5/Qt3DRender/
%{mingw64_libdir}/*.prl
%{mingw64_libdir}/libQt53DAnimation.dll.a
%{mingw64_libdir}/libQt53DCore.dll.a
%{mingw64_libdir}/libQt53DExtras.dll.a
%{mingw64_libdir}/libQt53DInput.dll.a
%{mingw64_libdir}/libQt53DLogic.dll.a
%{mingw64_libdir}/libQt53DQuick.dll.a
%{mingw64_libdir}/libQt53DQuickAnimation.dll.a
%{mingw64_libdir}/libQt53DQuickExtras.dll.a
%{mingw64_libdir}/libQt53DQuickInput.dll.a
%{mingw64_libdir}/libQt53DQuickRender.dll.a
%{mingw64_libdir}/libQt53DQuickScene2D.dll.a
%{mingw64_libdir}/libQt53DRender.dll.a
%{mingw64_libdir}/qt5/plugins/geometryloaders/
%{mingw64_libdir}/qt5/plugins/renderers/
%{mingw64_libdir}/qt5/plugins/renderplugins/
%{mingw64_libdir}/qt5/plugins/sceneparsers/
%{mingw64_libdir}/cmake/Qt53DAnimation/
%{mingw64_libdir}/cmake/Qt53DCore/
%{mingw64_libdir}/cmake/Qt53DExtras/
%{mingw64_libdir}/cmake/Qt53DInput/
%{mingw64_libdir}/cmake/Qt53DLogic/
%{mingw64_libdir}/cmake/Qt53DQuick/
%{mingw64_libdir}/cmake/Qt53DQuickAnimation/
%{mingw64_libdir}/cmake/Qt53DQuickExtras/
%{mingw64_libdir}/cmake/Qt53DQuickInput/
%{mingw64_libdir}/cmake/Qt53DQuickRender/
%{mingw64_libdir}/cmake/Qt53DQuickScene2D/
%{mingw64_libdir}/cmake/Qt53DRender/
%{mingw64_libdir}/pkgconfig/Qt53DAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt53DCore.pc
%{mingw64_libdir}/pkgconfig/Qt53DExtras.pc
%{mingw64_libdir}/pkgconfig/Qt53DInput.pc
%{mingw64_libdir}/pkgconfig/Qt53DLogic.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuick.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickInput.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickRender.pc
%{mingw64_libdir}/pkgconfig/Qt53DQuickScene2D.pc
%{mingw64_libdir}/pkgconfig/Qt53DRender.pc
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3danimation.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3danimation_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dcore.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dcore_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dextras.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dextras_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dinput.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dinput_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dlogic_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquick.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquick_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickanimation_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickextras_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickinput_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickrender_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3dquickscene2d_private.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3drender.pri
%{mingw64_datadir}/qt5/mkspecs/modules/qt_lib_3drender_private.pri
%{mingw64_libdir}/qt5/qml/Qt3D/
%dir %{mingw64_libdir}/qt5/qml/QtQuick/
%{mingw64_libdir}/qt5/qml/QtQuick/Scene2D/
%{mingw64_libdir}/qt5/qml/QtQuick/Scene3D/

%files -n mingw64-qt5-%{qt_module}-tools
%{_prefix}/%{mingw64_target}/bin/qt5/qgltf

%changelog
%autochangelog
