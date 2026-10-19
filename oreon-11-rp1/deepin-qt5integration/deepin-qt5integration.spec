%global source0_hash 987dddb3c9f655724cb71b2c6dd01462d984efe32d9fe1fbea956ecb6541f349
%global repo qt5integration
%global __provides_exclude_from ^%{_qt5_plugindir}/.*\.so$
Name:           deepin-qt5integration
Version:        6.7.49
Release:        1%{?dist}
Summary:        Qt platform theme integration plugins for DDE
License:        LGPL-3.0-or-later
URL:            https://github.com/linuxdeepin/qt5integration
Source0:        https://github.com/linuxdeepin/%{repo}/archive/%{version}/%{repo}-%{version}.tar.gz
%{?_qt5:Requires: %{_qt5}%{?_isa} = %{_qt5_version}}
Requires:       deepin-qt5platform-plugins%{?_isa}
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(DtkWidget)
BuildRequires:  cmake(Qt5Concurrent)
BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5ThemeSupport)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5X11Extras)
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(mtdev)
BuildRequires:  pkgconfig(x11)
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtbase-static
# /oreon:deps
%description
Multiple Qt plugins to provide better Qt5 integration for DDE is included.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{repo}-%{version}

%build

%cmake -DENABLE_QT_XDG_ICON_LOADER=OFF -DBUILD_TESTS=OFF
%cmake_build
%install
%cmake_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
