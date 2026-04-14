
%global qt_module qtwebsockets

#global unstable 0
%if 0%{?unstable}
%global prerelease rc
%endif

%global examples 1
# Examples plus QML import blow mock disk on some aarch64 workers
%ifarch aarch64
%global examples 0
%endif

Summary: Qt6 - WebSockets component
Name:    qt6-%{qt_module}
Version: 6.10.3
Release: 5%{?dist}

License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://qt-project.org/
%global  majmin %(echo %{version} | cut -d. -f1-2)
%global  qt_version %(echo %{version} | cut -d~ -f1)

%if 0%{?unstable}
Source0: https://download.qt.io/development_releases/qt/%{majmin}/%{qt_version}/submodules/%{qt_module}-everywhere-src-%{qt_version}-%{prerelease}.tar.xz
%else
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-src-%{version}.tar.xz
%endif

# filter qml provides
%global __provides_exclude_from ^%{_qt6_archdatadir}/qml/.*\\.so$

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ninja-build
BuildRequires: qt6-rpm-macros
BuildRequires: qt6-qtbase-devel >= %{version}
BuildRequires: qt6-qtbase-private-devel
#libQt6Core.so.6(Qt_5_PRIVATE_API)(64bit)
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}
BuildRequires: qt6-qtdeclarative-devel

BuildRequires: pkgconfig(xkbcommon) >= 0.5.0
BuildRequires: openssl-devel

%description
The QtWebSockets module implements the WebSocket protocol as specified in RFC
6455. It solely depends on Qt (no external dependencies).

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt6-qtbase-devel%{?_isa}
%description devel
%{summary}.

%if 0%{?examples}
%package examples
Summary: Programming examples for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
# BuildRequires: qt6-qtwebsockets-devel (same version as this package)
%description examples
%{summary}.
%endif

%prep
%autosetup -n %{qt_module}-everywhere-src-%{qt_version}%{?unstable:-%{prerelease}} -p1


%build
%cmake_qt6 \
%if 0%{?examples}
  -DQT_BUILD_EXAMPLES:BOOL=ON \
  -DQT_INSTALL_EXAMPLES_SOURCES=ON \
%else
  -DQT_BUILD_EXAMPLES:BOOL=OFF \
  -DQT_INSTALL_EXAMPLES_SOURCES=OFF \
%endif

%cmake_build


%install
%cmake_install
%if ! 0%{?examples}
# Belt and suspenders if anything still lands under examples
rm -rf %{buildroot}%{_qt6_examplesdir}/websockets
%endif

## .prl/.la file love
# nuke .prl reference(s) to %%buildroot, excessive (.la-like) libs
pushd %{buildroot}%{_qt6_libdir}
for prl_file in libQt6*.prl ; do
  sed -i -e "/^QMAKE_PRL_BUILD_DIR/d" ${prl_file}
  if [ -f "$(basename ${prl_file} .prl).so" ]; then
    rm -fv "$(basename ${prl_file} .prl).la"
    sed -i -e "/^QMAKE_PRL_LIBS/d" ${prl_file}
  fi
done
popd


%ldconfig_scriptlets

%files
%license LICENSES/*
%{_qt6_archdatadir}/sbom/%{qt_module}-%{qt_version}.spdx
%{_qt6_libdir}/libQt6WebSockets.so.6*

%files devel
%{_qt6_headerdir}/QtWebSockets/
%{_qt6_libdir}/libQt6WebSockets.so
%{_qt6_libdir}/libQt6WebSockets.prl
%{_qt6_libdir}/cmake/Qt6BuildInternals/StandaloneTests/QtWebSocketsTestsConfig.cmake
%{_qt6_libdir}/cmake/Qt6Qml/QmlPlugins/*.cmake
%dir %{_qt6_libdir}/cmake/Qt6WebSockets/
%dir %{_qt6_libdir}/cmake/Qt6WebSocketsPrivate/
%{_qt6_libdir}/cmake/Qt6WebSockets/*.cmake
%{_qt6_libdir}/cmake/Qt6WebSocketsPrivate/*.cmake
%{_qt6_libdir}/qt6/qml/QtWebSockets/
%{_qt6_archdatadir}/mkspecs/modules/qt_lib_websockets*.pri
%{_qt6_libdir}/qt6/metatypes/qt6*_metatypes.json
%{_qt6_libdir}/qt6/modules/*.json
%{_qt6_libdir}/pkgconfig/*.pc

%if 0%{?examples}
%files examples
%{_qt6_examplesdir}/
%endif


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.3-5
- Sync module to Qt 6.10.3 (match qt6-qtbase / qt6-rpm-macros)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-5
- Drop aarch64 %%_smp_mflags -j1 (still skip examples on aarch64 for mock disk)

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-3
- fix %%{?examples ON} so value 0 does not still enable QT_BUILD_EXAMPLES
- rm examples tree from buildroot when examples subpackage is off

* Thu Apr 09 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-2
- aarch64 skip examples and single-job build to avoid ENOSPC in mock

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.10.2-1
- Prepare for Oreon 11 (RP1)
