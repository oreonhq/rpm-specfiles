%global source0_hash 7f5cf698b7e21a076f78e4bad0d463ef1bdc58b64b9c31262b74556f56b5bf99
%global qt_module qtgamepad
Summary:        Qt5 - Gamepad component
Name:    qt5-%{qt_module}
Version: 5.15.18
Release:        1%{?dist}
License: LGPL-3.0-only OR GPL-3.0-only WITH Qt-GPL-exception-1.0
Url:     http://www.qt.io
%global majmin %(echo %{version} | cut -d. -f1-2)
Source0:        https://download.qt.io/archive/qt/%{majmin}/%{version}/submodules/%{qt_module}-everywhere-opensource-src-%{version}.tar.xz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
# oreon:deps
BuildRequires:  make
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
BuildRequires:  qt5-qtdeclarative-devel
# /oreon:deps
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
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n qt5-qtgamepad-devel -f %{oreon_filedir}/qt5-qtgamepad-devel.list
%files -n qt5-qtgamepad-examples -f %{oreon_filedir}/qt5-qtgamepad-examples.list

%changelog

%autochangelog
