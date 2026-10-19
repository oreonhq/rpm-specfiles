%global source0_hash 450f651d2864fa838a0f5f5054905d08d79e1850f95722e755ddb762be55aea3
%global repo dde-qt-dbus-factory
Name:           deepin-qt-dbus-factory
Version:        6.0.1
Release:        1%{?dist}
Summary:        A repository stores auto-generated Qt5 dbus code
License:        GPL-3.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/linuxdeepin/dde-qt-dbus-factory
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(gl)
BuildRequires:  python3
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
%description
A repository stores auto-generated Qt5 dbus code.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
Header files and libraries for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}
sed -i "s/env python$/env python3/g" libdframeworkdbus/generate_code.py

%build

%qmake_qt5 LIB_INSTALL_DIR=%{_libdir}
%make_build
%install
%make_install INSTALL_ROOT=%{buildroot}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n deepin-qt-dbus-factory-devel -f %{oreon_filedir}/deepin-qt-dbus-factory-devel.list

%changelog

%autochangelog
