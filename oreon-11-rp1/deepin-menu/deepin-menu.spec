%global source0_hash 023ac19dbd348a3950b64445d11b1799418b4365a66057b2d96dd9104ff9a5bb
Name:           deepin-menu
Version:        5.0.1
Release:        1%{?dist}
Summary:        Deepin menu service
License:        GPLv3+
URL:            https://github.com/linuxdeepin/deepin-menu
Source0:        https://github.com/linuxdeepin/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  make
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5MultimediaWidgets)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(dframeworkdbus)
BuildRequires:  pkgconfig(dtkwidget)
BuildRequires:  qt5-qtbase-private-devel
# /oreon:deps
%description
Deepin menu service for building beautiful menus.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Modify lib path to reflect the platform
sed -i 's|/usr/bin|%{_libexecdir}|' data/com.deepin.menu.service \
    deepin-menu.desktop deepin-menu.pro

%build

%qmake_qt5 DEFINES+=QT_NO_DEBUG_OUTPUT
%make_build
%install
%make_install INSTALL_ROOT="%{buildroot}"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
