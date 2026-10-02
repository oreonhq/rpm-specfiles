%global source0_hash 1f6c0b01327b4b5e2ddcf11fd8e4b3e66ba492c9c66c61a95d4ddfd258850d5f

%global stable_kf6 stable


# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:    bluedevil
Summary: Bluetooth stack for KDE
Version:        6.7.5
Release: 1%{?dist}

License: GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git

Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig


BuildRequires:  extra-cmake-modules
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6Service)
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
# runtime
BuildRequires:  cmake(KF6Kirigami)

# Plasma
BuildRequires:  cmake(Plasma)

BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  shared-mime-info
BuildRequires:  desktop-file-utils

Provides:       dbus-bluez-pin-helper

Obsoletes:      kbluetooth < 0.4.2-3
Obsoletes:      bluedevil-devel < 2.0.0-0.10

Requires:       bluez >= 5
Requires:       bluez-obexd
Requires:       kf6-kded
Requires:       pulseaudio-module-bluetooth
# runtime
Requires:       kf6-kirigami

# When -autostart was removed
Obsoletes:      bluedevil-autostart < 5.2.95

%description
BlueDevil is the bluetooth stack for KDE.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -p1


%build
%cmake_kf6
%cmake_build

%install
%cmake_install

%find_lang %{name} --all-name --with-html


%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilsendfile.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilwizard.desktop


%files -f %{name}.lang
%doc README
%{_datadir}/mime/packages/bluedevil-mime.xml
%{_kf6_bindir}/bluedevil-sendfile
%{_kf6_bindir}/bluedevil-wizard
%{_kf6_datadir}/applications/kcm_bluetooth.desktop
%{_kf6_datadir}/applications/org.kde.bluedevilsendfile.desktop
%{_kf6_datadir}/applications/org.kde.bluedevilwizard.desktop
%{_kf6_datadir}/bluedevilwizard/
%{_kf6_datadir}/knotifications6/bluedevil.notifyrc
%{_kf6_qmldir}/org/kde/bluedevil/
%{_kf6_qtplugindir}/plasma/applets/org.kde.plasma.bluetooth.so
%{_kf6_datadir}/qlogging-categories6/bluedevil.categories
%{_kf6_datadir}/remoteview/bluetooth-network.desktop
%{_kf6_plugindir}/kded/*.so
%{_kf6_plugindir}/kio/*.so
%{_kf6_qmldir}/org/kde/plasma/private/bluetooth/
%{_kf6_qtplugindir}/plasma/kcms/systemsettings/kcm_bluetooth.so


%changelog
%autochangelog
