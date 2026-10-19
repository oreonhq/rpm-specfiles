%global source1_hash b4c0e6098cf83e959747f07974752ef690095d849a9df643ab76680ab4a87ba8
%global source0_hash 1f6c0b01327b4b5e2ddcf11fd8e4b3e66ba492c9c66c61a95d4ddfd258850d5f
%global stable_kf6 stable
ExcludeArch: %{ix86}
Name:    bluedevil
Summary:        Bluetooth stack for KDE
Version:        6.7.5
Release:        1%{?dist}
License: GPL-2.0-or-later
URL:     https://cgit.kde.org/%{name}.git
Source0:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz
Source1:        https://download.kde.org/%{stable_kf6}/plasma/%{version}/%{name}-%{version}.tar.xz.sig
Provides:       dbus-bluez-pin-helper
Obsoletes:      kbluetooth < 0.4.2-3
Obsoletes:      bluedevil-devel < 2.0.0-0.10
Requires:       bluez >= 5
Requires:       bluez-obexd
Requires:       kf6-kded
Requires:       pulseaudio-module-bluetooth
Requires:       kf6-kirigami
Obsoletes:      bluedevil-autostart < 5.2.95
# oreon:deps
BuildRequires:  cmake(KF6BluezQt)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6Declarative)
BuildRequires:  cmake(KF6DocTools)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6IconThemes)
BuildRequires:  cmake(KF6JobWidgets)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KDED)
BuildRequires:  cmake(KF6KIO)
BuildRequires:  cmake(KF6Kirigami)
BuildRequires:  cmake(KF6Notifications)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6Svg)
BuildRequires:  cmake(KF6WidgetsAddons)
BuildRequires:  cmake(KF6WindowSystem)
BuildRequires:  cmake(Plasma)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  kf6-rpm-macros
BuildRequires:  qt6-qtbase-devel
BuildRequires:  qt6-qtdeclarative-devel
BuildRequires:  shared-mime-info
# /oreon:deps
%description
BlueDevil is the bluetooth stack for KDE.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name --with-html
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilsendfile.desktop
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.bluedevilwizard.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
