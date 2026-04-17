# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    powerdevil
Version: 6.6.3
Release: 1%{?dist}
Summary: Power management service for Plasma

License: BSD-2-Clause
URL:     https://invent.kde.org/plasma/%{name}

Source0: https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf6-kdoctools-devel
BuildRequires:  kf6-rpm-macros
BuildRequires:  ninja-build
BuildRequires:  qt6-qtbase-private-devel
BuildRequires:  qcoro-qt6-devel
BuildRequires:  wayland-devel
BuildRequires:  wayland-protocols-devel
BuildRequires:  libudev-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-renderutil-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-cursor-devel
BuildRequires:  xcb-util-errors-devel
BuildRequires:  pkgconfig(xcb-randr)
BuildRequires:  pkgconfig(xcb-dpms)
BuildRequires:  pkgconfig(ddcutil)

BuildRequires:  cmake(KF6Auth)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IdleTime)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6GlobalAccel)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Runner)
BuildRequires:  cmake(KF6Screen)
BuildRequires:  cmake(KF6Solid)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(KF6XmlGui)
BuildRequires:  cmake(LibKWorkspace)
BuildRequires:  cmake(Plasma)
BuildRequires:  cmake(PlasmaActivities)
BuildRequires:  cmake(PlasmaWaylandProtocols)

BuildRequires:  cmake(Qt6DBus)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6WaylandClient)
BuildRequires:  cmake(Qt6Widgets)

Requires:       kf6-filesystem

%description
PowerDevil is the power management service for Plasma. It handles battery and
AC events, display and keyboard brightness, suspend behavior, and power profiles.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-qt --all-name


%files -f %{name}.lang
%license LICENSES/*
%{_libexecdir}/org_kde_powerdevil
%{_kf6_libexecdir}/kauth/chargethresholdhelper
%{_kf6_libexecdir}/kauth/discretegpuhelper
%{_kf6_libexecdir}/kauth/backlighthelper
%{_kf6_libexecdir}/kauth/wakeupsourcehelper
%{_sysconfdir}/xdg/autostart/powerdevil.desktop
%{_userunitdir}/plasma-powerdevil.service
%{_datadir}/dbus-1/system-services/org.kde.powerdevil.*.service
%{_datadir}/polkit-1/actions/org.kde.powerdevil.*.policy
%{_kf6_datadir}/knotifications6/powerdevil.notifyrc
%{_kf6_datadir}/qlogging-categories6/powerdevil*.categories
%{_qt6_plugindir}/plasma/applets/*.so
%{_qt6_plugindir}/plasma/kcms/systemsettings/*.so
%{_qt6_plugindir}/kf6/krunner/krunner_powerdevil.so
%{_qt6_plugindir}/powerdevil/
%{_libdir}/qt6/qml/org/kde/plasma/private/batterymonitor/
%{_libdir}/qt6/qml/org/kde/plasma/private/brightnesscontrolplugin/
%{_libdir}/libpowerdevilcore.so.*


%changelog
* Tue Apr 14 2026 Oreon Packaging Team <packaging@oreonhq.com> - 6.6.3-1
- Add powerdevil package for Plasma power management
