%global source0_hash e310b9abda691a23767579b35cf468b63dccb7a03ed47cdd63e2ccbb5818fc10

Name:    kmix
Summary: KDE volume control
Version: 25.12.3
Release: 1%{?dist}

License: CC0-1.0 AND GPL-2.0-or-later
URL:     https://invent.kde.org/multimedia/%{name}

Source0: http://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

## upstream patches

## upstreamable patches
# disable autostart by default (on newer plasma releases that use plasma-pa)
Patch2:  kmix-21.04.0-autostart_disable.patch

BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(alsa)
BuildRequires: pkgconfig(libcanberra)
BuildRequires: pkgconfig(libpulse) pkgconfig(libpulse-mainloop-glib)

BuildRequires: extra-cmake-modules
BuildRequires: kf6-rpm-macros
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Crash)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6DocTools)
BuildRequires: cmake(KF6GlobalAccel)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6StatusNotifierItem)
BuildRequires: cmake(KF6WidgetsAddons)
BuildRequires: cmake(KF6WindowSystem)
BuildRequires: cmake(KF6XmlGui)

BuildRequires: pkgconfig(Qt5Gui)

# when split occurred
Obsoletes: kdemultimedia-kmix < 6:4.8.80
Provides:  kdemultimedia-kmix = 6:%{version}-%{release}

# translations moved here
Conflicts: kde-l10n < 17.03

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%cmake_kf6

%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html --with-man

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.kmix.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.kmix.desktop

%files -f %{name}.lang
%doc AUTHORS ChangeLog TODO
%license COPYING*
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kmix.control.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kmix.mixer.xml
%{_kf6_datadir}/dbus-1/interfaces/org.kde.kmix.mixset.xml
%{_kf6_datadir}/icons/hicolor/*/*/kmix.*
%{_kf6_bindir}/kmix
%{_kf6_bindir}/kmixctrl
%{_kf6_bindir}/kmixremote
%{_kf6_datadir}/applications/org.kde.kmix.desktop
%{_kf6_metainfodir}/org.kde.kmix.appdata.xml
%{_kf6_datadir}/config.kcfg/kmixsettings.kcfg
%{_kf6_datadir}/kmix/
%{_kf6_datadir}/kxmlgui5/kmix/
%{_kf6_datadir}/qlogging-categories6/kmix*
%{_sysconfdir}/xdg/autostart/restore_kmix_volumes.desktop
%{_sysconfdir}/xdg/autostart/kmix_autostart.desktop
%{_kf6_datadir}/knotifications6/kmix.notifyrc
# -libs subpkg?
%{_kf6_libdir}/libkmixcore.so.6*
%{_kf6_libdir}/libkmixcore.so.%{version}

%changelog
%autochangelog
