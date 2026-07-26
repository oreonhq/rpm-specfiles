%global source0_hash none

%ifarch %{ix86}
    %global arch i686
%else
    %global arch %{_arch}
%endif

%ifarch %{?qt6_qtwebengine_arches}
%global webengine 1
%endif

%global qt5_ver %(echo %{_qt5_version} | cut -d. -f1,2)
%global qt5_target %(echo qt%{qt5_ver}-%{arch} | sed 's/\\./_/g')
  
%global qt6_ver %(echo %{_qt6_version} | cut -d. -f1,2)
%global qt6_target %(echo qt%{qt6_ver}-%{arch} | sed 's/\\./_/g')

%global gammaray_ver 3.1
%global gammaray_ver_minor 0
%global gammaray_version %{gammaray_ver}.%{gammaray_ver_minor}

Name:    gammaray
Version: 3.1.0
Release: 19%{?dist}
Summary: A tool for examining internals of Qt applications
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License: GPL-2.0-or-later
URL:     https://github.com/KDAB/GammaRay

Source0: %{url}/releases/download/v%{version}/%{name}-%{version}.tar.gz

Patch1:  gammaray-fix-build-with-qt6.8.patch
Patch2:  gammaray-fix-build-for-qt-6.9.patch
Patch3:  gammaray-fix-build-against-qt-6-10.patch

BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: ninja-build
BuildRequires: desktop-file-utils

BuildRequires: elfutils-devel
BuildRequires: binutils-devel
BuildRequires: libdwarf-devel
BuildRequires: libunwind-devel

BuildRequires: kf6-rpm-macros
BuildRequires: extra-cmake-modules

# to build the documentation
BuildRequires: doxygen
BuildRequires: qt6-doc-devel
BuildRequires: qt6-doc-html
BuildRequires: qt6-doctools

# Qt6 GUI and probe
BuildRequires: qt6-qtbase-private-devel
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt63DAnimation)
BuildRequires: cmake(Qt63DExtras)
BuildRequires: cmake(Qt63DInput)
BuildRequires: cmake(Qt63DLogic)
BuildRequires: cmake(Qt63DRender)
BuildRequires: cmake(Qt63DQuick)
BuildRequires: cmake(Qt6Bluetooth)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: cmake(Qt6Designer)
BuildRequires: cmake(Qt6Location)
BuildRequires: cmake(Qt6OpenGL)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6QuickWidgets)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6ShaderTools)
%if 0%{?webengine}
BuildRequires: cmake(Qt6WebEngineWidgets)
%endif
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WaylandCompositor)
BuildRequires: wayland-devel

# optional dependencies
BuildRequires: cmake(Qt6Scxml)
BuildRequires: cmake(Qt6StateMachine)
BuildRequires: cmake(KF6SyntaxHighlighting)

# for building the probe qt5 for introspection of Qt5 apps
BuildRequires:	qt5-qt3d-devel
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-qtbase-doc
BuildRequires:	qt5-qtbase-private-devel
BuildRequires:	qt5-qtdeclarative-devel
BuildRequires:	qt5-qtscript-devel
BuildRequires:	qt5-qtsvg-devel
BuildRequires:	qt5-qtscxml-devel
BuildRequires:	qt5-qttools-devel
BuildRequires:	qt5-qtwayland-devel
%ifarch %{?qt5_qtwebengine_arches}
BuildRequires: qt5-qtwebengine-devel
%endif

Requires:	%{name}-probe = %{version}-%{release}
Recommends:	(%{name}-probe-qt5%{?_isa} = %{version}-%{release} if qt5-qtbase)
Recommends:	(%{name}-probe-qt6%{?_isa} = %{version}-%{release} if qt6-qtbase)
# When -doc subpkg was removed
Obsoletes: %{name}-doc <= 2.2.1

# omit provides from plugins
%global __provides_exclude_from \
         ^((%{_qt5_libdir}|%{_qt6_libdir})/libgammaray.*\\.so)$
         
%description
A tool to poke around in a Qt-application and also to manipulate
the application to some extent. It uses various DLL injection
techniques to hook into an application at run-time and provide
access to a lot of interesting information.

GammaRay can introspect Qt 6 and Qt 5 applications.

%package probe-qt5
Summary:	Qt 5 probe for GammaRay
Provides:	%{name}-probe = %{version}-%{release}
Obsoletes:	%{name}-qt5 < %{version}-%{release}
Requires:	qt5-qtbase%{?_isa} = %{_qt5_version}
Requires:	%{name} = %{version}-%{release}

%description probe-qt5
Provides a Qt 5 probe for GammaRay that allows introspecting Qt 5
applications. It is possible to install probes for different
architectures or Qt versions as well. GammaRay will then be able
to inspect those applications too.

%package probe-qt5-devel
Summary:        Development files for %{name} Qt5 probe
Requires:       %{name}-probe-qt5%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description probe-qt5-devel
The %{name}probe-qt5-devel package contains development libraries for
the %{name} Qt5 integration.

%package probe-qt6
Summary:    Qt 6 probe for GammaRay
Provides:   %{name}-probe = %{version}-%{release}
Requires:   qt6-qtbase%{?_isa} = %{_qt6_version}
Requires:   %{name} = %{version}-%{release}

%description probe-qt6
Provides a Qt 6 probe for GammaRay that allows introspecting Qt 6
applications. It is possible to install probes for different
architectures or Qt versions as well. GammaRay will then be able
to inspect those applications too.

%package probe-qt6-devel
Summary:        Development files for %{name} Qt6 probe
Requires:       %{name}-probe-qt6%{?_isa} = %{version}-%{release}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description probe-qt6-devel
The %{name}probe-qt6-devel package contains development libraries for
the %{name} Qt6 integration.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-probe-qt6-devel%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing plugins for %{name}.

	
%package        doc
Summary:        Developer Documentation files for %{name}
BuildArch:      noarch

%description    doc
Developer Documentation files for %{name} for use with KDevelop or QtCreator.

%prep
%autosetup -n %{name}-%{version} -p1

%build

%define _vpath_builddir %{_target_platform}_client
%cmake_qt6 \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt6_DIR=%{_libdir}/cmake/Qt6 \
    -DQT_VERSION_MAJOR=6 \
    -DGAMMARAY_QT6_BUILD:BOOL=TRUE \
    -DGAMMARAY_CLIENT_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_BUILD_DOCS:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec \
    -DECM_MKSPECS_INSTALL_DIR=%{_qt6_mkspecsdir}/modules \
    -DQCH_INSTALL_DIR=%{_qt6_docdir} \
    -DQT_INSTALL_BINS=%{_qt6_libexecdir} \
    -DQDOC_INDEX_DIR=%{_qt6_docdir} \
    -DQDOC_TEMPLATE_DIR=%{_qt6_docdir}

%cmake_build

# build the Qt6 probe only
%define _vpath_builddir %{_target_platform}_qt6
%cmake_qt6 \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt6_DIR=%{_libdir}/cmake/Qt6 \
    -DQT_VERSION_MAJOR=6 \
    -DGAMMARAY_QT6_BUILD:BOOL=TRUE \
    -DGAMMARAY_BUILD_UI:BOOL=FALSE \
    -DGAMMARAY_BUILD_DOCS:BOOL=FALSE \
    -DGAMMARAY_PROBE_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec

%cmake_build

# build the Qt5 probe only
%define _vpath_builddir %{_target_platform}_qt5
%cmake \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=TRUE \
    -DQt5_DIR=%{_libdir}/cmake/Qt5 \
    -DQt_DIR=%{_libdir}/cmake/Qt5 \
    -DQT_VERSION_MAJOR=5 \
    -DGAMMARAY_QT6_BUILD:BOOL=FALSE \
    -DGAMMARAY_BUILD_UI:BOOL=FALSE \
    -DGAMMARAY_BUILD_DOCS:BOOL=FALSE \
    -DGAMMARAY_PROBE_ONLY_BUILD:BOOL=TRUE \
    -DGAMMARAY_INSTALL_QT_LAYOUT:BOOL=FALSE \
    -DLIBEXEC_INSTALL_DIR=libexec

%cmake_build

%install

%define _vpath_builddir %{_target_platform}_client
%cmake_install
%define _vpath_builddir %{_target_platform}_qt6
%cmake_install
%define _vpath_builddir %{_target_platform}_qt5
%cmake_install

# We install the license manually
rm -fv %{buildroot}%{_docdir}/gammaray/LICENSE.txt
rm -rfv %{buildroot}%{_docdir}/gammaray/LICENSES

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/GammaRay.desktop

%files
%doc README.md
%license LICENSES/*
%{_bindir}/gammaray
%{_qt6_libdir}/libgammaray_client.so.*
%{_qt6_libdir}/libgammaray_launcher.so.*
%{_qt6_libdir}/libgammaray_launcher_ui.so.*
%{_qt6_libdir}/libgammaray_kuserfeedback.so.*
%{_qt6_libdir}/gammaray/libexec/gammaray-launcher
%{_qt6_libdir}/gammaray/libexec/gammaray-client
%{_datadir}/applications/GammaRay.desktop
%{_datadir}/icons/hicolor/*/apps/GammaRay.png
%{_datadir}/metainfo/com.kdab.GammaRay.metainfo.xml
%{_datadir}/zsh/site-functions/_gammaray
%lang(de) %{_datadir}/gammaray/translations/gammaray_de.qm
%lang(en) %{_datadir}/gammaray/translations/gammaray_en.qm

%files probe-qt5
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so.*
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so.*
%{_qt5_libdir}/gammaray/%{gammaray_ver}/%{qt5_target}/

%files probe-qt5-devel
%{_qt5_libdir}/libgammaray_common-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_core-%{qt5_target}.so
%{_qt5_libdir}/libgammaray_kitemmodels-%{qt5_target}.so
  
%files probe-qt6
%{_qt6_libdir}/libgammaray_ui-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_common-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_core-%{qt6_target}.so.*
%{_qt6_libdir}/libgammaray_kitemmodels-%{qt6_target}.so.*
%{_qt6_libdir}/gammaray/%{gammaray_ver}/%{qt6_target}/

%files probe-qt6-devel
%{_qt6_libdir}/libgammaray_ui-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_common-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_core-%{qt6_target}.so
%{_qt6_libdir}/libgammaray_kitemmodels-%{qt6_target}.so
%{_qt6_libdir}/gammaray/%{gammaray_ver}/%{qt6_target}/

%files devel
%{_includedir}/gammaray
%{_qt6_libdir}/libgammaray_client.so
%{_qt6_libdir}/libgammaray_launcher.so
%{_qt6_libdir}/libgammaray_launcher_ui.so
%{_qt6_libdir}/libgammaray_kuserfeedback.so
%{_libdir}/cmake/GammaRay/
# this is an error in the sources, it should go to qt6
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayCommon.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayCore.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayUi.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayClient.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayKItemModels.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayLauncher.pri
%{_qt6_archdatadir}/mkspecs/modules/qt_GammaRayLauncherUi.pri

%files doc
%{_mandir}/man1/gammaray.1.gz
%{_qt6_docdir}/gammaray-api.qch
%{_qt6_docdir}/gammaray-manual.qch
%{_qt6_docdir}/gammaray.qhc

%changelog
%autochangelog
