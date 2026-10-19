%global source0_hash ee2e913bbb2117bb24aebcf60c0542d1f9df3f2f48c13e5463d92ce4b8f45ed1
Name:           plasma-settings
Version: 26.08.0
Release:        1%{?dist}
License:        BSD-2-Clause AND CC-BY-4.0 AND CC0-1.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-only
Summary:        Convergent Plasma Mobile settings application
Url:            https://invent.kde.org/plasma-mobile/plasma-settings
Source0:        https://download.kde.org/stable/release-service/%{version}/src/plasma-settings-%{version}.tar.xz
Requires:       ((pulseaudio-module-gsettings and sound-theme-freedesktop) if pulseaudio)
Requires:       polkit-kde
Requires:       accountsservice
# oreon:deps
BuildRequires:  appstream
BuildRequires:  cmake
BuildRequires:  cmake(KF6Config)
BuildRequires:  cmake(KF6CoreAddons)
BuildRequires:  cmake(KF6Crash)
BuildRequires:  cmake(KF6DBusAddons)
BuildRequires:  cmake(KF6I18n)
BuildRequires:  cmake(KF6ItemModels)
BuildRequires:  cmake(KF6ItemViews)
BuildRequires:  cmake(KF6KCMUtils)
BuildRequires:  cmake(KF6KirigamiAddons)
BuildRequires:  cmake(KF6Service)
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Quick)
BuildRequires:  cmake(Qt6Test)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  desktop-file-utils
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  kf6-rpm-macros
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-2.0)
# /oreon:deps
%description
Convergent settings application for Plasma Mobile.
Notice that Wi-Fi, mobile broadband and hotspot KConfig
modules are provided separately, by plasma-nm.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

%cmake_kf6
%cmake_build
%install
%cmake_install
%find_lang %{name} --all-name
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_kf6_datadir}/applications/org.kde.mobile.plasmasettings.desktop
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.mobile.plasmasettings.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
