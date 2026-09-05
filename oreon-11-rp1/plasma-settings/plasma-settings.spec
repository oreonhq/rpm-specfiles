%global source0_hash 598a5f8f28785148c7e527802398011660dbd72e1c4c5628d291679069d00530

Name:           plasma-settings
Version: 26.08.0
Release: 1%{?dist}
License:        BSD-2-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
Summary:        Convergent Plasma Mobile settings application
Url:            https://invent.kde.org/plasma-mobile/plasma-settings
Source0:        https://download.kde.org/stable/release-service/%{version}/src/plasma-settings-%{version}.tar.xz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plasma-settings-v26.03.80

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
%autochangelog
