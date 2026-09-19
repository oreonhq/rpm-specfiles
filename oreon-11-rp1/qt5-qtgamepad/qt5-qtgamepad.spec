%global source0_hash 7f5cf698b7e21a076f78e4bad0d463ef1bdc58b64b9c31262b74556f56b5bf99

%global qt_module qtgamepad

Summary: Qt5 - Gamepad component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release: 2%{?dist}

# See LGPL_EXCEPTIONS.txt, LICENSE.GPL3, respectively, for exception details
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0: https://download.qt.io/official_releases/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz

BuildRequires: make
BuildRequires: qt5-qtbase-devel >= %{version}
BuildRequires: qt5-qtbase-static >= %{version}
BuildRequires: qt5-qtbase-private-devel
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
BuildRequires: qt5-qtdeclarative-devel >= %{version}
BuildRequires: pkgconfig(xrender)
BuildRequires: pkgconfig(libudev)
BuildRequires: pkgconfig(sdl2)

%description
Qt Gamepad provides a way to display web content in a QML application without necessarily
including a full web browser stack by using native APIs where it makes sense.

%package devel
Summary: Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: qt5-qtbase-devel%{?_isa}
Requires: qt5-qtdeclarative-devel%{?_isa}
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
mkdir %{_target_platform}
pushd %{_target_platform}
%{qmake_qt5} ..
popd

%make_build -C %{_target_platform}

%if 0%{?docs}
%make_build docs -C %{_target_platform}
%endif

%install
make install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%if 0%{?docs}
make install_docs INSTALL_ROOT=%{buildroot} -C %{_target_platform}
%endif

%ldconfig_scriptlets

%files
%license LICENSE.GPL LICENSE.LGPLv3
%{_qt5_libdir}/libQt5Gamepad.so.5*
%{_qt5_qmldir}/QtGamepad/
%{_qt5_plugindir}/gamepads/

%files devel
%{_qt5_headerdir}/QtGamepad/
%{_qt5_libdir}/libQt5Gamepad.so
%{_qt5_libdir}/libQt5Gamepad.prl
%{_qt5_libdir}/pkgconfig/Qt5Gamepad.pc
%{_qt5_libdir}/cmake/Qt5Gamepad
%{_qt5_archdatadir}/mkspecs/modules/*
%exclude %{_qt5_libdir}/libQt5Gamepad.la

%if 0%{?_qt5_examplesdir:1}
%files examples
%{_qt5_examplesdir}/
%endif

%changelog
%autochangelog
