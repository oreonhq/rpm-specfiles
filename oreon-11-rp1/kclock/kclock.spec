%global source0_hash 60a1a3048bf5d508dfe6dfbf0cc70f9a6041d33476f579a23dc67325368a8de7

%global stable_kf6 stable


%global klockd_name org.kde.kclockd
%global orig_name org.kde.kclock


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:           kclock
Version:        26.08.1
Release:        1%{?dist}
License:        LGPL-2.1-or-later AND LGPL-2.0-or-later AND GPL-3.0-or-later AND CC-BY-4.0 AND GPL-2.0-or-later
Summary:        Clock app for Plasma Mobile
Url:            https://apps.kde.org/kclock/
Source0:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  appstream
 
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Svg)
BuildRequires:  cmake(Qt6QuickControls2)
BuildRequires:  cmake(Qt6Multimedia)
BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(Qt6WaylandClientPrivate)
BuildRequires:  cmake(Qt6CorePrivate)

BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6StatusNotifierItem)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6JobWidgets)

BuildRequires:  cmake(Plasma)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  cmake(PlasmaWaylandProtocols)
 
Requires:       hicolor-icon-theme
# QML module dependencies
Requires:       kf6-kcoreaddons%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       kf6-kirigami-addons-dateandtime%{?_isa}
Requires:       kf6-ksvg%{?_isa}
Requires:       qt6-qtmultimedia%{?_isa}


%description
A convergent clock application for Plasma.


%package plasma-applet
Summary:        Plasma applet for kclock
Requires:       %{name}%{?_isa} = %{version}-%{release}
# QML module dependencies
Requires:       kf6-kcmutils%{?_isa}
Requires:       kf6-kirigami%{?_isa}
Requires:       libplasma%{?_isa}

%description plasma-applet
%{summary}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version}


%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name


%check
appstreamcli validate --no-net %{buildroot}%{_datadir}/metainfo/org.kde.%{name}.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.%{name}.desktop

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_bindir}/%{name}
%{_kf6_bindir}/%{name}d
%{_kf6_datadir}/applications/%{orig_name}.desktop
%{_kf6_metainfodir}/%{orig_name}.appdata.xml
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.%{name}.svg
%{_sysconfdir}/xdg/autostart/%{klockd_name}-autostart.desktop
%{_datadir}/dbus-1/services/org.kde.%{name}d.service
%{_datadir}/krunner/dbusplugins/org.kde.kclock.desktop
%{_kf6_datadir}/knotifications6/%{name}d.notifyrc
%{_kf6_datadir}/dbus-1/interfaces/*.xml

%files plasma-applet
%{_kf6_datadir}/icons/hicolor/scalable/apps/kclock_plasmoid.svg
%{_datadir}/plasma/plasmoids/org.kde.plasma.%{name}_1x2/
%{_qt6_plugindir}/plasma/applets/org.kde.plasma.%{name}_1x2.so

%changelog
%autochangelog
