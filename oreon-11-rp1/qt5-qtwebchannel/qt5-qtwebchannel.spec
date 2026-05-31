%global source0_hash none

%global qt_module qtwebchannel

Summary: Qt5 - WebChannel component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LICENSE.GPL LICENSE.LGPL LGPL_EXCEPTION.txt, for details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url: http://qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
## upstream patches
## repo: https://invent.kde.org/qt/qt/qtwebchannel
## branch: kde/5.15
## git format-patch v5.15.16-lts-lgpl
Patch1: 0001-Handle-signals-in-the-registered-object-s-thread.patch
Patch2: 0002-Handle-per-transport-client-idle-status.patch
Patch3: 0003-QMetaObjectPublisher-Never-send-stale-queued-message.patch

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-private-devel
#libQt5Core.so.5(Qt_5_PRIVATE_API)(64bit)
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtwebsockets-devel

%description
The Qt WebChannel module provides a library for seamless integration of C++
and QML applications with HTML/JavaScript clients. Any QObject can be
published to remote clients, where its public API becomes available.

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%{_qt5_libdir}/libQt5WebChannel.so.5*
%{_qt5_archdatadir}/qml/QtWebChannel/

%files devel
%{_qt5_headerdir}/QtWebChannel/
%{_qt5_libdir}/libQt5WebChannel.so
%{_qt5_libdir}/libQt5WebChannel.prl
%dir %{_qt5_libdir}/cmake/Qt5WebChannel/
%{_qt5_libdir}/cmake/Qt5WebChannel/Qt5WebChannelConfig*.cmake
%{_qt5_libdir}/pkgconfig/Qt5WebChannel.pc
%{_qt5_archdatadir}/mkspecs/modules/qt_lib_webchannel*.pri

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 5.15.18-2
- Import
