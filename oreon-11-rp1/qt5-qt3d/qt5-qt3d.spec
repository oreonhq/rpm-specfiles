%global qt_module qt3d

%global multilib_archs x86_64 %{ix86} %{?mips} ppc64 ppc s390x s390 sparc64 sparcv9

Summary: Qt5 - Qt3D QML bindings and C++ APIs
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
# See also http://doc.qt.io/qt-5/licensing.html
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
Source1: qt3dcore-config-multilib_p.h

BuildRequires: make
BuildRequires: qt5-rpm-macros >= %{version}
BuildRequires: qt5-qtbase-static >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtimageformats
BuildRequires: qt5-qtxmlpatterns-devel
%if 0%{?fedora} || 0%{?oreon}
BuildRequires: pkgconfig(assimp) >= 3.3.1
%endif
Requires: qt5-qtimageformats%{?_isa} >= %{version}

%description
Qt 3D provides functionality for near-realtime simulation systems with
support for 2D and 3D rendering in both Qt C++ and Qt Quick applications).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
%description devel
%{summary}.

%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
%description examples
%{summary}.


%prep
%setup -q -n %{qt_module}-everywhere-src-%{version}


%build
# QT is known not to work properly with LTO at this point.  Some of the issues
# are being worked on upstream and disabling LTO should be re-evaluated as
# we update this change.  Until such time...
# Disable LTO
%define _lto_cflags %{nil}

%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

%ifarch %{multilib_archs}
# multilib: qt3dcore-config_p.h
  mv %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config-%{__isa_bits}_p.h
  install -p -m644 -D %{SOURCE1} %{buildroot}%{_qt5_headerdir}/Qt3DCore/%{version}/Qt3DCore/private/qt3dcore-config_p.h
%endif

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt5_libdir}
for prl_file in libQt5*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSE.GPL* LICENSE.LGPL*
%{_qt5_libdir}/libQt53DQuick.so.5*
%{_qt5_libdir}/libQt53DInput.so.5*
%{_qt5_libdir}/libQt53DQuickRender.so.5*
%{_qt5_libdir}/libQt53DRender.so.5*
%{_qt5_libdir}/libQt53DCore.so.5*
%{_qt5_libdir}/libQt53DLogic.so.5*
%{_qt5_libdir}/libQt53DQuickInput.so.5*
%{_qt5_libdir}/libQt53DExtras.so.5*
%{_qt5_libdir}/libQt53DAnimation.so.5*
%{_qt5_libdir}/libQt53DQuickAnimation.so.5*
%{_qt5_libdir}/libQt53DQuickScene2D.so.5*
%{_qt5_libdir}/libQt53DQuickExtras.so.5*
%{_qt5_qmldir}/Qt3D/
%{_qt5_qmldir}/QtQuick/Scene3D/
%{_qt5_qmldir}/QtQuick/Scene2D/
%{_qt5_plugindir}/renderers/
%{_qt5_plugindir}/sceneparsers/
%{_qt5_plugindir}/renderplugins/
%{_qt5_plugindir}/geometryloaders/

%files devel
%{_qt5_bindir}/qgltf
%{_qt5_libdir}/libQt53DQuick.so
%{_qt5_libdir}/libQt53DQuick.prl
%{_qt5_libdir}/cmake/Qt53DQuick
%{_qt5_includedir}/Qt3DQuick
%{_qt5_libdir}/pkgconfig/Qt53DQuick.pc
%{_qt5_libdir}/libQt53DInput.so
%{_qt5_libdir}/libQt53DInput.prl
%{_qt5_libdir}/cmake/Qt53DInput
%{_qt5_includedir}/Qt3DInput/
%{_qt5_libdir}/pkgconfig/Qt53DInput.pc
%{_qt5_libdir}/libQt53DCore.so
%{_qt5_libdir}/libQt53DCore.prl
%{_qt5_libdir}/cmake/Qt53DCore/
%{_qt5_includedir}/Qt3DCore/
%{_qt5_libdir}/pkgconfig/Qt53DCore.pc
%{_qt5_libdir}/libQt53DQuickRender.so
%{_qt5_libdir}/libQt53DQuickRender.prl
%{_qt5_libdir}/cmake/Qt53DQuickRender/
%{_qt5_includedir}/Qt3DQuickRender/
%{_qt5_libdir}/pkgconfig/Qt53DQuickRender.pc
%{_qt5_libdir}/libQt53DRender.so
%{_qt5_libdir}/libQt53DRender.prl
%{_qt5_libdir}/cmake/Qt53DRender/
%{_qt5_includedir}/Qt3DRender/
%{_qt5_libdir}/pkgconfig/Qt53DRender.pc
%{_qt5_archdatadir}/mkspecs/modules/*.pri
%{_qt5_libdir}/libQt53DLogic.so
%{_qt5_libdir}/libQt53DLogic.prl
%{_qt5_includedir}/Qt3DLogic/
%{_qt5_libdir}/cmake/Qt53DLogic
%{_qt5_libdir}/pkgconfig/Qt53DLogic.pc
%{_qt5_libdir}/libQt53DQuickInput.so
%{_qt5_libdir}/libQt53DQuickInput.prl
%{_qt5_includedir}/Qt3DQuickInput/
%{_qt5_libdir}/cmake/Qt53DQuickInput
%{_qt5_libdir}/pkgconfig/Qt53DQuickInput.pc
%{_qt5_libdir}/libQt53DExtras.so
%{_qt5_libdir}/libQt53DExtras.prl
%{_qt5_libdir}/cmake/Qt53DExtras
%{_qt5_includedir}/Qt3DExtras
%{_qt5_libdir}/pkgconfig/Qt53DExtras.pc
%{_qt5_libdir}/libQt53DQuickExtras.so
%{_qt5_libdir}/libQt53DQuickExtras.prl
%{_qt5_libdir}/cmake/Qt53DQuickExtras
%{_qt5_includedir}/Qt3DQuickExtras
%{_qt5_libdir}/pkgconfig/Qt53DQuickExtras.pc
%{_qt5_libdir}/libQt53DAnimation.so
%{_qt5_libdir}/libQt53DAnimation.prl
%{_qt5_libdir}/cmake/Qt53DAnimation
%{_qt5_includedir}/Qt3DAnimation
%{_qt5_libdir}/pkgconfig/Qt53DAnimation.pc
%{_qt5_libdir}/libQt53DQuickAnimation.so
%{_qt5_libdir}/libQt53DQuickAnimation.prl
%{_qt5_libdir}/cmake/Qt53DQuickAnimation
%{_qt5_includedir}/Qt3DQuickAnimation
%{_qt5_libdir}/pkgconfig/Qt53DQuickAnimation.pc
%{_qt5_libdir}/libQt53DQuickScene2D.so
%{_qt5_libdir}/libQt53DQuickScene2D.prl
%{_qt5_libdir}/cmake/Qt53DQuickScene2D
%{_qt5_includedir}/Qt3DQuickScene2D
%{_qt5_libdir}/pkgconfig/Qt53DQuickScene2D.pc

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
