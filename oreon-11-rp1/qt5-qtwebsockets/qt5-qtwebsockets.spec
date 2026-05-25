%global qt_module qtwebsockets

Summary: Qt5 - WebSockets component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url: http://qt-project.org/
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

## upstream patches
## repo: https://invent.kde.org/qt/qt/qtwebsockets
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1:   0001-Clear-frame-on-reconnect.patch
Patch2:   0002-Disconnect-when-handshake-fails.patch

Patch100: %{name}-gcc11.patch

# filter qml provides
%global __provides_exclude_from ^%{_qt5_archdatadir}/qml/.*\\.so$

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel

%description
The QtWebSockets module implements the WebSocket protocol as specified in RFC
6455. It solely depends on Qt (no external dependencies).

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
%autosetup -n %{qt_module}-everywhere-src-%{version} -p1


%build
%{qmake_qt5}

%make_build


%install
make install INSTALL_ROOT=%{buildroot}

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
%license LICENSE.*
%{_qt5_libdir}/libQt5WebSockets.so.5*
%{_qt5_archdatadir}/qml/Qt/WebSockets/

%files devel
%{_qt5_headerdir}/QtWebSockets/
%{_qt5_libdir}/libQt5WebSockets.so
%{_qt5_libdir}/libQt5WebSockets.prl
%dir %{_qt5_libdir}/cmake/Qt5WebSockets/
%{_qt5_libdir}/cmake/Qt5WebSockets/Qt5WebSocketsConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5WebSockets.pc
%{_qt5_libdir}/qt5/qml/QtWebSockets/
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_websockets*.pri

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
