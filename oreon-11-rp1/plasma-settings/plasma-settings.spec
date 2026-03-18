Name:           plasma-settings
Version:        26.02.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
Summary:        Convergent Plasma Mobile settings application
Url:            https://invent.kde.org/plasma-mobile/plasma-settings
Source0:        https://download.kde.org/stable/plasma-settings/%{name}-%{version}.tar.xz

BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libappstream-glib
BuildRequires:  kf6-rpm-macros

BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Widgets)

BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6ItemModels)

BuildRequires:  pkgconfig(gobject-2.0)

Requires:       ((pulseaudio-module-gsettings and sound-theme-freedesktop) if pulseaudio)
Requires:       polkit-kde
Requires:       accountsservice

%description
Convergent settings application for Plasma Mobile.
Notice that Wi-Fi, mobile broadband and hotspot KConfig
modules are provided separately, by plasma-nm.

%prep
%autosetup -p1

%build
%cmake_kf6
%cmake_build

%install
%cmake_install
%find_lang %{name} --all-name

%check
desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.mobile.plasmasettings.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.mobile.plasmasettings.metainfo.xml

%files -f %{name}.lang
%doc README.md
%license LICENSES/*
%{_kf6_datadir}/icons/hicolor/scalable/apps/org.kde.mobile.plasmasettings.svg
%{_kf6_bindir}/plasma-settings
%{_kf6_datadir}/applications/org.kde.mobile.plasmasettings.desktop
%{_kf6_metainfodir}/org.kde.mobile.plasmasettings.metainfo.xml
%{_kf6_datadir}/plasma-settings/

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 26.02.0-1
- Prepare for Oreon 11 (RP1)
