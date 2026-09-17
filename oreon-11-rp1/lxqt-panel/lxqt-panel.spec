%global source0_hash 6e42cb032186e0b18e2649aed2ef57ef7d1f63cc81a6f38a7918f62c573a906d

Name:          lxqt-panel
Summary:       Main panel bar for LXQt desktop suite
Version:       2.3.2
Release:       2%{?dist}
License:       LGPL-2.1-or-later
URL:           https://lxqt-project.org/
Source0:       https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

# Proposed upstream
# https://github.com/lxqt/lxqt-panel/pull/2161
Patch0101:   0101-use-wlroots-backend-with-unknown-compositors.patch

BuildRequires:  cmake
%dnl BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  git-core
BuildRequires:  pkgconfig(Qt6Xdg)
BuildRequires:  pkgconfig(lxqt)
BuildRequires:  pkgconfig(lxqt-globalkeys)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-damage)
BuildRequires:  pkgconfig(xcb-xkb)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(libstatgrab)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libmenu-cache)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(sysstat-qt6)
BuildRequires:  cmake(lxqt2-build-tools)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6LinguistTools)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6Xml)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  pkgconfig(dbusmenu-lxqt)
BuildRequires:  desktop-file-utils
BuildRequires:  lm_sensors-devel
BuildRequires:  libXdamage-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  cmake(LayerShellQt)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  xcb-util-image-devel
BuildRequires:  lxqt-menu-data
BuildRequires:  perl
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  wayland-devel
BuildRequires:  qt6-qtbase-private-devel
Requires: lxqt-menu-data

Requires: xscreensaver-base
Requires: lxmenu-data

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

%autosetup -S git_am

%build
%cmake
%cmake_build

%install
%cmake_install

for desktop in %{buildroot}/%{_datadir}/lxqt/lxqt-panel/*.desktop; do
  # Exclude category as been Service
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

%files
%{_bindir}/lxqt-panel
%dir %{_libdir}/lxqt-panel
%{_libdir}/lxqt-panel/
%{_datadir}/lxqt
%{_mandir}/man1/lxqt-panel*
%config(noreplace) %{_sysconfdir}/xdg/autostart/lxqt-panel.desktop
%{_datadir}/applications/lxqt-panel.desktop
%config %{_sysconfdir}/xdg/lxqt/panel.conf

%files devel
%dir %{_includedir}/lxqt
%{_includedir}/lxqt/*

%files l10n -f lxqt-panel.lang -f cpuload.lang -f desktopswitch.lang -f directorymenu.lang  -f mainmenu.lang -f mount.lang -f networkmonitor.lang -f quicklaunch.lang -f sensors.lang -f showdesktop.lang -f spacer.lang -f statusnotifier.lang -f sysstat.lang -f taskbar.lang -f volume.lang -f worldclock.lang
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%dir %{_datadir}/lxqt/translations/lxqt-panel

%changelog
%autochangelog
