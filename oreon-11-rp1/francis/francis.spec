
# https://fedoraproject.org/wiki/Changes/EncourageI686LeafRemoval
ExcludeArch: %{ix86}

Name:          francis
Version:       25.12.3
Release:       1%{?dist}
License:       BSD-2-Clause AND BSD-3-Clause AND CC0-1.0 AND GPL-3.0-or-later AND LGPL-2.0-or-later AND LGPL-2.1-or-later
Summary:       Time tracking app for KDE Plasma
URL:           https://apps.kde.org/francis/
Source:        https://download.kde.org/%{stable_kf6}/release-service/%{version}/src/%{name}-%{version}.tar.xz

# upstream patches

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Svg)
BuildRequires: cmake(Qt6Widgets)

BuildRequires: cmake(KF6Kirigami)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(KF6Config)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6KirigamiAddons)

Requires: hicolor-icon-theme
Requires: qt6qml(org.kde.coreaddons)
Requires: qt6qml(org.kde.kirigami)
Requires: qt6qml(org.kde.kirigamiaddons.formcard)
Requires: qt6qml(org.kde.notification)


%description
Francis is a time tracking app using the well-known
pomodoro technique to help you get more productive.


%prep
%autosetup -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang %{name} --with-man --with-qt --all-name

%check
desktop-file-validate %{buildroot}%{_kf6_datadir}/applications/org.kde.francis.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.metainfo.xml

%files -f %{name}.lang
%license LICENSES/*
%{_kf6_bindir}/francis
%{_kf6_datadir}/applications/org.kde.francis.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.francis.svg
%{_metainfodir}/org.kde.francis.metainfo.xml


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 25.12.3-1
- Prepare for Oreon 11 (RP1)
