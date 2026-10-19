%global source0_hash 37d7ec67dea2234971d66f247ec9bd3c811e7c976402fa4a2f6831222da6b570
Name:          lxqt-panel
Summary:        Main panel bar for LXQt desktop suite
Version:       2.4.1
Release:        1%{?dist}
License:       LGPL-2.1-or-later
URL:           https://lxqt-project.org/
Source0:        https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0101:   0101-use-wlroots-backend-with-unknown-compositors.patch
%dnl BuildRequires:  fdupes
Requires: lxqt-menu-data
Requires: xscreensaver-base
Requires: lxmenu-data
# oreon:deps
BuildRequires:  cmake
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  libXdamage-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  lxqt-menu-data
BuildRequires:  perl
BuildRequires:  pkgconfig(Qt6Xdg)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(dbusmenu-lxqt)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(lxqt-globalkeys)
BuildRequires:  pkgconfig(sysstat-qt6)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  wayland-devel
BuildRequires:  xcb-util-image-devel
# /oreon:deps
%description
%{summary}.

%package devel
Summary:  Developer files for %{name}
Requires: %{name} = %{version}-%{release}
%description devel
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-panel
Requires:       lxqt-panel
%description l10n
This package provides translations for the lxqt-panel package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%cmake
%cmake_build
%install
%cmake_install
for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
  desktop-file-edit --remove-category=LXQt --remove-only-show-in=LXQt --add-only-show-in=X-LXQt ${desktop}
done
desktop-file-validate %{buildroot}/%{_datadir}/applications/lxqt-panel.desktop ||:
%dnl %fdupes -s %{buildroot}%{_datadir}/lxqt
%find_lang lxqt-panel --with-qt
%find_lang cpuload --with-qt
%find_lang desktopswitch --with-qt
%find_lang directorymenu --with-qt
%find_lang mainmenu --with-qt
%find_lang mount --with-qt
%find_lang networkmonitor --with-qt
%find_lang quicklaunch --with-qt
%find_lang sensors --with-qt
%find_lang showdesktop --with-qt
%find_lang spacer --with-qt
%find_lang statusnotifier --with-qt
%find_lang sysstat --with-qt
%find_lang taskbar --with-qt
%find_lang volume --with-qt
%find_lang worldclock --with-qt
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n lxqt-panel-devel -f %{oreon_filedir}/lxqt-panel-devel.list
%files -n lxqt-panel-l10n -f %{oreon_filedir}/lxqt-panel-l10n.list

%changelog

%autochangelog
