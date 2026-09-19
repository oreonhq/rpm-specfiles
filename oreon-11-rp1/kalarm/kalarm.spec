%global source0_hash 2ba214f9216f57b97899162aeb9ea7b7223edb2f7dba7ba49e8c9b0b10f72762

Name:    kalarm
Summary: Personal Alarm Scheduler
Version: 25.12.3
Release: 1%{?dist}

License: BSD-3-Clause AND CC0-1.0 AND GPL-2.0-or-later AND LGPL-2.0-or-later
URL:     https://www.kde.org/applications/utilities/kalarm

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

BuildRequires: cmake
BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Core5Compat)

BuildRequires: cmake(KF6Auth)
BuildRequires: cmake(KF6CalendarCore)
BuildRequires: cmake(KF6Codecs)
BuildRequires: cmake(KF6Completion)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Contacts)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6GuiAddons)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6ItemModels)
BuildRequires: cmake(KF6JobWidgets)
BuildRequires: cmake(KF6KIO)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6NotifyConfig)
BuildRequires: cmake(KF6Service)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)
BuildRequires: cmake(KF6TextWidgets)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(Phonon4Qt6)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6TextTemplate)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KPim6CalendarUtils)
BuildRequires: cmake(KPim6IdentityManagementWidgets)
BuildRequires: cmake(KPim6Mime)
BuildRequires: cmake(KF6TextEditTextToSpeech)
BuildRequires: cmake(KPim6Akonadi)
BuildRequires: cmake(KPim6AkonadiContactWidgets)
BuildRequires: cmake(KPim6AkonadiMime)
BuildRequires: cmake(KPim6MailTransport)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: vlc-devel
BuildRequires: mpv-devel

Provides:  kf6-kalarmcal = %{version}-%{release}

%description
KAlarm is a personal alarm message, command and email scheduler.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6 \
  -DENABLE_RTC_WAKE_FROM_SUSPEND:BOOL=%{!?flatpak:ON}%{?flatpak:OFF} \
  -DWITHOUT_X11=ON

%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name --with-html

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.%{name}.appdata.xml ||:

%files -f %{name}.lang
%license LICENSES/*
%{_datadir}/dbus-1/interfaces/org.kde.kalarm.kalarm.xml
%{_datadir}/kalarm/icons/oxygen/16x16/actions/*.png
%{_kf6_bindir}/kalarm
%{_kf6_bindir}/kalarmautostart
%{_kf6_datadir}/applications/org.kde.kalarm.desktop
%{_kf6_datadir}/config.kcfg/kalarmconfig.kcfg
%{_kf6_datadir}/icons/hicolor/*/apps/kalarm.*
%{_kf6_datadir}/kalarm/icons/oxygen/22x22/actions/*.png
%{_kf6_datadir}/knotifications6/kalarm.notifyrc
%{_kf6_datadir}/qlogging-categories6/*%{name}.*
%{_kf6_metainfodir}/org.kde.kalarm.appdata.xml
%{_sysconfdir}/xdg/autostart/kalarm.autostart.desktop
%{_kf6_libdir}/libkalarmcalendar.so.*
%{_kf6_libdir}/libkalarmplugin.so.*
%{_kf6_qtplugindir}/pim6/kalarm/
%{_kf6_datadir}/kconf_update/kalarm.upd
%{_kf6_libdir}/kconf_update_bin/kalarm-3.10.0-run_mode
%{_datadir}/icons/hicolor/22x22/actions/kalarm-*.png
%if %{undefined flatpak}
%{_kf6_libexecdir}/kauth/kalarm_helper
%{_datadir}/dbus-1/system-services/org.kde.kalarm.rtcwake.service
%{_datadir}/dbus-1/system.d/org.kde.kalarm.rtcwake.conf
%{_datadir}/polkit-1/actions/org.kde.kalarm.rtcwake.policy
%endif

%changelog
%autochangelog
